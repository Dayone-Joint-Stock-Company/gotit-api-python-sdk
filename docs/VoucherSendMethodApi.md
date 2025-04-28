# gotit_api_sdk_python.VoucherSendMethodApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_status_zns**](VoucherSendMethodApi.md#check_status_zns) | **POST** /api/v4.0/vouchers/send/zns/check | Check status zns
[**send_voucher_by_email**](VoucherSendMethodApi.md#send_voucher_by_email) | **POST** /api/v4.0/vouchers/send/email | Send voucher by mail
[**send_voucher_by_sms**](VoucherSendMethodApi.md#send_voucher_by_sms) | **POST** /api/v4.0/vouchers/send/sms | Send voucher by sms
[**send_voucher_by_zns**](VoucherSendMethodApi.md#send_voucher_by_zns) | **POST** /api/v4.0/vouchers/send/zns | Send voucher by zns


# **check_status_zns**
> VOUCHERCHECKZNSRESPONSE check_status_zns(x_gi_authorization, requestcheckstatuszns=requestcheckstatuszns)

Check status zns

Check status zns

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestcheckstatuszns import REQUESTCHECKSTATUSZNS
from gotit_api_sdk_python.models.vouchercheckznsresponse import VOUCHERCHECKZNSRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherSendMethodApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestcheckstatuszns = gotit_api_sdk_python.REQUESTCHECKSTATUSZNS() # REQUESTCHECKSTATUSZNS |  (optional)

    try:
        # Check status zns
        api_response = api_instance.check_status_zns(x_gi_authorization, requestcheckstatuszns=requestcheckstatuszns)
        print("The response of VoucherSendMethodApi->check_status_zns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherSendMethodApi->check_status_zns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestcheckstatuszns** | [**REQUESTCHECKSTATUSZNS**](REQUESTCHECKSTATUSZNS.md)|  | [optional] 

### Return type

[**VOUCHERCHECKZNSRESPONSE**](VOUCHERCHECKZNSRESPONSE.md)

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

# **send_voucher_by_email**
> VOUCHERSENDEMAILRESPONSE send_voucher_by_email(x_gi_authorization, requestsendvoucherbyemail=requestsendvoucherbyemail)

Send voucher by mail

Send voucher by mail

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestsendvoucherbyemail import REQUESTSENDVOUCHERBYEMAIL
from gotit_api_sdk_python.models.vouchersendemailresponse import VOUCHERSENDEMAILRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherSendMethodApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestsendvoucherbyemail = gotit_api_sdk_python.REQUESTSENDVOUCHERBYEMAIL() # REQUESTSENDVOUCHERBYEMAIL |  (optional)

    try:
        # Send voucher by mail
        api_response = api_instance.send_voucher_by_email(x_gi_authorization, requestsendvoucherbyemail=requestsendvoucherbyemail)
        print("The response of VoucherSendMethodApi->send_voucher_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherSendMethodApi->send_voucher_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestsendvoucherbyemail** | [**REQUESTSENDVOUCHERBYEMAIL**](REQUESTSENDVOUCHERBYEMAIL.md)|  | [optional] 

### Return type

[**VOUCHERSENDEMAILRESPONSE**](VOUCHERSENDEMAILRESPONSE.md)

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

# **send_voucher_by_sms**
> VOUCHERSENDSMSRESPONSE send_voucher_by_sms(x_gi_authorization, requestsendvoucherbysms)

Send voucher by sms

Send voucher by sms

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestsendvoucherbysms import REQUESTSENDVOUCHERBYSMS
from gotit_api_sdk_python.models.vouchersendsmsresponse import VOUCHERSENDSMSRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherSendMethodApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestsendvoucherbysms = gotit_api_sdk_python.REQUESTSENDVOUCHERBYSMS() # REQUESTSENDVOUCHERBYSMS | 

    try:
        # Send voucher by sms
        api_response = api_instance.send_voucher_by_sms(x_gi_authorization, requestsendvoucherbysms)
        print("The response of VoucherSendMethodApi->send_voucher_by_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherSendMethodApi->send_voucher_by_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestsendvoucherbysms** | [**REQUESTSENDVOUCHERBYSMS**](REQUESTSENDVOUCHERBYSMS.md)|  | 

### Return type

[**VOUCHERSENDSMSRESPONSE**](VOUCHERSENDSMSRESPONSE.md)

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

# **send_voucher_by_zns**
> VOUCHERSENDZNSRESPONSE send_voucher_by_zns(x_gi_authorization, requestsendvoucherbyzns=requestsendvoucherbyzns)

Send voucher by zns

Send voucher by zns

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.requestsendvoucherbyzns import REQUESTSENDVOUCHERBYZNS
from gotit_api_sdk_python.models.vouchersendznsresponse import VOUCHERSENDZNSRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherSendMethodApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    requestsendvoucherbyzns = gotit_api_sdk_python.REQUESTSENDVOUCHERBYZNS() # REQUESTSENDVOUCHERBYZNS |  (optional)

    try:
        # Send voucher by zns
        api_response = api_instance.send_voucher_by_zns(x_gi_authorization, requestsendvoucherbyzns=requestsendvoucherbyzns)
        print("The response of VoucherSendMethodApi->send_voucher_by_zns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherSendMethodApi->send_voucher_by_zns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **requestsendvoucherbyzns** | [**REQUESTSENDVOUCHERBYZNS**](REQUESTSENDVOUCHERBYZNS.md)|  | [optional] 

### Return type

[**VOUCHERSENDZNSRESPONSE**](VOUCHERSENDZNSRESPONSE.md)

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

