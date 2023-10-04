const name_url = 'https://fourtonfish.com/hellosalut/?lang=fr'

$(document).ready(function () {
  $.ajax({
    url: name_url,
    type: 'GET',
    datatype: 'json',
    success: function (data) {
      $('div#hello').text(data.hello);
    }
  })
})
