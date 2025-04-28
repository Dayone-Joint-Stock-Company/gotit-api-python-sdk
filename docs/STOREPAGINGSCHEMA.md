# STOREPAGINGSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Number of page | [optional] 
**page_size** | **int** | Size of page | [optional] 
**total_page** | **int** | Total page | [optional] 

## Example

```python
from gotit_api_sdk_python.models.storepagingschema import STOREPAGINGSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of STOREPAGINGSCHEMA from a JSON string
storepagingschema_instance = STOREPAGINGSCHEMA.from_json(json)
# print the JSON string representation of the object
print(STOREPAGINGSCHEMA.to_json())

# convert the object into a dict
storepagingschema_dict = storepagingschema_instance.to_dict()
# create an instance of STOREPAGINGSCHEMA from a dict
storepagingschema_from_dict = STOREPAGINGSCHEMA.from_dict(storepagingschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


