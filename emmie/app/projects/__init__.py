# -*- coding:utf-8 -*-
import os

from emmie.app.projects.wsgi import ProjectApplication
from mako.lookup import TemplateLookup
from emmie.models import Project
from webhelpers2.containers import correlate_objects


def make_project_app(assets):
    here = os.path.dirname(__file__)
    templates = TemplateLookup(
        directories=[os.path.join(here, "templates")],
    )
    repository = ProjectRepository(Project)
    project_app = ProjectApplication(templates=templates,
                             assets=assets,
                             repository=repository)
    return project_app


class ProjectRepository(object):
    def __init__(self, resource_class):
        self.resource_class = resource_class

    def query(self):
        return self.resource_class.query

    def values(self):
        return self.query().all()

    def items(self):
        projects = self.values()
        return correlate_objects(projects, "id")