
### Delete user resource. <a name="delete"></a>

This can only be done by the logged in user.

**API Endpoint**: `DELETE /user/{username}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `username` | ✓ | The name that needs to be deleted | `"string"` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.delete(username="string")

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.delete(username="string")

```

### Logs user into the system. <a name="login"></a>

Log into the system.

**API Endpoint**: `GET /user/login`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `password` | ✗ | The password for login in clear text | `"string"` |
| `username` | ✗ | The user name for login | `"string"` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.login()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.login()

```

### Logs out current logged in user session. <a name="logout"></a>

Log user out of the system.

**API Endpoint**: `GET /user/logout`

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.logout()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.logout()

```

### Get user by user name. <a name="get"></a>

Get user detail based on username.

**API Endpoint**: `GET /user/{username}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `username` | ✓ | The name that needs to be fetched. Use user1 for testing | `"string"` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.get(username="string")

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.get(username="string")

```

### Create user. <a name="create"></a>

This can only be done by the logged in user.

**API Endpoint**: `POST /user`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✗ |  | `{"email": "john@email.com", "first_name": "John", "id": 10, "last_name": "James", "password": "12345", "phone": "12345", "user_status": 1, "username": "theUser"}` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.create()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.create()

```

### Creates list of users with given input array. <a name="create_with_list"></a>

Creates list of users with given input array.

**API Endpoint**: `POST /user/createWithList`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✗ |  | `[{"email": "john@email.com", "first_name": "John", "id": 10, "last_name": "James", "password": "12345", "phone": "12345", "user_status": 1, "username": "theUser"}]` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.create_with_list()

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.create_with_list()

```

### Update user resource. <a name="update"></a>

This can only be done by the logged in user.

**API Endpoint**: `PUT /user/{username}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `username` | ✓ | name that need to be deleted | `"string"` |
| `data` | ✗ |  | `{"email": "john@email.com", "first_name": "John", "id": 10, "last_name": "James", "password": "12345", "phone": "12345", "user_status": 1, "username": "theUser"}` |

#### Synchronous Client

```python
from local_api_16_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.user.update(username="string")

```

#### Asynchronous Client

```python
from local_api_16_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.user.update(username="string")

```
