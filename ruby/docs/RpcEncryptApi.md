# SwaggerClient::RpcEncryptApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_encrypt_post**](RpcEncryptApi.md#rpc_encrypt_post) | **POST** /rpc/encrypt | 


# **rpc_encrypt_post**
> rpc_encrypt_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcEncryptApi.new

args = nil # Object | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_encrypt_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcEncryptApi->rpc_encrypt_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | **Object**|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json



