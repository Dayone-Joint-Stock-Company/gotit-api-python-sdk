# BRANDCATEGORYDETAILRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[BRANDCATEGORYDETAIL]**](BRANDCATEGORYDETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.brandcategorydetailresponse import BRANDCATEGORYDETAILRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of BRANDCATEGORYDETAILRESPONSE from a JSON string
brandcategorydetailresponse_instance = BRANDCATEGORYDETAILRESPONSE.from_json(json)
# print the JSON string representation of the object
print(BRANDCATEGORYDETAILRESPONSE.to_json())

# convert the object into a dict
brandcategorydetailresponse_dict = brandcategorydetailresponse_instance.to_dict()
# create an instance of BRANDCATEGORYDETAILRESPONSE from a dict
brandcategorydetailresponse_from_dict = BRANDCATEGORYDETAILRESPONSE.from_dict(brandcategorydetailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


