# VOUCHERCHECKZNSRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**VOUCHERCHECKZNSRESPONSEData**](VOUCHERCHECKZNSRESPONSEData.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchercheckznsresponse import VOUCHERCHECKZNSRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERCHECKZNSRESPONSE from a JSON string
vouchercheckznsresponse_instance = VOUCHERCHECKZNSRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERCHECKZNSRESPONSE.to_json())

# convert the object into a dict
vouchercheckznsresponse_dict = vouchercheckznsresponse_instance.to_dict()
# create an instance of VOUCHERCHECKZNSRESPONSE from a dict
vouchercheckznsresponse_from_dict = VOUCHERCHECKZNSRESPONSE.from_dict(vouchercheckznsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


