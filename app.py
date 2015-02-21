# -*- coding:utf-8 -*-
import waitress
from whitenoise import WhiteNoise
from backlash import DebuggedApplication
from emmie.projects import make_project_app
from emmie.assetbundles import assets
from rutter.urlmap import URLMap


def main():
    application = URLMap()
    project_app = make_project_app(assets=assets)
    application['/projects'] = project_app
    application = WhiteNoise(application)
    application.add_files(
        assets.directory,
        prefix=assets.url,
    )
    application = DebuggedApplication(application)
    waitress.serve(application)


if __name__ == '__main__':
    main()