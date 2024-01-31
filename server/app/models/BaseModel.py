from ..db import session
class BaseModel:

    def __init__(self):
        self.__session = session
        self._query = self._get_query()

    def _get_query(self):
        return self.__session.query(self.__class__)
    def get(self,id):
        return self._query.filter(self.__class__.id == id).one()

    def get_all(self):
        return self._query.all()