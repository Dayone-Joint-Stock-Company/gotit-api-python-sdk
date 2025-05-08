# PRODUCTDETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id | [optional] 
**product_nm** | **str** | Product Name | [optional] 
**product_img** | **str** | Link product image | [optional] 
**product_sub_img** | **List[object]** | Array of link image | [optional] 
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**product_type** | **str** | c (cash) hoặc i (item) | [optional] 
**brand_name_slug** | **str** | Slug of brand | [optional] 
**brand_phone** | **str** | Phone of brand | [optional] 
**brand_address** | **str** | Address of brand | [optional] 
**brand_desc** | **str** | Description of brand | [optional] 
**brand_service_guide** | **str** | T&amp;C of brand | [optional] 
**service_guide** | **str** | T&amp;C of product | [optional] 
**brand_logo** | **str** | Link to brand logo image | [optional] 
**link** | **str** |  | [optional] 
**prices** | [**List[PRODUCTPRICESCHEMA]**](PRODUCTPRICESCHEMA.md) |  | [optional] 
**name_slug** | **str** | Slug of product | [optional] 
**product_desc** | **str** | Product Description | [optional] 
**product_short_desc** | **str** | Product Short Description | [optional] 
**terms** | **str** | Terms of use | [optional] 
**category_id** | **int** | Category Id | [optional] 
**category_nm** | **str** | Category Name | [optional] 
**category_img** | **str** | Category Image | [optional] 
**brand_redeem** | [**List[BRANDREEDEMSCHEMA]**](BRANDREEDEMSCHEMA.md) |  | [optional] 
**store_list** | [**List[STORESSCHEMA]**](STORESSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productdetail import PRODUCTDETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTDETAIL from a JSON string
productdetail_instance = PRODUCTDETAIL.from_json(json)
# print the JSON string representation of the object
print(PRODUCTDETAIL.to_json())

# convert the object into a dict
productdetail_dict = productdetail_instance.to_dict()
# create an instance of PRODUCTDETAIL from a dict
productdetail_from_dict = PRODUCTDETAIL.from_dict(productdetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


