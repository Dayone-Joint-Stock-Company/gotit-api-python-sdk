# VOUCHERSENDZNSRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**VOUCHERSENDZNSRESPONSEData**](VOUCHERSENDZNSRESPONSEData.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchersendznsresponse import VOUCHERSENDZNSRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERSENDZNSRESPONSE from a JSON string
vouchersendznsresponse_instance = VOUCHERSENDZNSRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERSENDZNSRESPONSE.to_json())

# convert the object into a dict
vouchersendznsresponse_dict = vouchersendznsresponse_instance.to_dict()
# create an instance of VOUCHERSENDZNSRESPONSE from a dict
vouchersendznsresponse_from_dict = VOUCHERSENDZNSRESPONSE.from_dict(vouchersendznsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


