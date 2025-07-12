from local_api_16_py.core import AsyncBaseClient, SyncBaseClient
from local_api_16_py.resources.store.inventory import (
    AsyncInventoryClient,
    InventoryClient,
)
from local_api_16_py.resources.store.order import AsyncOrderClient, OrderClient


class StoreClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.order = OrderClient(base_client=self._base_client)
        self.inventory = InventoryClient(base_client=self._base_client)


class AsyncStoreClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.order = AsyncOrderClient(base_client=self._base_client)
        self.inventory = AsyncInventoryClient(base_client=self._base_client)
