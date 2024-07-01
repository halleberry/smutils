from datetime import datetime
from ulid import ULID
import uuid


def get_uuid_from_ulid_from_dt(value: datetime):
  """Converts the given datetime into it's corresponding ulid formatted as uuid.

    :param value: <datetime.datetime>    like (2024-06-27 17:17:21.288000) 
    :return: <uuid>        like (01905bfd-3d08-4308-84ea-bca979225185)
    """
  
    # Create a ULID from the given datetime
    _ulid = ULID.from_datetime(value)

    # Get the ULID formatted as UUID
    return _ulid.to_uuid4()


def get_dt_from_ulid_from_uuid(uuid_value: str):
    """Converts the given UUID str into it's corresponding datetime and returns it.

    :param uuid_value: <str>        like (01905bfd-3d08-4308-84ea-bca979225185)
    :return: <datetime.datetime>    like (2024-06-27 17:17:21.288000)
    """
  
    # Get the UUID object corresponding to the given UUID str value
    uuid_obj = uuid.UUID(uuid_value)

    # Get the ULID obj corresponding to the given UUID obj
    ulid_obj = ULID.from_uuid(uuid_obj)

    # Get the dt corresponding to the of the ULID obj.
    return datetime.fromtimestamp(ulid_obj.timestamp)

