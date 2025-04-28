# gotit_api_sdk_python.VoucherStatusApi

All URIs are relative to *https://api-biz-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_voucher**](VoucherStatusApi.md#check_voucher) | **GET** /api/v4.0/vouchers/multiple/status/{refId} | Check voucher status


# **check_voucher**
> VOUCHERCHECKRESPONSE check_voucher(x_gi_authorization, ref_id, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)

Check voucher status

Check voucher status

### Example


```python
import gotit_api_sdk_python
from gotit_api_sdk_python.models.vouchercheckresponse import VOUCHERCHECKRESPONSE
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
    api_instance = gotit_api_sdk_python.VoucherStatusApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization
    ref_id = 'voucher_0711_102' # str | Transaction RefId
    is_exclude_store_list_info = true # bool | Exclude store list information (optional)
    store_list_page = 1 # int | Store Page (optional)
    store_list_page_size = 200 # int | Store Page Size (optional)

    try:
        # Check voucher status
        api_response = api_instance.check_voucher(x_gi_authorization, ref_id, is_exclude_store_list_info=is_exclude_store_list_info, store_list_page=store_list_page, store_list_page_size=store_list_page_size)
        print("The response of VoucherStatusApi->check_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherStatusApi->check_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gi_authorization** | **str**| Authorization | 
 **ref_id** | **str**| Transaction RefId | 
 **is_exclude_store_list_info** | **bool**| Exclude store list information | [optional] 
 **store_list_page** | **int**| Store Page | [optional] 
 **store_list_page_size** | **int**| Store Page Size | [optional] 

### Return type

[**VOUCHERCHECKRESPONSE**](VOUCHERCHECKRESPONSE.md)

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

