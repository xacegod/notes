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

  static async signIn(data) {
    let url = `${BaseApi.URL}/v1/signin`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      }); 
  }

  static async checkUser(data) {
    let url = `${BaseApi.URL}/v1/check_user`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async adminCheckUsername(data) {
    let url = `${BaseApi.URL}/v1/admin_check_username`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async adminGetAllUsers(data) {
    let url = `${BaseApi.URL}/v1/admin_get_all_users`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async changePassword(data) {
    let url = `${BaseApi.URL}/v1/change_password`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async checkUserEmail(data) {
    let url = `${BaseApi.URL}/v1/check_user_email`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async checkUserUsername(data) {
    let url = `${BaseApi.URL}/v1/check_user_username`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }

  static async adminChangeUsertype(data) {
    let url = `${BaseApi.URL}/v1/admin_change_usertype`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }
  static async resendActivationEmail(data) {
    let url = `${BaseApi.URL}/v1/resend_activation_email`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }
  static async activateUserFromLink(data) {
    let url = `${BaseApi.URL}/v1/activate_user_by_link`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }
  static async createResetPassword(data) {
    let url = `${BaseApi.URL}/v1/create_reset_password`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }
  static async resetPassword(data) {
    let url = `${BaseApi.URL}/v1/reset_password`;
    
    return axios.post(url, data)
      .then((res) => res.data)
      .catch((e) => {
        console.error(e);
      });
  }
}
# 
