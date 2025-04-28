# gotit_api_sdk_python.ProductsApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_of_products**](ProductsApi.md#get_list_of_products) | **GET** /api/v4.0/products | Get all products master data
[**get_product_detail**](ProductsApi.md#get_product_detail) | **GET** /api/v4.0/products/{id} | Get product detail data
[**get_stores_of_product**](ProductsApi.md#get_stores_of_product) | **GET** /api/v4.0/products/{id}/stores | Get stores of this product


# **get_list_of_products**
> PRODUCTSRESPONSE get_list_of_products(x_gi_authorization, page, page_size, min_price=min_price, max_price=max_price, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)

Get all products master data

Returns all products master data

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.productsresponse import PRODUCTSRESPONSE
from gotit_api_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_sdk_python.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_sdk_python.ProductsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    page = 1 # int | Page
    page_size = 200 # int | Page Size
    min_price = 1000 # int | Min price (optional)
    max_price = 10000000 # int | Max price (optional)
    is_exclude_store_list_info = true # bool | Stores (optional)
    store_list_page = 1 # int | Store Page (optional)
    store_list_page_size = 200 # int | Store Page Size (optional)

    try:
        # Get all products master data
        api_response = api_instance.get_list_of_products(x_gi_authorization, page, page_size, min_price=min_price, max_price=max_price, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)
        print("The response of ProductsApi->get_list_of_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_list_of_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **page** | **int**| Page | 
 **page_size** | **int**| Page Size | 
 **min_price** | **int**| Min price | [optional] 
 **max_price** | **int**| Max price | [optional] 
 **is_exclude_store_list_info** | **bool**| Stores | [optional] 
 **store_list_page** | **int**| Store Page | [optional] 
 **store_list_page_size** | **int**| Store Page Size | [optional] 

### Return type

[**PRODUCTSRESPONSE**](PRODUCTSRESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**404** | Request not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_detail**
> PRODUCTDETAILRESPONSE get_product_detail(x_gi_authorization, id, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)

Get product detail data

Returns product detail data

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.productdetailresponse import PRODUCTDETAILRESPONSE
from gotit_api_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_sdk_python.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_sdk_python.ProductsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    id = 1541 # int | Product ID
    is_exclude_store_list_info = true # bool | Exclude store list information (optional)
    store_list_page = 1 # int | Store Page (optional)
    store_list_page_size = 200 # int | Store Page Size (optional)

    try:
        # Get product detail data
        api_response = api_instance.get_product_detail(x_gi_authorization, id, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)
        print("The response of ProductsApi->get_product_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **id** | **int**| Product ID | 
 **is_exclude_store_list_info** | **bool**| Exclude store list information | [optional] 
 **store_list_page** | **int**| Store Page | [optional] 
 **store_list_page_size** | **int**| Store Page Size | [optional] 

### Return type

[**PRODUCTDETAILRESPONSE**](PRODUCTDETAILRESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**404** | Request not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stores_of_product**
> STORESRESPONSE get_stores_of_product(x_gi_authorization, id)

Get stores of this product

Returns all stores of this product

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.storesresponse import STORESRESPONSE
from gotit_api_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_sdk_python.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_sdk_python.ProductsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    id = 1541 # int | Product ID

    try:
        # Get stores of this product
        api_response = api_instance.get_stores_of_product(x_gi_authorization, id)
        print("The response of ProductsApi->get_stores_of_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_stores_of_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **id** | **int**| Product ID | 

### Return type

[**STORESRESPONSE**](STORESRESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**404** | Request not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

