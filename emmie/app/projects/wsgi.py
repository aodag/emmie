# -*- coding:utf-8 -*-
from emmie.templating.dec import templating
from webob.dec import wsgify
from webdispatch.urldispatcher import URLDispatcher


class ProjectApplication(URLDispatcher):
    def __init__(self, *, templates, assets, repository):
        extra_environ = {
            "templates": templates,
        }
        super(ProjectApplication, self).__init__(extra_environ=extra_environ)
        self.assets = assets
        self.repository = repository

        self.add_url("top", "", self.index)

    @wsgify
    @templating("index.html")
    def index(self, request):
        projects = self.repository.values()
        return dict(assets=self.assets,
                    projects=projects)