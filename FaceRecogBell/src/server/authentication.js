import { client } from "../axios"

export function SendLoginRequest(username, password) {
    return client.post(
        "/login/",
        {
            username: username,
            password: password
        }
    ).then(function (res) {
        return [true, res.data.username]
    }).catch(function () {
        return [false, undefined]
    })
}


export function SendSignupRequest(email, username, password){
    return client.post(
        "/signup/",
        {
            email: email,
            username: username,
            password: password
        }
    ).then(function (res) {
        return [true, res.data.username]
    }).catch(function () {
        return [false, undefined]
    })
}