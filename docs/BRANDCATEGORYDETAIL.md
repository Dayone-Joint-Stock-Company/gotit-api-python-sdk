# BRANDCATEGORYDETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**brand_logo** | **str** | Link to brand logo image | [optional] 
**short_desc** | **str** | Brand short description | [optional] 
**description** | **str** | Brand description | [optional] 
**order** | **int** |  | [optional] 
**service_guide** | **str** | Describe the brand&#39;s terms of reference (T&amp;C). HTML format | [optional] 
**usage_methods** | [**List[USAGEMETHODSCHEMA]**](USAGEMETHODSCHEMA.md) | Information on the brand&#39;s applicable channels | [optional] 

## Example

```python
from gotit_api_python_sdk.models.brandcategorydetail import BRANDCATEGORYDETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDCATEGORYDETAIL from a JSON string
brandcategorydetail_instance = BRANDCATEGORYDETAIL.from_json(json)
# print the JSON string representation of the object
print(BRANDCATEGORYDETAIL.to_json())

# convert the object into a dict
brandcategorydetail_dict = brandcategorydetail_instance.to_dict()
# create an instance of BRANDCATEGORYDETAIL from a dict
brandcategorydetail_from_dict = BRANDCATEGORYDETAIL.from_dict(brandcategorydetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


