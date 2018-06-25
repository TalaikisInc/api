# SwaggerClient::RpcSignupApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_signup_post**](RpcSignupApi.md#rpc_signup_post) | **POST** /rpc/signup | 


# **rpc_signup_post**
> rpc_signup_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcSignupApi.new

args = SwaggerClient::Args1.new # Args1 | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_signup_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcSignupApi->rpc_signup_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args1**](Args1.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json



