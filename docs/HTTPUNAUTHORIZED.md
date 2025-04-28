# HTTPUNAUTHORIZED


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
from gotit_api_sdk_python.models.httpunauthorized import HTTPUNAUTHORIZED

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPUNAUTHORIZED from a JSON string
httpunauthorized_instance = HTTPUNAUTHORIZED.from_json(json)
# print the JSON string representation of the object
print(HTTPUNAUTHORIZED.to_json())

# convert the object into a dict
httpunauthorized_dict = httpunauthorized_instance.to_dict()
# create an instance of HTTPUNAUTHORIZED from a dict
httpunauthorized_from_dict = HTTPUNAUTHORIZED.from_dict(httpunauthorized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


