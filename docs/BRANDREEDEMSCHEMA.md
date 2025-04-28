# BRANDREEDEMSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **int** | Brand id | [optional] 
**brand_name** | **str** | Brand name | [optional] 
**brand_logo** | **str** | Link to brand logo image | [optional] 
**brand_name_slug** | **str** | Brand name slug | [optional] 
**brand_phone** | **str** | Brand Phone Number | [optional] 
**brand_address** | **str** | Address of brand | [optional] 
**brand_desc** | **str** | Brand Description | [optional] 
**brand_service_guide** | **str** | Describe the brand&#39;s terms of reference (T&amp;C). HTML format | [optional] 
**category_id** | **int** | Category Id | [optional] 
**category_nm** | **str** | Category Name | [optional] 
**category_img** | **str** | Category Image Logo | [optional] 

## Example

```python
from gotit_api_sdk_python.models.brandreedemschema import BRANDREEDEMSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDREEDEMSCHEMA from a JSON string
brandreedemschema_instance = BRANDREEDEMSCHEMA.from_json(json)
# print the JSON string representation of the object
print(BRANDREEDEMSCHEMA.to_json())

# convert the object into a dict
brandreedemschema_dict = brandreedemschema_instance.to_dict()
# create an instance of BRANDREEDEMSCHEMA from a dict
brandreedemschema_from_dict = BRANDREEDEMSCHEMA.from_dict(brandreedemschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


