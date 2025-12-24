from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from core.models import Base
from .mixins.int_id_pk import IntIdPkMixin

class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass