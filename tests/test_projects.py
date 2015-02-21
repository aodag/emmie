# -*- coding:utf-8 -*-
import unittest

from testfixtures import compare, Comparison as C

from emmie.testing import (
    DummyRenderer,
    DummyTemplateLookup,
)
import webob


class MyTestCase(unittest.TestCase):

    def _get_target(self):
        from emmie.app.projects.wsgi import ProjectApplication
        return ProjectApplication

    def _make_one(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_index(self):
        templates = DummyTemplateLookup()
        templates["index.html"] = DummyRenderer("OK")
        request = webob.Request.blank("/", environ={"templates": templates})
        assets = object()
        target = self._make_one(
            templates=templates,
            assets=assets,
            repository=dict(),
        )

        res = request.get_response(target.index)

        compare(res.text, "OK")
        compare(templates["index.html"].called,
                [('render', {'request': C(webob.Request),
                             'environ': request.environ,
                             'assets': assets})])
        compare(templates.called, [('get_template', 'index.html')])


if __name__ == '__main__':
    unittest.main()
