from flask import abort, request
from ..models.user_site_model import UserSite
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from ..config import database as dbase

db = dbase.connect()


class UserSiteRepository(AbstractRepository[UserSite]):
    pass