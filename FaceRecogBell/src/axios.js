import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
axios.defaults.withXSRFToken = true

export const client = axios.create({ // Creates the connection between frontend and backend
    baseURL: "http://127.0.0.1:8000"
});


// client.interceptors.response.use(function (response) {
//     return response;
// }, function (error) {
//     // Intercepts all requests and if the status is 401 (Unauthorized) 
//     // or 403 (Forbidden), it takes them to the login page
//     if (error.response.status == 403 || error.response.status == 401) {
//         window.location.replace(
//             "/",
//         );
//     }
//     return Promise.reject(error);
// });