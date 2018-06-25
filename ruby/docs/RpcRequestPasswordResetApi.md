# SwaggerClient::RpcRequestPasswordResetApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_request_password_reset_post**](RpcRequestPasswordResetApi.md#rpc_request_password_reset_post) | **POST** /rpc/request_password_reset | 


# **rpc_request_password_reset_post**
> rpc_request_password_reset_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcRequestPasswordResetApi.new

args = SwaggerClient::Args2.new # Args2 | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_request_password_reset_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcRequestPasswordResetApi->rpc_request_password_reset_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args2**](Args2.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json



