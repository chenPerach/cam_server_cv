const http = new XMLHttpRequest()
const url = "http://"+document.domain+":"+location.port



function sendjson(route,json){
    http.open("POST",url + route)
    http.setRequestHeader("Content-Type","application/json")

    const json_string = JSON.stringify(json)
    http.send(json_string)
}
