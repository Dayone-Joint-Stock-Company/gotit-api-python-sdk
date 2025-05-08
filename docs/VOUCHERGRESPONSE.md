# VOUCHERGRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERGSCHEMA]**](VOUCHERGSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchergresponse import VOUCHERGRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERGRESPONSE from a JSON string
vouchergresponse_instance = VOUCHERGRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERGRESPONSE.to_json())

# convert the object into a dict
vouchergresponse_dict = vouchergresponse_instance.to_dict()
# create an instance of VOUCHERGRESPONSE from a dict
vouchergresponse_from_dict = VOUCHERGRESPONSE.from_dict(vouchergresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


