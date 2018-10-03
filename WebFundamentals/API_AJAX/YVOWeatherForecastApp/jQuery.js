// api key
let key = '4b3026e1ba6dc8dfbfb26e8f0bdfa3c2';
// api call to get weather of city 
let apiByCity = 'https://api.openweathermap.org/data/2.5/weather?q=';

function kelvinToC(k) {
    return k - 273.15;
}

function kelvinToF(k) {
    return (k * (9/5)) - 459.67;
}

$(document).ready(function() {
    // clears text inside input box (works once only once)
    // $('#searchBar').on('click', function() {
    //     $(this).attr('value','');
    // })

    $('#searchBar').on('click', function() {
        this.value = "";
    })


    $('form').submit(function() {
        $('#weatherInfo').children().remove();

        let city = $('input[name="target"]').val();
        let url = apiByCity+city+'&APPID='+key;

        $.get(url, function(res) {
            let name = res.name;
            let temp = kelvinToF(res.main['temp']);

            $('#weatherInfo').append(`<h2>${name}</h2>`);
            $('#weatherInfo').append(`<p>Temperature: ${temp} F</p>`);
            
        }, 'json')

        // return false so page does not refresh
        return false;
    })
});