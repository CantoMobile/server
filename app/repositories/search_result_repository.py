from flask import abort, request
from ..models.search_result_model import SearchResult
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from main import db


class SearchResultRepository(AbstractRepository[SearchResult]):
    pass
