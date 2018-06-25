# SwaggerClient::RpcEncryptIvApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_encrypt_iv_post**](RpcEncryptIvApi.md#rpc_encrypt_iv_post) | **POST** /rpc/encrypt_iv | 


# **rpc_encrypt_iv_post**
> rpc_encrypt_iv_post(args, opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::RpcEncryptIvApi.new

args = nil # Object | 

opts = { 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.rpc_encrypt_iv_post(args, opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling RpcEncryptIvApi->rpc_encrypt_iv_post: #{e}"
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



