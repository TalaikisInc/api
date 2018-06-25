# SwaggerClient::RpcLoginApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_login_post**](RpcLoginApi.md#rpc_login_post) | **POST** /rpc/login | 


# **rpc_login_post**
> rpc_login_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcLoginApi.new

args = SwaggerClient::Args3.new # Args3 | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_login_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcLoginApi->rpc_login_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args3**](Args3.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json



