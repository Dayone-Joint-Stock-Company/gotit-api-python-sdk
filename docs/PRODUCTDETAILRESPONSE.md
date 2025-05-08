# PRODUCTDETAILRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[PRODUCTDETAIL]**](PRODUCTDETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productdetailresponse import PRODUCTDETAILRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTDETAILRESPONSE from a JSON string
productdetailresponse_instance = PRODUCTDETAILRESPONSE.from_json(json)
# print the JSON string representation of the object
print(PRODUCTDETAILRESPONSE.to_json())

# convert the object into a dict
productdetailresponse_dict = productdetailresponse_instance.to_dict()
# create an instance of PRODUCTDETAILRESPONSE from a dict
productdetailresponse_from_dict = PRODUCTDETAILRESPONSE.from_dict(productdetailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


