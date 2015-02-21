# -*- coding:utf-8 -*-
class DummyRenderer(object):
    def __init__(self, result):
        self.called = []
        self.result = result

    def render(self, **kwargs):
        self.called.append(('render', kwargs))
        return self.result


class DummyTemplateLookup(dict):
    def __init__(self):
        super(DummyTemplateLookup, self).__init__()
        self.called = []

    def get_template(self, name):
        self.called.append(("get_template", name))
        return self[name]