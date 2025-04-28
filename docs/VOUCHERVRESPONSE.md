# VOUCHERVRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERV]**](VOUCHERV.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchervresponse import VOUCHERVRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERVRESPONSE from a JSON string
vouchervresponse_instance = VOUCHERVRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERVRESPONSE.to_json())

# convert the object into a dict
vouchervresponse_dict = vouchervresponse_instance.to_dict()
# create an instance of VOUCHERVRESPONSE from a dict
vouchervresponse_from_dict = VOUCHERVRESPONSE.from_dict(vouchervresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


