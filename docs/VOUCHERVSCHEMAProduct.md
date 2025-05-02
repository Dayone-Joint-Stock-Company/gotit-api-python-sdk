# VOUCHERVSCHEMAProduct


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
from gotit_api_python_sdk.models.vouchervschema_product import VOUCHERVSCHEMAProduct

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERVSCHEMAProduct from a JSON string
vouchervschema_product_instance = VOUCHERVSCHEMAProduct.from_json(json)
# print the JSON string representation of the object
print(VOUCHERVSCHEMAProduct.to_json())

# convert the object into a dict
vouchervschema_product_dict = vouchervschema_product_instance.to_dict()
# create an instance of VOUCHERVSCHEMAProduct from a dict
vouchervschema_product_from_dict = VOUCHERVSCHEMAProduct.from_dict(vouchervschema_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


