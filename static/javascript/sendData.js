const http = new XMLHttpRequest()
const url = "http://"+document.domain+":"+location.port



function sendjson(route){
    http.open("POST",url + route)
    http.setRequestHeader("Content-Type","application/json")

    const json_string = JSON.stringify(getjson())
    http.send(json_string)
}
