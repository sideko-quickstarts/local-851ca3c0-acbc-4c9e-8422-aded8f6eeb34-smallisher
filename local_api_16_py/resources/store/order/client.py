import httpx
import typing

from local_api_16_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from local_api_16_py.types import models, params


class OrderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete purchase order by identifier.

        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        DELETE /store/order/{orderId}

        Args:
            orderId: ID of the order that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            order deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.delete(order_id=123)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Order, BinaryResponse]:
        """
        Find purchase order by ID.

        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        GET /store/order/{orderId}

        Args:
            orderId: ID of order that needs to be fetched
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.get(order_id=123)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Order, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.Order], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Order:
        """
        Place an order for a pet.

        Place a new order in the store.

        POST /store/order

        Args:
            data: Order
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.create()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerOrder) if data else None
        )
        return self._base_client.request(
            method="POST",
            path="/store/order",
            auth_names=["api_key"],
            json=_json,
            cast_to=models.Order,
            request_options=request_options or default_request_options(),
        )


class AsyncOrderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete purchase order by identifier.

        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        DELETE /store/order/{orderId}

        Args:
            orderId: ID of the order that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            order deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.delete(order_id=123)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Order, BinaryResponse]:
        """
        Find purchase order by ID.

        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        GET /store/order/{orderId}

        Args:
            orderId: ID of order that needs to be fetched
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.get(order_id=123)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Order, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.Order], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Order:
        """
        Place an order for a pet.

        Place a new order in the store.

        POST /store/order

        Args:
            data: Order
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.create()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerOrder) if data else None
        )
        return await self._base_client.request(
            method="POST",
            path="/store/order",
            auth_names=["api_key"],
            json=_json,
            cast_to=models.Order,
            request_options=request_options or default_request_options(),
        )
