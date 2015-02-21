# -*- coding:utf-8 -*-
from datetime import datetime
import pytz
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession

Base = declarative_base()


def utcnow():
    now = datetime.utcnow()
    return pytz.utc.localize(now)


class Project(Base):
    __tablename__ = 'projects'
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    description = Column(UnicodeText)
    created_at = Column(DateTime,
                        default=lambda: utcnow())
    updated_at = Column(DateTime,
                        default=lambda: utcnow(),
                        onupdate=lambda: utcnow())