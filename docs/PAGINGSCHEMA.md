# PAGINGSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | page size | [optional] 
**page** | **int** | page | [optional] 
**total_page** | **int** | total page | [optional] 

## Example

```python
from gotit_api_sdk_python.models.pagingschema import PAGINGSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of PAGINGSCHEMA from a JSON string
pagingschema_instance = PAGINGSCHEMA.from_json(json)
# print the JSON string representation of the object
print(PAGINGSCHEMA.to_json())

# convert the object into a dict
pagingschema_dict = pagingschema_instance.to_dict()
# create an instance of PAGINGSCHEMA from a dict
pagingschema_from_dict = PAGINGSCHEMA.from_dict(pagingschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


