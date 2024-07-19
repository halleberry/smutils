
import posixpath
import sys
from typing import List

from multi_language_strings.core.repository.model.multi_language_string_model import MultiLanguageStringModel as _Model

sys.path.append(posixpath.dirname(__file__))


class MultiLanguageStringRepository:
    def __init__(self, session):
        self._session = session

    def add(self, payload: dict) -> _Model:
        _record = _Model(**payload)
        self._session.add(_record)
        return _record

    def _get(self, id_, **filters) -> _Model:
        return self._session.query(_Model).filter(_Model.id == str(id_)).filter_by(**filters).first()

    def get(self, id_, **filters):
        return self._get(id_, **filters)

    def list(self, limit=None, **filters) -> List[_Model]:
        _records = self._session.query(_Model).filter_by(**filters).limit(limit).all()
        return [_record for _record in _records]

    def update(self, id_, payload: dict, **filters) -> _Model:
        _record = self._get(id_, **filters)
        self._session.delete(_record)
        for k, v in payload.items():
            setattr(_record, k, v)
        self._session.add(_record)

        return _record

    def delete(self, id_, **filters):
        _record = self._get(id_, **filters)
        self._session.delete(_record)



