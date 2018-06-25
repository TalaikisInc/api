# SwaggerClient::RpcResetPasswordApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_reset_password_post**](RpcResetPasswordApi.md#rpc_reset_password_post) | **POST** /rpc/reset_password | 


# **rpc_reset_password_post**
> rpc_reset_password_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcResetPasswordApi.new

args = SwaggerClient::Args.new # Args | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_reset_password_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcResetPasswordApi->rpc_reset_password_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args**](Args.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json



