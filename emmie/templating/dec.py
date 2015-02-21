# -*- coding:utf-8 -*-
from functools import wraps


def render(environ, template_name, data):
    return environ["templates"].get_template(template_name).render(**data)


def templating(template_name):
    def dec(app):

        @wraps(app)
        def wsgi_app(*args):
            data = app(*args)
            request = args[0] if len(args) == 1 else args[1]
            environ = request.environ
            if isinstance(data, dict):
                data.update(
                    request=request,
                    environ=environ,
                )
                return render(environ, template_name, data)
            return data
        return wsgi_app
    return dec