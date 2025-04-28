# HTTPNOTFOUND


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.httpnotfound import HTTPNOTFOUND

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPNOTFOUND from a JSON string
httpnotfound_instance = HTTPNOTFOUND.from_json(json)
# print the JSON string representation of the object
print(HTTPNOTFOUND.to_json())

# convert the object into a dict
httpnotfound_dict = httpnotfound_instance.to_dict()
# create an instance of HTTPNOTFOUND from a dict
httpnotfound_from_dict = HTTPNOTFOUND.from_dict(httpnotfound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


