from sqlalchemy.orm import relationship  # Import
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,  # import
)

from .meta import Base


class WeatherLocation(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    zip_code = Column(Integer, unique=True)

    # NOTE: Added account and account_id refs for relationship management
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    account = relationship('Account', back_populates='location')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        location = cls(**kwargs)
        request.dbsession.add(location)

        return request.dbsession.query(cls).filter(
            cls.zip_code == kwargs['zip_code']).one_or_none()

    @classmethod
    def one(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def all(cls, request):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

    @classmethod
    def remove(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()


Index('my_account', WeatherLocation.name, unique=True, mysql_length=255)
