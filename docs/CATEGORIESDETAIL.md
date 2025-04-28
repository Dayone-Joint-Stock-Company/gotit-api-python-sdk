# CATEGORIESDETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | Category Id | [optional] 
**category_nm** | **str** | Category Name | [optional] 
**category_img** | **str** | Category Image | [optional] 
**slug** | **str** | Category Slug | [optional] 
**order** | **int** | Category Short | [optional] 

## Example

```python
from gotit_api_sdk_python.models.categoriesdetail import CATEGORIESDETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of CATEGORIESDETAIL from a JSON string
categoriesdetail_instance = CATEGORIESDETAIL.from_json(json)
# print the JSON string representation of the object
print(CATEGORIESDETAIL.to_json())

# convert the object into a dict
categoriesdetail_dict = categoriesdetail_instance.to_dict()
# create an instance of CATEGORIESDETAIL from a dict
categoriesdetail_from_dict = CATEGORIESDETAIL.from_dict(categoriesdetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


