# PostgRestApi.RpcGenRandomBytesApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcGenRandomBytesPost**](RpcGenRandomBytesApi.md#rpcGenRandomBytesPost) | **POST** /rpc/gen_random_bytes | 


<a name="rpcGenRandomBytesPost"></a>
# **rpcGenRandomBytesPost**
> rpcGenRandomBytesPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcGenRandomBytesApi();

var args = null; // Object | 

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
apiInstance.rpcGenRandomBytesPost(args, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | **Object**|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

