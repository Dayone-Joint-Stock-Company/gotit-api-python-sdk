# VOUCHERSENDEMAILRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERSENDEMAILSCHEMA]**](VOUCHERSENDEMAILSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchersendemailresponse import VOUCHERSENDEMAILRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERSENDEMAILRESPONSE from a JSON string
vouchersendemailresponse_instance = VOUCHERSENDEMAILRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERSENDEMAILRESPONSE.to_json())

# convert the object into a dict
vouchersendemailresponse_dict = vouchersendemailresponse_instance.to_dict()
# create an instance of VOUCHERSENDEMAILRESPONSE from a dict
vouchersendemailresponse_from_dict = VOUCHERSENDEMAILRESPONSE.from_dict(vouchersendemailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


