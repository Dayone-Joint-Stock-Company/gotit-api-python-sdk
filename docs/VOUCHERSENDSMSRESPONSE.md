# VOUCHERSENDSMSRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERSENDSMSSCHEMA]**](VOUCHERSENDSMSSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchersendsmsresponse import VOUCHERSENDSMSRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERSENDSMSRESPONSE from a JSON string
vouchersendsmsresponse_instance = VOUCHERSENDSMSRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERSENDSMSRESPONSE.to_json())

# convert the object into a dict
vouchersendsmsresponse_dict = vouchersendsmsresponse_instance.to_dict()
# create an instance of VOUCHERSENDSMSRESPONSE from a dict
vouchersendsmsresponse_from_dict = VOUCHERSENDSMSRESPONSE.from_dict(vouchersendsmsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


