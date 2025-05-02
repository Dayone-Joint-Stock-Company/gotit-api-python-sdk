# PRODUCTPRICESCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_id** | **int** | Product id/size code | [optional] 
**price_nm** | **str** | Product name/size name | [optional] 
**price_value** | **int** | Product value | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productpriceschema import PRODUCTPRICESCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTPRICESCHEMA from a JSON string
productpriceschema_instance = PRODUCTPRICESCHEMA.from_json(json)
# print the JSON string representation of the object
print(PRODUCTPRICESCHEMA.to_json())

# convert the object into a dict
productpriceschema_dict = productpriceschema_instance.to_dict()
# create an instance of PRODUCTPRICESCHEMA from a dict
productpriceschema_from_dict = PRODUCTPRICESCHEMA.from_dict(productpriceschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


