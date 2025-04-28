# PRODUCTV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id | [optional] 
**product_nm** | **str** | Product Name | [optional] 
**product_img** | **str** | Link product image | [optional] 
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**brand_service_guide** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**price** | [**PRODUCTPRICESCHEMA**](PRODUCTPRICESCHEMA.md) |  | [optional] 
**product_desc** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**store_list** | [**List[STOREPRODUCTSCHEMA]**](STOREPRODUCTSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.productv import PRODUCTV

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTV from a JSON string
productv_instance = PRODUCTV.from_json(json)
# print the JSON string representation of the object
print(PRODUCTV.to_json())

# convert the object into a dict
productv_dict = productv_instance.to_dict()
# create an instance of PRODUCTV from a dict
productv_from_dict = PRODUCTV.from_dict(productv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


