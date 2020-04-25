setInterval(sendjson,1000,"/proccesHSV")

function getjson(){
    const json = {
        hmax: document.getElementById("hmax").value,
        smax: document.getElementById("smax").value,
        vmax: document.getElementById("vmax").value,
        hmin: document.getElementById("hmin").value,
        smin: document.getElementById("smin").value,
        vmin: document.getElementById("vmin").value
    };
    console.log(JSON.stringify(json))
    return json
}
