# PRODUCTSRESPONSEDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_list** | [**List[PRODUCTSALLDETAIL]**](PRODUCTSALLDETAIL.md) |  | [optional] 
**pagination** | [**PAGINGSCHEMA**](PAGINGSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productsresponse_data_inner import PRODUCTSRESPONSEDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTSRESPONSEDataInner from a JSON string
productsresponse_data_inner_instance = PRODUCTSRESPONSEDataInner.from_json(json)
# print the JSON string representation of the object
print(PRODUCTSRESPONSEDataInner.to_json())

# convert the object into a dict
productsresponse_data_inner_dict = productsresponse_data_inner_instance.to_dict()
# create an instance of PRODUCTSRESPONSEDataInner from a dict
productsresponse_data_inner_from_dict = PRODUCTSRESPONSEDataInner.from_dict(productsresponse_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


