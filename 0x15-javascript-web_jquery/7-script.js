const ch_uri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

$.ajax({
	  url: ch_uri,
	  Type: 'GET',
	  datatype: 'json',
	  success: function (data) {
		      $('div#character').text(data.name)
		    }
})
