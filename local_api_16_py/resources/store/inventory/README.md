
### Returns pet inventories by status. <a name="list"></a>

Returns a map of status codes to quantities.

**API Endpoint**: `GET /store/inventory`

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.store.inventory.list()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.store.inventory.list()

```

#### Response

##### Type
[StoreInventoryListResponse](/local_api_16_py/types/models/store_inventory_list_response.py)

##### Example
`{}`
