# V1beta1HTTPIngressBackend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_rules** | **list[str]** | Serialized HAProxy rules to apply on server backend including request, response or header rewrite. acls also can be used. https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#1 | [optional] 
**header_rules** | **list[str]** | Header rules to modifies the header.  Deprecated: Use backendRule, will be removed. | [optional] 
**host_names** | **list[str]** | Host names to forward traffic to. If empty traffic will be forwarded to all subsets instance. If set only matched hosts will get the traffic. This is an handy way to send traffic to Specific StatefulSet pod. IE. Setting [web-0] will send traffic to only web-0 host for this StatefulSet, https://kubernetes.io/docs/tasks/stateful-application/basic-stateful-set/#creating-a-statefulset | [optional] 
**name** | **str** | User can specify backend name for using it with custom acl Otherwise it will be generated | [optional] 
**rewrite_rules** | **list[str]** | Path rewrite rules with haproxy formatted regex.  Deprecated: Use backendRule, will be removed. | [optional] 
**service_name** | **str** | Specifies the name of the referenced service. | [optional] 
**service_port** | **str** | Specifies the port of the referenced service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


