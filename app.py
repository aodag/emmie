# -*- coding:utf-8 -*-
import argparse

from emmie.app.projects import make_project_app
from emmie.assetbundles import assets
from emmie.db import init_db

import waitress
from whitenoise import WhiteNoise
from backlash import DebuggedApplication
from rutter.urlmap import URLMap
from sqlalchemy import create_engine
from repoze.tm import TM, default_commit_veto


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("database_url")
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()

    engine = create_engine(args.database_url)
    init_db(engine)

    application = URLMap()
    project_app = make_project_app(assets=assets)
    application['/projects'] = project_app
    application = TM(application,
                     commit_veto=default_commit_veto)
    application = WhiteNoise(application)
    application.add_files(
        assets.directory,
        prefix=assets.url,
    )
    if args.debug:
        engine.echo = True
        application = DebuggedApplication(application)

    waitress.serve(application,
                   port=args.port)


if __name__ == '__main__':
    main()