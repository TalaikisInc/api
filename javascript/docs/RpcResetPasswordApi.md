# PostgRestApi.RpcResetPasswordApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcResetPasswordPost**](RpcResetPasswordApi.md#rpcResetPasswordPost) | **POST** /rpc/reset_password | 


<a name="rpcResetPasswordPost"></a>
# **rpcResetPasswordPost**
> rpcResetPasswordPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcResetPasswordApi();

var args = new PostgRestApi.Args(); // Args | 

var opts = { 
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.rpcResetPasswordPost(args, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args**](Args.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

