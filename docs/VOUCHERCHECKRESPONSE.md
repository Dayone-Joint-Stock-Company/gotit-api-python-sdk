# VOUCHERCHECKRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[VOUCHERCHECKSCHEMA]**](VOUCHERCHECKSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchercheckresponse import VOUCHERCHECKRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERCHECKRESPONSE from a JSON string
vouchercheckresponse_instance = VOUCHERCHECKRESPONSE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERCHECKRESPONSE.to_json())

# convert the object into a dict
vouchercheckresponse_dict = vouchercheckresponse_instance.to_dict()
# create an instance of VOUCHERCHECKRESPONSE from a dict
vouchercheckresponse_from_dict = VOUCHERCHECKRESPONSE.from_dict(vouchercheckresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


