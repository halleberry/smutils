from sqlalchemy import create_engine as _create_engine
from sqlalchemy.orm import sessionmaker as _sessionmaker


class UnitOfWork:
    """UnitOfWork ensures that every transaction(unit of work) is atomic, consistne, isolated and durable.


    (ACID) unit of work:
    --------------------
    - Atomic — The whole transaction either succeeds or fails;
    - Consistent — It conforms to the constraints of the database;
    - Isolated — It doesn’t interfere with other transactions;
    - Durable — It’s written to persistent storage.


    Use Example - Place an order transaction:

    >>> # in web.api.api:@api.[METHOD] function:
    ... # == 1. Enter a transaction which represents unit-Of-work.
    ... with UnitOfWork() as transaction:
    ...    # 2. get a repository instance by passing in transaction.session.
    ...    repo = Repository(transaction.session)
    ...    # 3. get a service instance by passing in the repository
    ...    service = Service(repo)
    ...    # 4. create a new record
    ...    record = {"id": 'someid'}
    ...    # 4. save the new record
    ...    service.save(record)
    ...    # 5. commit the transaction
    ...    transaction.commit()

    """

    def __init__(self):
        self.session_maker = _sessionmaker(bind=_create_engine('sqlite:///order.db'))

    def __enter__(self):
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
            self.session.close()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
