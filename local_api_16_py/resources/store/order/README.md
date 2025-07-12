
### Delete purchase order by identifier. <a name="delete"></a>

For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

**API Endpoint**: `DELETE /store/order/{orderId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `orderId` | ✓ | ID of the order that needs to be deleted | `123` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.store.order.delete(order_id=123)

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.store.order.delete(order_id=123)

```

### Find purchase order by ID. <a name="get"></a>

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

**API Endpoint**: `GET /store/order/{orderId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `orderId` | ✓ | ID of order that needs to be fetched | `123` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.store.order.get(order_id=123)

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.store.order.get(order_id=123)

```

### Place an order for a pet. <a name="create"></a>

Place a new order in the store.

**API Endpoint**: `POST /store/order`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✗ |  | `{"id": 10, "pet_id": 198772, "quantity": 7, "status": "approved"}` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.store.order.create()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.store.order.create()

```

#### Response

##### Type
[Order](/local_api_16_py/types/models/order.py)

##### Example
`{"id": 10, "pet_id": 198772, "quantity": 7, "status": "approved"}`
