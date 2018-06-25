# PostgRestApi.RpcRequestPasswordResetApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcRequestPasswordResetPost**](RpcRequestPasswordResetApi.md#rpcRequestPasswordResetPost) | **POST** /rpc/request_password_reset | 


<a name="rpcRequestPasswordResetPost"></a>
# **rpcRequestPasswordResetPost**
> rpcRequestPasswordResetPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcRequestPasswordResetApi();

var args = new PostgRestApi.Args2(); // Args2 | 

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
apiInstance.rpcRequestPasswordResetPost(args, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args2**](Args2.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

