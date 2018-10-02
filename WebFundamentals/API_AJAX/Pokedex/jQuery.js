$(document).ready(function() {
    for(let i=1; i < 51; i++) {
        $('div.leftDiv').append('<img></img>')
        $('img').last().attr('src',`http://pokeapi.co/media/sprites/pokemon/${i}.png`)
    }
});