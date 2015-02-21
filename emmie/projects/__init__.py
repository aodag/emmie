# -*- coding:utf-8 -*-
import os
from .app import ProjectApplication
from mako.lookup import TemplateLookup


def make_project_app(assets):
    here = os.path.dirname(__file__)
    templates = TemplateLookup(
        directories=[os.path.join(here, "templates")],
    )
    repository = dict()
    project_app = ProjectApplication(templates=templates,
                             assets=assets,
                             repository=repository)
    return project_app