# REQUESTSENDVOUCHERBYZNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_no** | **str** |  | 
**receiver_nm** | **str** |  | [optional] 
**voucher_serials** | **List[str]** |  | 
**transaction_id** | **str** |  | 

## Example

```python
from gotit_api_sdk_python.models.requestsendvoucherbyzns import REQUESTSENDVOUCHERBYZNS

# TODO update the JSON string below
json = "{}"
# create an instance of REQUESTSENDVOUCHERBYZNS from a JSON string
requestsendvoucherbyzns_instance = REQUESTSENDVOUCHERBYZNS.from_json(json)
# print the JSON string representation of the object
print(REQUESTSENDVOUCHERBYZNS.to_json())

# convert the object into a dict
requestsendvoucherbyzns_dict = requestsendvoucherbyzns_instance.to_dict()
# create an instance of REQUESTSENDVOUCHERBYZNS from a dict
requestsendvoucherbyzns_from_dict = REQUESTSENDVOUCHERBYZNS.from_dict(requestsendvoucherbyzns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


