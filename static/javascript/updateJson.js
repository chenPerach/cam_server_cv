function slide(event,name,ui){
    json[name+"min"] = ui.values[0]
    json[name+"max"] = ui.values[1]
}
$(function () {
  $(".my-slider").each(function () {
    var max = parseInt( $(this).text())
    var name = $(this).attr("id")

    $(this).empty().slider({
      range:true,
      max: max,
      min:0,
      values: [0,max],
      slide: function(event,ui){
        slide(event,name,ui)
      },
      change: function () {
        sendjson(route,json)
      }    
    })
  })
})

$(document).ready(function() {
  $(".my-checkbox").click(function () {
    json[$(this).attr("id")] = !json[$(this).attr("id")]
    sendjson(route,json)
  })
})