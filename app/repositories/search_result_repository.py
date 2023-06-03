from flask import abort, request
from ..models.search_result_model import SearchResult
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from ..config import database as dbase

db = dbase.connect()


class SearchResultRepository(AbstractRepository[SearchResult]):
    pass
