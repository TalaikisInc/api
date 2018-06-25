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
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.PostgRestApi) {
      root.PostgRestApi = {};
    }
    root.PostgRestApi.Contracts = factory(root.PostgRestApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The Contracts model module.
   * @module model/Contracts
   * @version 0.5.0.0 (d8896be)
   */

  /**
   * Constructs a new <code>Contracts</code>.
   * @alias module:model/Contracts
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>Contracts</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Contracts} obj Optional instance to populate.
   * @return {module:model/Contracts} The populated <code>Contracts</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('addr')) {
        obj['addr'] = ApiClient.convertToType(data['addr'], 'String');
      }
      if (data.hasOwnProperty('bytecode')) {
        obj['bytecode'] = ApiClient.convertToType(data['bytecode'], 'String');
      }
      if (data.hasOwnProperty('balance')) {
        obj['balance'] = ApiClient.convertToType(data['balance'], 'Number');
      }
    }
    return obj;
  }

  /**
   * Note: This is a Primary Key.<pk/>
   * @member {String} addr
   */
  exports.prototype['addr'] = undefined;
  /**
   * @member {String} bytecode
   */
  exports.prototype['bytecode'] = undefined;
  /**
   * @member {Number} balance
   */
  exports.prototype['balance'] = undefined;



  return exports;
}));


