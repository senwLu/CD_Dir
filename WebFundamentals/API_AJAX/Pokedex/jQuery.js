$(document).ready(function() {
    for(let i=1; i < 152; i++) {
        $('div.leftDiv').append('<img></img>');
        $('img').last().attr('src',`https://pokeapi.co/media/sprites/pokemon/${i}.png`);
        $('img').last().attr('id',i);
    }

    $(document).on('click','img', function() {
        $('div.rightDiv').children().remove();
        // set variable to pokemon clicked
        var id = $(this).attr('id');

        

        $.get(`https://pokeapi.co/api/v2/pokemon/${id}/`, function(res) {
            var name = res.name;
            var type = res.types[0].type.name;
            var height = res.height;
            var weight = res.weight;

            $('.rightDiv').append(`<h2>${name}</h2>`);
            $('.rightDiv').append(`<img class="centerItems" src=https://pokeapi.co/media/sprites/pokemon/${id}.png></img>`);
            $('.rightDiv').append('<div id="pokeData"></div>');
            $('#pokeData').append(`<h4>Types</h4><ul><li>${type}</li></ul>`);
            $('#pokeData').append(`<h4>Height</h4><p>${height}</p>`);
            $('#pokeData').append(`<h4>Weight</h4><p>${weight}</p>`);

            


            console.log(height);
        })
    })
});