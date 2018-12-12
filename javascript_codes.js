# BaseApi
class BaseApi {}

BaseApi.URL = process.env.NODE_ENV === 'development' ? location.protocol + '//' + location.hostname + ':5005' : location.origin;
export default BaseApi;
#

# UserApi
import axios from 'axios';
import BaseApi from './BaseApi';

export default class UserApi extends BaseApi {
  static async signUp(data) {
    let url = `${BaseApi.URL}/v1/signup`;
    
    return axios.post(url,data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }  
# 
