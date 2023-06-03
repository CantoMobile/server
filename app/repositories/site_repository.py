from flask import abort, request
from ..models.site_model import Site
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from ..config import database as dbase

db = dbase.connect()


class SiteRepository(AbstractRepository[Site]):
    pass
