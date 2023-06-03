from flask import abort, request
from ..models.role_model import Role
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from ..config import database as dbase

db = dbase.connect()


class RoleRepository(AbstractRepository[Role]):
    pass
