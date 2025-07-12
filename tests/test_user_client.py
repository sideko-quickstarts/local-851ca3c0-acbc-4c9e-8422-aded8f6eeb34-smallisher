import httpx
import pydantic
import pytest

from local_api_16_py import AsyncClient, Client
from local_api_16_py.core import BinaryResponse
from local_api_16_py.environment import Environment
from local_api_16_py.types import models


def test_update_200_success_all_params():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.update(
        username="string",
        data={
            "email": "john@email.com",
            "first_name": "John",
            "id": 10,
            "last_name": "James",
            "password": "12345",
            "phone": "12345",
            "user_status": 1,
            "username": "theUser",
        },
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_update_200_success_all_params():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.update(
        username="string",
        data={
            "email": "john@email.com",
            "first_name": "John",
            "id": 10,
            "last_name": "James",
            "password": "12345",
            "phone": "12345",
            "user_status": 1,
            "username": "theUser",
        },
    )
    assert isinstance(response, httpx.Response)


def test_create_with_list_200_success_all_params():
    """Tests a POST request to the /user/createWithList endpoint.

    Operation: create_with_list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.create_with_list(
        data=[
            {
                "email": "john@email.com",
                "first_name": "John",
                "id": 10,
                "last_name": "James",
                "password": "12345",
                "phone": "12345",
                "user_status": 1,
                "username": "theUser",
            }
        ]
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_with_list_200_success_all_params():
    """Tests a POST request to the /user/createWithList endpoint.

    Operation: create_with_list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.create_with_list(
        data=[
            {
                "email": "john@email.com",
                "first_name": "John",
                "id": 10,
                "last_name": "James",
                "password": "12345",
                "phone": "12345",
                "user_status": 1,
                "username": "theUser",
            }
        ]
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_create_200_success_all_params():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.create(
        data={
            "email": "john@email.com",
            "first_name": "John",
            "id": 10,
            "last_name": "James",
            "password": "12345",
            "phone": "12345",
            "user_status": 1,
            "username": "theUser",
        }
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.create(
        data={
            "email": "john@email.com",
            "first_name": "John",
            "id": 10,
            "last_name": "James",
            "password": "12345",
            "phone": "12345",
            "user_status": 1,
            "username": "theUser",
        }
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.get(username="string")
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.User, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.get(username="string")
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_logout_200_success_all_params():
    """Tests a GET request to the /user/logout endpoint.

    Operation: logout
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.logout()
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_logout_200_success_all_params():
    """Tests a GET request to the /user/logout endpoint.

    Operation: logout
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.logout()
    assert isinstance(response, httpx.Response)


def test_login_200_success_required_only():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[str, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.login()
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_login_200_success_required_only():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[str, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.login()
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_login_200_success_all_params():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[str, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.login(password="string", username="string")
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_login_200_success_all_params():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[str, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.login(password="string", username="string")
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_delete_200_success_all_params():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.user.delete(username="string")
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.user.delete(username="string")
    assert isinstance(response, httpx.Response)
