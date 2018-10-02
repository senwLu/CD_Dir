$(document).ready(function() {
    for(let i=1; i < 31; i++) {
        $('div').append('<img></img>')
        // $('img').last().attr('src','http://pokeapi.co/media/sprites/pokemon/' + i + '.png');
        $('img').last().attr('src',`http://pokeapi.co/media/sprites/pokemon/${i}.png`)
    }
});