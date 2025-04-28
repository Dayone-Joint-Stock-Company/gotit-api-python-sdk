# gotit_api_sdk_python.VoucherApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_voucher_link_e**](VoucherApi.md#create_voucher_link_e) | **POST** /api/v4.0/vouchers/e | Create voucher link e
[**create_voucher_link_g**](VoucherApi.md#create_voucher_link_g) | **POST** /api/v4.0/vouchers/g | Create voucher link g
[**create_voucher_link_v**](VoucherApi.md#create_voucher_link_v) | **POST** /api/v4.0/vouchers/v | Create voucher link v


# **create_voucher_link_e**
> VOUCHERERESPONSE create_voucher_link_e(x_gi_authorization, requestcreatevoucherlinke=requestcreatevoucherlinke)

Create voucher link e

Create voucher link e

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestcreatevoucherlinke import REQUESTCREATEVOUCHERLINKE
from gotit_api_sdk_python.models.vouchereresponse import VOUCHERERESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestcreatevoucherlinke = gotit_api_sdk_python.REQUESTCREATEVOUCHERLINKE() # REQUESTCREATEVOUCHERLINKE |  (optional)

    try:
        # Create voucher link e
        api_response = api_instance.create_voucher_link_e(x_gi_authorization, requestcreatevoucherlinke=requestcreatevoucherlinke)
        print("The response of VoucherApi->create_voucher_link_e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->create_voucher_link_e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestcreatevoucherlinke** | [**REQUESTCREATEVOUCHERLINKE**](REQUESTCREATEVOUCHERLINKE.md)|  | [optional] 

### Return type

[**VOUCHERERESPONSE**](VOUCHERERESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_voucher_link_g**
> VOUCHERGRESPONSE create_voucher_link_g(x_gi_authorization, requestcreatevoucherlinkg=requestcreatevoucherlinkg)

Create voucher link g

Create voucher link g

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestcreatevoucherlinkg import REQUESTCREATEVOUCHERLINKG
from gotit_api_sdk_python.models.vouchergresponse import VOUCHERGRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestcreatevoucherlinkg = gotit_api_sdk_python.REQUESTCREATEVOUCHERLINKG() # REQUESTCREATEVOUCHERLINKG |  (optional)

    try:
        # Create voucher link g
        api_response = api_instance.create_voucher_link_g(x_gi_authorization, requestcreatevoucherlinkg=requestcreatevoucherlinkg)
        print("The response of VoucherApi->create_voucher_link_g:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->create_voucher_link_g: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestcreatevoucherlinkg** | [**REQUESTCREATEVOUCHERLINKG**](REQUESTCREATEVOUCHERLINKG.md)|  | [optional] 

### Return type

[**VOUCHERGRESPONSE**](VOUCHERGRESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_voucher_link_v**
> VOUCHERVRESPONSE create_voucher_link_v(x_gi_authorization, requestcreatevoucherlinkv=requestcreatevoucherlinkv)

Create voucher link v

Create voucher link v

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestcreatevoucherlinkv import REQUESTCREATEVOUCHERLINKV
from gotit_api_sdk_python.models.vouchervresponse import VOUCHERVRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestcreatevoucherlinkv = gotit_api_sdk_python.REQUESTCREATEVOUCHERLINKV() # REQUESTCREATEVOUCHERLINKV |  (optional)

    try:
        # Create voucher link v
        api_response = api_instance.create_voucher_link_v(x_gi_authorization, requestcreatevoucherlinkv=requestcreatevoucherlinkv)
        print("The response of VoucherApi->create_voucher_link_v:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->create_voucher_link_v: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestcreatevoucherlinkv** | [**REQUESTCREATEVOUCHERLINKV**](REQUESTCREATEVOUCHERLINKV.md)|  | [optional] 

### Return type

[**VOUCHERVRESPONSE**](VOUCHERVRESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

