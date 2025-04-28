# STORESRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[STORESRESPONSEDataInner]**](STORESRESPONSEDataInner.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.storesresponse import STORESRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of STORESRESPONSE from a JSON string
storesresponse_instance = STORESRESPONSE.from_json(json)
# print the JSON string representation of the object
print(STORESRESPONSE.to_json())

# convert the object into a dict
storesresponse_dict = storesresponse_instance.to_dict()
# create an instance of STORESRESPONSE from a dict
storesresponse_from_dict = STORESRESPONSE.from_dict(storesresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


