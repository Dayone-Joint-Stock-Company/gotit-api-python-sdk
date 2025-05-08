# HTTPINTERNALSERVERERROR


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
from gotit_api_python_sdk.models.httpinternalservererror import HTTPINTERNALSERVERERROR

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPINTERNALSERVERERROR from a JSON string
httpinternalservererror_instance = HTTPINTERNALSERVERERROR.from_json(json)
# print the JSON string representation of the object
print(HTTPINTERNALSERVERERROR.to_json())

# convert the object into a dict
httpinternalservererror_dict = httpinternalservererror_instance.to_dict()
# create an instance of HTTPINTERNALSERVERERROR from a dict
httpinternalservererror_from_dict = HTTPINTERNALSERVERERROR.from_dict(httpinternalservererror_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


