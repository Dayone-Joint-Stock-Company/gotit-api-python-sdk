# gotit_api_sdk_python.CategoriesApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_category_by_product**](CategoriesApi.md#get_category_by_product) | **GET** /api/v4.0/categories/categoriesByProducts | Get category by product
[**get_list_of_categories**](CategoriesApi.md#get_list_of_categories) | **GET** /api/v4.0/categories | Get lists category


# **get_category_by_product**
> CATEGORIESRESPONSE get_category_by_product(x_gi_authorization)

Get category by product

Returns all categories data master

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.categoriesresponse import CATEGORIESRESPONSE
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
    api_instance = gotit_api_sdk_python.CategoriesApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization

    try:
        # Get category by product
        api_response = api_instance.get_category_by_product(x_gi_authorization)
        print("The response of CategoriesApi->get_category_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_category_by_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 

### Return type

[**CATEGORIESRESPONSE**](CATEGORIESRESPONSE.md)

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

# **get_list_of_categories**
> CATEGORIESRESPONSE get_list_of_categories(x_gi_authorization)

Get lists category

Returns all categories data master

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.categoriesresponse import CATEGORIESRESPONSE
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
    api_instance = gotit_api_sdk_python.CategoriesApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization

    try:
        # Get lists category
        api_response = api_instance.get_list_of_categories(x_gi_authorization)
        print("The response of CategoriesApi->get_list_of_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_list_of_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 

### Return type

[**CATEGORIESRESPONSE**](CATEGORIESRESPONSE.md)

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

