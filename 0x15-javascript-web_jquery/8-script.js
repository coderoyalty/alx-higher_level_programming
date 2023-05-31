$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.getJSON(url, function (data) {
        const results = data.results;
        $.each(results, function(index, value) {
            const title = value.title;
            $('ul#list_movies').append(`<li>${title}</li>`);
        });
    });
});
