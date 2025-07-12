import httpx
import typing

from local_api_16_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from local_api_16_py.types import models, params


class UserClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete user resource.

        This can only be done by the logged in user.

        DELETE /user/{username}

        Args:
            username: The name that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            User deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.delete(username="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/user/{username}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def login(
        self,
        *,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[str, BinaryResponse]:
        """
        Logs user into the system.

        Log into the system.

        GET /user/login

        Args:
            password: The password for login in clear text
            username: The user name for login
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.login()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(password, type_utils.NotGiven):
            encode_query_param(
                _query,
                "password",
                to_encodable(item=password, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/user/login",
            auth_names=["api_key"],
            query_params=_query,
            cast_to=typing.Union[str, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Logs out current logged in user session.

        Log user out of the system.

        GET /user/logout

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.logout()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/user/logout",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Get user by user name.

        Get user detail based on username.

        GET /user/{username}

        Args:
            username: The name that needs to be fetched. Use user1 for testing
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.get(username="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/user/{username}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.User], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Create user.

        This can only be done by the logged in user.

        POST /user

        Args:
            data: User
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.create()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerUser) if data else None
        )
        return self._base_client.request(
            method="POST",
            path="/user",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create_with_list(
        self,
        *,
        data: typing.Union[
            typing.Optional[typing.List[params.User]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Creates list of users with given input array.

        Creates list of users with given input array.

        POST /user/createWithList

        Args:
            data: typing.List[User]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.create_with_list()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=typing.List[params._SerializerUser])
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/user/createWithList",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        username: str,
        data: typing.Union[
            typing.Optional[params.User], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Update user resource.

        This can only be done by the logged in user.

        PUT /user/{username}

        Args:
            data: User
            username: name that need to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.update(username="string")
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerUser) if data else None
        )
        return self._base_client.request(
            method="PUT",
            path=f"/user/{username}",
            auth_names=["api_key"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncUserClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete user resource.

        This can only be done by the logged in user.

        DELETE /user/{username}

        Args:
            username: The name that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            User deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.delete(username="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/user/{username}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def login(
        self,
        *,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[str, BinaryResponse]:
        """
        Logs user into the system.

        Log into the system.

        GET /user/login

        Args:
            password: The password for login in clear text
            username: The user name for login
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.login()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(password, type_utils.NotGiven):
            encode_query_param(
                _query,
                "password",
                to_encodable(item=password, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/user/login",
            auth_names=["api_key"],
            query_params=_query,
            cast_to=typing.Union[str, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Logs out current logged in user session.

        Log user out of the system.

        GET /user/logout

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.logout()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/user/logout",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Get user by user name.

        Get user detail based on username.

        GET /user/{username}

        Args:
            username: The name that needs to be fetched. Use user1 for testing
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.get(username="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/user/{username}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.User], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Create user.

        This can only be done by the logged in user.

        POST /user

        Args:
            data: User
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.create()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerUser) if data else None
        )
        return await self._base_client.request(
            method="POST",
            path="/user",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create_with_list(
        self,
        *,
        data: typing.Union[
            typing.Optional[typing.List[params.User]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Creates list of users with given input array.

        Creates list of users with given input array.

        POST /user/createWithList

        Args:
            data: typing.List[User]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.create_with_list()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=typing.List[params._SerializerUser])
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/user/createWithList",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        username: str,
        data: typing.Union[
            typing.Optional[params.User], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Update user resource.

        This can only be done by the logged in user.

        PUT /user/{username}

        Args:
            data: User
            username: name that need to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.update(username="string")
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerUser) if data else None
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/user/{username}",
            auth_names=["api_key"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
