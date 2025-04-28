# PRODUCTSALLDETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id | [optional] 
**product_nm** | **str** | Product Name | [optional] 
**product_img** | **str** | Link product image | [optional] 
**product_desc** | **str** | Product Description | [optional] 
**product_short_desc** | **str** | Product Short Description | [optional] 
**terms** | **str** | Terms of use | [optional] 
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**brand_logo** | **str** | Link to brand logo image | [optional] 
**brand_service_guide** | **str** | T&amp;C of brand | [optional] 
**category_id** | **int** | Category Id | [optional] 
**category_nm** | **str** | Category Name | [optional] 
**category_img** | **str** | Category Image | [optional] 
**product_type** | **str** | c (cash) hoặc i (item) | [optional] 
**prices** | [**List[PRODUCTPRICESCHEMA]**](PRODUCTPRICESCHEMA.md) |  | [optional] 
**link** | **str** |  | [optional] 
**store_list** | [**List[STOREPRODUCTSCHEMA]**](STOREPRODUCTSCHEMA.md) |  | [optional] 
**total_store** | **int** | Total store | [optional] 
**store_pagination** | [**PAGINGSCHEMA**](PAGINGSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.productsalldetail import PRODUCTSALLDETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTSALLDETAIL from a JSON string
productsalldetail_instance = PRODUCTSALLDETAIL.from_json(json)
# print the JSON string representation of the object
print(PRODUCTSALLDETAIL.to_json())

# convert the object into a dict
productsalldetail_dict = productsalldetail_instance.to_dict()
# create an instance of PRODUCTSALLDETAIL from a dict
productsalldetail_from_dict = PRODUCTSALLDETAIL.from_dict(productsalldetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


