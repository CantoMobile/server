from flask import abort, request
from ..models.site_stats_model import SiteStats
from bson.objectid import ObjectId
from .abstract_repository import AbstractRepository
from ..config import database as dbase

db = dbase.connect()


class SiteStatsRepository(AbstractRepository[SiteStats]):
    pass