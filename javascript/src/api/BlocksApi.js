/**
 * PostgREST API
 * standard public schema
 *
 * OpenAPI spec version: 0.5.0.0 (d8896be)
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: unset
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/Blocks'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/Blocks'));
  } else {
    // Browser globals (root is window)
    if (!root.PostgRestApi) {
      root.PostgRestApi = {};
    }
    root.PostgRestApi.BlocksApi = factory(root.PostgRestApi.ApiClient, root.PostgRestApi.Blocks);
  }
}(this, function(ApiClient, Blocks) {
  'use strict';

  /**
   * Blocks service.
   * @module api/BlocksApi
   * @version 0.5.0.0 (d8896be)
   */

  /**
   * Constructs a new BlocksApi. 
   * @alias module:api/BlocksApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the blocksDelete operation.
     * @callback module:api/BlocksApi~blocksDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.block 
     * @param {module:model/String} opts.prefer Preference
     * @param {module:api/BlocksApi~blocksDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.blocksDelete = function(opts, callback) {
      opts = opts || {};
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
        'block': opts['block'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
        'Prefer': opts['prefer']
      };
      var formParams = {
      };

      var authNames = [];
      var contentTypes = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var accepts = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var returnType = null;

      return this.apiClient.callApi(
        '/blocks', 'DELETE',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the blocksGet operation.
     * @callback module:api/BlocksApi~blocksGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Blocks} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.block 
     * @param {String} opts.select Filtering Columns
     * @param {String} opts.order Ordering
     * @param {String} opts.range Limiting and Pagination
     * @param {String} opts.rangeUnit Limiting and Pagination (default to items)
     * @param {String} opts.offset Limiting and Pagination
     * @param {String} opts.limit Limiting and Pagination
     * @param {module:model/String} opts.prefer Preference
     * @param {module:api/BlocksApi~blocksGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Blocks}
     */
    this.blocksGet = function(opts, callback) {
      opts = opts || {};
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
        'block': opts['block'],
        'select': opts['select'],
        'order': opts['order'],
        'offset': opts['offset'],
        'limit': opts['limit'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
        'Range': opts['range'],
        'Range-Unit': opts['rangeUnit'],
        'Prefer': opts['prefer']
      };
      var formParams = {
      };

      var authNames = [];
      var contentTypes = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var accepts = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var returnType = Blocks;

      return this.apiClient.callApi(
        '/blocks', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the blocksPatch operation.
     * @callback module:api/BlocksApi~blocksPatchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.block 
     * @param {module:model/Blocks} opts.blocks blocks
     * @param {module:model/String} opts.prefer Preference
     * @param {module:api/BlocksApi~blocksPatchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.blocksPatch = function(opts, callback) {
      opts = opts || {};
      var postBody = opts['blocks'];


      var pathParams = {
      };
      var queryParams = {
        'block': opts['block'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
        'Prefer': opts['prefer']
      };
      var formParams = {
      };

      var authNames = [];
      var contentTypes = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var accepts = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var returnType = null;

      return this.apiClient.callApi(
        '/blocks', 'PATCH',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the blocksPost operation.
     * @callback module:api/BlocksApi~blocksPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {module:model/Blocks} opts.blocks blocks
     * @param {module:model/String} opts.prefer Preference
     * @param {module:api/BlocksApi~blocksPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.blocksPost = function(opts, callback) {
      opts = opts || {};
      var postBody = opts['blocks'];


      var pathParams = {
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
        'Prefer': opts['prefer']
      };
      var formParams = {
      };

      var authNames = [];
      var contentTypes = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var accepts = ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'];
      var returnType = null;

      return this.apiClient.callApi(
        '/blocks', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
