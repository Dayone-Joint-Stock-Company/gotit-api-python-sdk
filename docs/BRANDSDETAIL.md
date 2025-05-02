# BRANDSDETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**brand_logo** | **str** | Link to brand logo image | [optional] 
**slug** | **str** | Brand name used for URL | [optional] 
**short_desc** | **object** | Brand short description | [optional] 
**description** | **str** |  | [optional] 
**category_id** | **List[object]** | Array containing a list of Categories codes to which the Brand belongs | [optional] 
**order** | **int** | The serial number displays the brand | [optional] 
**service_guide** | **object** | Describe the brand&#39;s terms of reference (T&amp;C). HTML format | [optional] 
**stores** | [**List[STORESSCHEMA]**](STORESSCHEMA.md) |  | [optional] 
**usage_methods** | [**List[USAGEMETHODSCHEMA]**](USAGEMETHODSCHEMA.md) | Information on the brand&#39;s applicable channels | [optional] 

## Example

```python
from gotit_api_python_sdk.models.brandsdetail import BRANDSDETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDSDETAIL from a JSON string
brandsdetail_instance = BRANDSDETAIL.from_json(json)
# print the JSON string representation of the object
print(BRANDSDETAIL.to_json())

# convert the object into a dict
brandsdetail_dict = brandsdetail_instance.to_dict()
# create an instance of BRANDSDETAIL from a dict
brandsdetail_from_dict = BRANDSDETAIL.from_dict(brandsdetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


