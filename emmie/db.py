# -*- coding:utf-8 -*-
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
import zope.sqlalchemy

DBSession = scoped_session(sessionmaker())
zope.sqlalchemy.register(DBSession)


def init_db(engine):
    DBSession.remove()
    DBSession.configure(bind=engine)