import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/v1/"; /*
// add Access-Control-Allow-Origin *
axios.defaults.headers.common["Content-Type"] = "application/json";
axios.defaults.headers.common.Accept = "application/json";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "localhost:5173";

axios.defaults.headers.common["mode"] = "no-cors";
*/
export const register = (username: string, email: string, password: string) => {
  return axios
    .post(API_URL + "register", {
      username,
      email,
      password,
    })
    .then((response) => {
      if (response.data.accessToken) {
        localStorage.setItem(
          "token",
          JSON.stringify(response.data.accessToken)
        );
      }
      return response;
    });
};

export const login = (username: string, password: string) => {
  return axios
    .post(API_URL + "login", {
      username,
      password,
    })
    .then((response) => {
      if (response.data.accessToken) {
        localStorage.setItem(
          "token",
          JSON.stringify(response.data.accessToken)
        );
      }
      return response;
    });
};

export const verifyToken = (token: string) => {
  return axios.post(API_URL + "token?token=" + token, {}).then((response) => {
    if (response.status === 401) {
      //localStorage.removeItem("token");
    }
    return response;
  });
};
