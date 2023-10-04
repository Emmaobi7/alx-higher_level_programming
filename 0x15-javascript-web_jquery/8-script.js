const mv_uri = 'https://swapi-api.alx-tools.com/api/films/?format=json'

$.ajax({
	  url: mv_uri,
	  type: 'GET',
	  dataType: 'json',
	  success: function (data) {
		      const movie_list = data.results;
		      for (let i = 0; i < movie_list.length; ++i) {
			            const mv_title = movie_list[i].title;
			            $('ul#list_movies').append(`<li>${mv_title}</li>`)
			          }
		    }
})
