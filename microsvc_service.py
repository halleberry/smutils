from typing import List

from multi_language_strings.core.domain.multi_language_string import MultiLanguageString as _Domain


class MultiLanguageStringService:
    def __init__(self, repository):
        self._repository = repository

    def get(self, limit=None, **filters) -> List[_Domain]:
        _records = self._repository.list(limit, **filters)
        return [_Domain(**_record.dictionary) for _record in _records]

    def save(self, payload: dict):
        _record = self._repository.add(payload)
        return _Domain(**_record.dictionary, db_record_=_record)

    def show(self, id_, **filters) -> _Domain:
        _record = self._repository.get(id_, **filters)
        return _Domain(**_record.dictionary, db_record_=_record)

    def update(self, id_, payload: dict, **filters) -> _Domain:
        _record = self._repository.update(id_, payload, **filters)
        return _Domain(**_record.dictionary, db_record_=_record)

    def delete(self, id_):
        self._repository.delete(id_)
