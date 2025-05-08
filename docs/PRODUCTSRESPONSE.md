# PRODUCTSRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[PRODUCTSRESPONSEDataInner]**](PRODUCTSRESPONSEDataInner.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productsresponse import PRODUCTSRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTSRESPONSE from a JSON string
productsresponse_instance = PRODUCTSRESPONSE.from_json(json)
# print the JSON string representation of the object
print(PRODUCTSRESPONSE.to_json())

# convert the object into a dict
productsresponse_dict = productsresponse_instance.to_dict()
# create an instance of PRODUCTSRESPONSE from a dict
productsresponse_from_dict = PRODUCTSRESPONSE.from_dict(productsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


