# PRODUCTVENDORLINKG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id. You can see the Products section for the product id. Note: productId type auto convert merchant code does not support creating cover links. | 
**product_price_id** | **int** | Product price id. Each product will have 1 or more denomination codes corresponding to the value or converted product size. | 
**quantity** | **int** | Number of vouchers to be issued | 

## Example

```python
from gotit_api_python_sdk.models.productvendorlinkg import PRODUCTVENDORLINKG

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTVENDORLINKG from a JSON string
productvendorlinkg_instance = PRODUCTVENDORLINKG.from_json(json)
# print the JSON string representation of the object
print(PRODUCTVENDORLINKG.to_json())

# convert the object into a dict
productvendorlinkg_dict = productvendorlinkg_instance.to_dict()
# create an instance of PRODUCTVENDORLINKG from a dict
productvendorlinkg_from_dict = PRODUCTVENDORLINKG.from_dict(productvendorlinkg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


