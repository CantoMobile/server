from flask import abort, request
from ..models.user_site_model import UserSite
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from main import db


class UserSiteRepository(AbstractRepository[UserSite]):
    pass