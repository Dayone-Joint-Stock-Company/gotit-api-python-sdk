# HTTPBADREQUEST


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
from gotit_api_sdk_python.models.httpbadrequest import HTTPBADREQUEST

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPBADREQUEST from a JSON string
httpbadrequest_instance = HTTPBADREQUEST.from_json(json)
# print the JSON string representation of the object
print(HTTPBADREQUEST.to_json())

# convert the object into a dict
httpbadrequest_dict = httpbadrequest_instance.to_dict()
# create an instance of HTTPBADREQUEST from a dict
httpbadrequest_from_dict = HTTPBADREQUEST.from_dict(httpbadrequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


