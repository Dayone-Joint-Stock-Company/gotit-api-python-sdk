# PRODUCTDEFAULTLINKG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id. You can see the Products section for the product id. Note: productId type auto convert merchant code does not support creating cover links. | 
**product_price_id** | **int** | Product price id. Each product will have 1 or more denomination codes corresponding to the value or converted product size. | 
**quantity** | **int** | Number of vouchers to be issued | 

## Example

```python
from gotit_api_python_sdk.models.productdefaultlinkg import PRODUCTDEFAULTLINKG

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTDEFAULTLINKG from a JSON string
productdefaultlinkg_instance = PRODUCTDEFAULTLINKG.from_json(json)
# print the JSON string representation of the object
print(PRODUCTDEFAULTLINKG.to_json())

# convert the object into a dict
productdefaultlinkg_dict = productdefaultlinkg_instance.to_dict()
# create an instance of PRODUCTDEFAULTLINKG from a dict
productdefaultlinkg_from_dict = PRODUCTDEFAULTLINKG.from_dict(productdefaultlinkg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


