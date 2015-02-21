# -*- coding:utf-8 -*-
import argparse

import waitress
from whitenoise import WhiteNoise
from backlash import DebuggedApplication
from emmie.app.projects import make_project_app
from emmie.assetbundles import assets
from rutter.urlmap import URLMap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    application = URLMap()
    project_app = make_project_app(assets=assets)
    application['/projects'] = project_app
    application = WhiteNoise(application)
    application.add_files(
        assets.directory,
        prefix=assets.url,
    )
    application = DebuggedApplication(application)
    waitress.serve(application,
                   port=args.port)


if __name__ == '__main__':
    main()