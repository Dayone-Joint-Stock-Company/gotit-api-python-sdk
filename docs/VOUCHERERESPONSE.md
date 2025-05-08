# VOUCHERERESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERE]**](VOUCHERE.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchereresponse import VOUCHERERESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERERESPONSE from a JSON string
vouchereresponse_instance = VOUCHERERESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERERESPONSE.to_json())

# convert the object into a dict
vouchereresponse_dict = vouchereresponse_instance.to_dict()
# create an instance of VOUCHERERESPONSE from a dict
vouchereresponse_from_dict = VOUCHERERESPONSE.from_dict(vouchereresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


