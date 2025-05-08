# gotit_api_python_sdk.BrandsApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brands_by_products**](BrandsApi.md#brands_by_products) | **GET** /api/v4.0/brands/brandsByProducts | Get brand by product
[**get_detail_of_brand**](BrandsApi.md#get_detail_of_brand) | **GET** /api/v4.0/brands/{id} | Get brand detail
[**get_list_of_brands**](BrandsApi.md#get_list_of_brands) | **GET** /api/v4.0/brands | Get list of brands


# **brands_by_products**
> BRANDDETAILRESPONSE brands_by_products(x_gi_authorization)

Get brand by product

Returns brand detail data master

### Example


```python
import gotit_api_python_sdk
from gotit_api_python_sdk.models.branddetailresponse import BRANDDETAILRESPONSE
from gotit_api_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_python_sdk.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_python_sdk.BrandsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization

    try:
        # Get brand by product
        api_response = api_instance.brands_by_products(x_gi_authorization)
        print("The response of BrandsApi->brands_by_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->brands_by_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 

### Return type

[**BRANDDETAILRESPONSE**](BRANDDETAILRESPONSE.md)

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

# **get_detail_of_brand**
> BRANDDETAILRESPONSE get_detail_of_brand(x_gi_authorization, id)

Get brand detail

Returns brand detail data master

### Example


```python
import gotit_api_python_sdk
from gotit_api_python_sdk.models.branddetailresponse import BRANDDETAILRESPONSE
from gotit_api_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_python_sdk.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_python_sdk.BrandsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    id = 46 # int | Brand Id

    try:
        # Get brand detail
        api_response = api_instance.get_detail_of_brand(x_gi_authorization, id)
        print("The response of BrandsApi->get_detail_of_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->get_detail_of_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **id** | **int**| Brand Id | 

### Return type

[**BRANDDETAILRESPONSE**](BRANDDETAILRESPONSE.md)

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

# **get_list_of_brands**
> BRANDSRESPONSE get_list_of_brands(x_gi_authorization)

Get list of brands

Retrieve a list of brands

### Example


```python
import gotit_api_python_sdk
from gotit_api_python_sdk.models.brandsresponse import BRANDSRESPONSE
from gotit_api_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_python_sdk.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with gotit_api_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_python_sdk.BrandsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization

    try:
        # Get list of brands
        api_response = api_instance.get_list_of_brands(x_gi_authorization)
        print("The response of BrandsApi->get_list_of_brands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->get_list_of_brands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 

### Return type

[**BRANDSRESPONSE**](BRANDSRESPONSE.md)

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

