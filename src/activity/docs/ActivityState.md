# ActivityState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **list[str]** | State pair tuple (CurrentState, NextState). NextState is equal to null if there is no pending transition between states. | 
**reason** | **str** | Reason for Activity termination (specified when Activity in Terminated state). | [optional] 
**error_message** | **str** | If error caused state change - error message shall be provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


