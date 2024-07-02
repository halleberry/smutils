# orders API


1. Design and document the API.
2. Build the API client and the API server following the documentation.
3. Test both the API client and the API server against the documentation.


## Describe

    Coffee Orders.
    
    CoffeeMesh is a fictitious company that allows 
    customers to order all sorts of products derived from coffee, 
    including beverages and pastries.

    CoffeeMesh has one mission: 

        to make and deliver the best coffee in the world on demand to its customers, 
        no matter where they are or when they place their order. 

    The production factories owned by CoffeeMesh form a dense network, 
    a mesh of coffee production units that spans several countries. 
    
    Coffee production is fully automated, and 
    deliveries are carried out by an unmanned fleet of drones operating 24/7.
    
    When a customer places an order through the CoffeeMesh website,
    the ordered items are produced on demand.
    
    An algorithm determines `which factory` is the most suitable place to produce each item based on:
    - available `stock`,
    - the number of `pending orders` the factory is taking care of, and
    - `distance` to the customer.
    
    Once the items are `produced`, they’re immediately `dispatched` to the customer.
    
    It’s part of CoffeeMesh’s mission statement that
    the customer receives each item fresh and hot.


## Design

### __lifecycle__:

1. When the customer lands on the website, we show them the product catalogue. Each product is marked as available or unavailable. The customer can filter the list by availability and sort it by price (from lowest to highest and highest to lowest).

2. The customer selects products.

3. The customer pays for their order.

4. Once the customer has paid, we pass on the details of the order to the kitchen.

5. The kitchen picks up the order and produces it.

6. The customer monitors progress on their order.

7. Once the order is ready, we arrange its delivery.

8. The customer tracks the drone’s itinerary until their order is delivered.


### __subdomains__:

1. Products subdomain: When the customer lands on the website, we show a list of products with their availability.

2. Schedules subdomain: The customer places an order.

3. Payments subdomain: The customer pays for their order.

4. Schedules subdomain: Upon successful payment, we pass the order to the kitchen.

5. Kitchen subdomain: Kitchen picks up the order and starts production.

6. Schedules subdomain: The customer keeps track of the order’s progress.

7. Delivery subdomain: Once the order is produced, we arrange its delivery.

8. Schedules subdomain: The customer keeps track of the order’s itinerary.


### __states__:

- created
- progress
- cancelled
- dispatched 
- delivered 

### other
- order.products[beverage|pastry]
- place_order
- payment - progress | cancelled
- kitchen(in_stock, pending_orders, distance) - produced | cancelled
- delivery - dispatched | cancelled


## Document

Document API Specifications

__oas.json__

```json

{
  "openapi": "3.0.3",
  "info": {
    "title": "Orders Management API",
    "version": "1.0.0",
    "description": "This API provides endpoints for managing orders.\n"
  },
  "servers": [
    {
      "url": "http://127.0.0.1:8000",
      "description": "localhost"
    }
  ],
  "paths": {
    "/orders": {
      "get": {
        "operationId": "get",
        "summary": "Retrieve list",
        "parameters": [
          {
            "name": "cancelled",
            "in": "query",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved list",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Order"
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "operationId": "save",
        "summary": "Create ID",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrderInput"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          }
        }
      }
    },
    "/orders/{uid}": {
      "get": {
        "summary": "Retrieve ID",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          },
          "404": {
            "$ref": "#/components/responses/NotFound"
          }
        }
      },
      "put": {
        "summary": "Update ID",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrderInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          },
          "404": {
            "$ref": "#/components/responses/NotFound"
          }
        }
      },
      "delete": {
        "summary": "Delete ID",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Deleted ID"
          },
          "404": {
            "$ref": "#/components/responses/NotFound"
          }
        }
      }
    },
    "/orders/{uid}/pay": {
      "post": {
        "operationId": "pay",
        "summary": "Pay ID",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrderInput"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Paid ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          }
        }
      }
    },
    "/orders/{uid}/cancel": {
      "post": {
        "operationId": "cancel",
        "summary": "Cancel ID",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrderInput"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Cancelled ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "responses": {
      "NotFound": {
        "description": "ID was not found.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/Error"
            }
          }
        }
      }
    },
    "schemas": {
      "OrderItem": {
        "type": "object",
        "properties": {
          "product": {
            "type": "string"
          },
          "size": {
            "type": "string",
            "enum": [
              "small",
              "medium",
              "big"
            ]
          },
          "quantity": {
            "type": "integer",
            "default": 1,
            "minimum": 1
          }
        },
        "required": [
          "product",
          "size"
        ]
      },
      "OrderInput": {
        "type": "object",
        "properties": {
          "order": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OrderItem"
            }
          }
        },
        "required": [
          "order"
        ]
      },
      "Order": {
        "allOf": [
          {
            "$ref": "#/components/schemas/OrderInput"
          },
          {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "format": "uuid"
            },
            "created": {
              "type": "string",
              "format": "date-time"
            },
            "status": {
              "type": "string",
              "enum": [
                "created",
                "progress",
                "cancelled",
                "dispatched",
                "delivered"
              ]
            },
            "order": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/OrderItem"
              }
            }
          }
          }
          
        ],
        "required": [
          "order",
          "id",
          "created",
          "status"
        ]
      },
      "Error": {
        "type": "object",
        "properties": {
          "detail": {
            "type": "string"
          }
        },
        "required": [
          "detail"
        ]
      }
    },
    "securitySchemes": {
      "openIdConnect": {
        "type": "openIdConnect",
        "openIdConnectUrl": "https://gumazon-dev.eu.auth0.com/.well-known/openid-configuration"
      },
      "oauth2": {
        "type": "oauth2",
        "flows": {
          "clientCredentials": {
            "tokenUrl": "https://gumazon-dev.eu.auth0.com/oauth/token",
            "scopes": {}
          }
        }
      },
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  }
}

```


create a `specifications.json` file with setup-props with the setup.attrs is `oas` specs

```shell
#!/usr/bin/env sh

# from cwd, to create specifications.json, run:
python ~/smrepo/_main/specifications.py .


```


## Implement

### View <Schemas>


__orders/common__

```python


# file: orders/common/size.py

from enum import Enum

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


# file: orders/common/status.py

class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'


```


__orders/view__

```python

from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, conlist, conint, field_validator
from orders.common.size import Size as _Size
from orders.common.status import Status as _Status


# file: orders/view/order_item.py
class OrderItem(BaseModel):
    product: str 
    size: _Size
    # specify quantity’s minimum value, and we give it a default
    quantity: Optional[conint(ge=1, strict=True)] = 1
    
    @field_validator('quantity')
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value


# file: orders/view/order_input.py
class OrderInput(BaseModel):
    # use pydantic’s conlist type to define a list with at least one element.
    order:  conlist(OrderItem, min_length=1)


# file: orders/view/order.py
class Order(OrderInput):
    id: UUID
    created: datetime
    status: _Status


# file: orders/view/orders.py
class Orders(BaseModel):
    orders: List[Order]


```


### Controller <Endpoints>

```python

# orders/controller/order_controller.py


from datetime import datetime
from http import HTTPStatus
from typing import Optional
from starlette.responses import Response
from fastapi import HTTPException

from orders.view.order_input import OrderInput as SchemaInput
from orders.view.order import Order as Schema
from orders.view.orders import Orders as SchemaList


from ulid import ULID


def _get_uuid_from_ulid_from_dt(value: datetime):
    """Converts the given datetime into it's corresponding ulid formatted as uuid.

      :param value: <datetime.datetime>    like (2024-06-27 17:17:21.288000)
      :return: <uuid>        like (01905bfd-3d08-4308-84ea-bca979225185)
      """

    # Create a ULID from the given datetime
    _ulid = ULID.from_datetime(value)

    # Get the ULID formatted as UUID
    return _ulid.to_uuid4()


class OrderController:
    __resource = 'orders'

    def __init__(self):
        self._list = [
            {
                'id': 'f01905bfd-3d08-4308-84ea-bca979225185',
                'status': "delivered",
                'created': datetime.now(),
                'order': [
                    {
                        'product': 'cappuccino',
                        'size': 'medium',
                        'quantity': 1
                    }
                ]
            }
        ]

    # @api.get('/', response_model=_SchemaList)
    def get(self, cancelled: Optional[bool] = None, limit: Optional[int] = None) -> SchemaList:  # , tags: Optional[list[str]] = None):
        # If the parameters haven’t been set, we return immediately.
        if cancelled is None and limit is None:
            return SchemaList(orders=self._list)

        # If any of the parameters has been set, we filter list into a query_set.
        query_set = [_dic for _dic in self._list]

        # Check if cancelled is set.
        if cancelled is not None:
            if cancelled:
                query_set = [_d for _d in query_set if _d['status'] == 'cancelled']
            else:
                query_set = [_d for _d in query_set if _d['status'] != 'cancelled']

        # Check if limit is set and its value <= len(query_set), we return a subset query_set.
        if limit is not None and len(query_set) > limit:
            return SchemaList(orders=query_set[:limit])

        return SchemaList(orders=query_set)

    # @api.post('/', status_code=status.HTTP_201_CREATED, response_model=_Schema)
    def save(self, data: SchemaInput) -> Schema:
        _now = datetime.utcnow()
        dictionary = data.model_dump()
        dictionary['id'] = _get_uuid_from_ulid_from_dt(_now)
        dictionary['created'] = _now
        dictionary['status'] = 'created'
        # To create the order, we add it to the list.
        self._list.append(dictionary)
        return Schema(**dictionary)

    # @api.get('/{uid}', response_model=_Schema)
    def show(self, uid) -> Schema:
        for dictionary in self._list:
            if dictionary['id'] == uid:
                return Schema(**dictionary)
        raise HTTPException(status_code=404, detail=f'{self.__resource} with ID {uid} not found')

    # @api.put('/{uid}', response_model=_Schema)
    def update(self, uid, data: SchemaInput) -> Schema:
        for dictionary in self._list:
            if dictionary['id'] == uid:
                dictionary.update(data.model_dump())
                return Schema(**dictionary)
        raise HTTPException(status_code=404, detail=f'{self.__resource} with ID {uid} not found')

    # @api.delete('/{uid}', status_code=status.HTTP_204_NO_CONTENT)
    def delete(self, uid):
        for index, dictionary in enumerate(self._list):
            if dictionary['id'] == uid:
                # delete dictionary from the list using the list.pop() method.
                self._list.pop(index)

                # return an empty response.
                return Response(status_code=HTTPStatus.NO_CONTENT.value)

        raise HTTPException(status_code=404, detail=f'{self.__resource} with ID {uid} not found')

    # @api.post('/{uid}/cancel')
    def cancel(self, uid) -> Schema:
        for dictionary in self._list:
            if dictionary['id'] == uid:
                dictionary['status'] = 'cancelled'
                return Schema(**dictionary)
        raise HTTPException(
            status_code=404, detail=f'{self.__resource} with ID {uid} not found')

    # @api.post('/{uid}/pay')
    def pay(self, uid) -> Schema:
        for dictionary in self._list:
            if dictionary['id'] == uid:
                dictionary['status'] = 'progress'
                return Schema(**dictionary)
        raise HTTPException(
            status_code=404, detail=f'{self.__resource} with ID {uid} not found')


```


### REST API

__./web/api/api.py__

```python

# file: web/api/api.py

from typing import Optional

from fastapi import APIRouter
from starlette import status
from orders.controller.order_controller import OrderController as _Controller, SchemaInput as _SchemaInput, Schema as _Schema, SchemaList as _SchemaList


api = APIRouter(prefix='/orders', tags=['orders'])


@api.get('/', response_model=_SchemaList)
def get(cancelled: Optional[bool] = None, limit: Optional[int] = None):
    return _Controller().get(cancelled, limit)


@api.post('/', status_code=status.HTTP_201_CREATED, response_model=_Schema)
def save(data: _SchemaInput):
    return _Controller().save(data)


@api.get('/{uid}', response_model=_Schema)
def show(uid):
    return _Controller().show(uid)


@api.put('/{uid}', response_model=_Schema)
def update(uid, data: _SchemaInput):
    return _Controller().update(uid, data)


@api.delete('/{uid}', status_code=status.HTTP_204_NO_CONTENT)
def delete(uid):
    return _Controller().delete(uid)


@api.post('/{uid}/cancel')
def cancel(uid):
    return _Controller().cancel(uid)


@api.post('/{uid}/pay')
def pay(uid):
    return _Controller().pay(uid)


```

__./web/app.py__

```python
# file: orders/web/app.py

# Creating an instance of the FastAPI application


import json
import pathlib

from fastapi import FastAPI

from orders.web.api import api

oas_doc = json.loads(pathlib.Path.cwd().joinpath('oas.json').read_text())

app = FastAPI(debug=True)  # , openapi_url='/openapi/orders.json', docs_url='/docs/orders')

app.openapi = lambda: oas_doc

app.include_router(api.api)


```


### Run:

__run server__:

from the `orders` directory, run: `uvicorn orders.web.app:app --port 8000 --reload`


__run client__:

`curl http://127.0.0.1:8000`


## Service

### Repository

#### Database 

Setup DB with sqlalchemy and alembic, apply the models and create the schemas


- install requirements

```shell
#!/usr/bin/env sh

pipenv install sqlalchemy alembic

```


- create models

```python

# orders/repository/models.py

from typing import Optional
from datetime import datetime
from ulid import ULID
import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def _uuid_of_ulid_of_dt(value: datetime):
    # # Get a datetime object
    # _dt = datetime.now()
    # print(_dt)
    # Create a ULID from the given datetime object
    _ulid = ULID.from_datetime(value)

    # Get the ULID in UUID format
    return _ulid.to_uuid4()


def _dt_of_ulid_of_uuid(uuid_value: str):
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


def generate_uuid(value: Optional[datetime] = None):
    if value is None:
        value = datetime.now()

    # Create a ULID from the given datetime object
    _ulid = ULID.from_datetime(value)

    # Get the ULID in UUID format
    return _ulid.to_uuid4()


class OrderModel(Base):
    __tablename__ = '_LIST'
    id = Column(String, primary_key=True, default=generate_uuid)
    items = relationship('OrderItemModel', backref='_LIST')
    status = Column(String, nullable=False, default='created')
    created = Column(DateTime, default=datetime.utcnow)
    schedule_id = Column(String)
    delivery_id = Column(String)

    def dict(self):
        return {
            'id': self.id,
            'items': [item.dict() for item in self.items],
            'status': self.status,
            'created': self.created,
            'schedule_id': self.schedule_id,
            'delivery_id': self.delivery_id,
        }


class OrderItemModel(Base):
    __tablename__ = 'order_item'
    id = Column(String, primary_key=True, default=generate_uuid)
    order_id = Column(Integer, ForeignKey('_LIST.id'))
    product = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'product': self.product,
            'size': self.size,
            'quantity': self.quantity
        }


```


- init alembic to manage db migrations

```shell
#!/usr/bin/env sh 

# create:
#   {cwd}/migrations
#   {cwd}/migrations/env.py
#   {cwd}/migrations/versions/...*_migration.py files
#   {cwd}/alembic.ini
alembic init migrations

```


- Config db-url in alembic.ini

```alembic.ini

sqlalchemy.url = sqlite:///orders.db

```


- Config target_metadata of db-tables in migrations/env.py

```python

# migrations/env.py

from orders.repository.models import Base
target_metadata = Base.metadata


```


- Create the db's migration and schemas

```shell
#!/usr/bin/env sh 

echo 'create db migration: apply models to db in cwd <creates migrations/versions/*_migration.py>'
PYTHONPATH=`pwd` alembic revision --autogenerate -m "Initial migration"

echo 'create db schemas: apply the migrations and create the schemas for the db models, in cwd'
PYTHONPATH=`pwd` alembic upgrade heads

```


- Commit migrations and alembic.ini for replicating DB setup in new environments.

`git add . && git commit -m 'setup DB in the environment API.Service.Repository.Database'`

### Data-Access Repository

### Unit Of Work 

### Integrate service layer with the API layer


## Secure

## Test API

Testing and Validating APIs

## Build API distribution

dist/

Docherizing microservice APIs

## Deploy





