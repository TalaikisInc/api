# PostgRestApi.RpcLoginApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcLoginPost**](RpcLoginApi.md#rpcLoginPost) | **POST** /rpc/login | 


<a name="rpcLoginPost"></a>
# **rpcLoginPost**
> rpcLoginPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcLoginApi();

var args = new PostgRestApi.Args3(); // Args3 | 

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
apiInstance.rpcLoginPost(args, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Args3**](Args3.md)|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

