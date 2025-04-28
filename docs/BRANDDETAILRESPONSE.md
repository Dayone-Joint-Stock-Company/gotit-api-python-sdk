# BRANDDETAILRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[BRANDDETAIL]**](BRANDDETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.branddetailresponse import BRANDDETAILRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDDETAILRESPONSE from a JSON string
branddetailresponse_instance = BRANDDETAILRESPONSE.from_json(json)
# print the JSON string representation of the object
print(BRANDDETAILRESPONSE.to_json())

# convert the object into a dict
branddetailresponse_dict = branddetailresponse_instance.to_dict()
# create an instance of BRANDDETAILRESPONSE from a dict
branddetailresponse_from_dict = BRANDDETAILRESPONSE.from_dict(branddetailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


