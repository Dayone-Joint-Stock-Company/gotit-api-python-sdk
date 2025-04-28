# BRANDSRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[BRANDSDETAIL]**](BRANDSDETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.brandsresponse import BRANDSRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDSRESPONSE from a JSON string
brandsresponse_instance = BRANDSRESPONSE.from_json(json)
# print the JSON string representation of the object
print(BRANDSRESPONSE.to_json())

# convert the object into a dict
brandsresponse_dict = brandsresponse_instance.to_dict()
# create an instance of BRANDSRESPONSE from a dict
brandsresponse_from_dict = BRANDSRESPONSE.from_dict(brandsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


