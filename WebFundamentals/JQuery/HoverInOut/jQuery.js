

$(document).ready(function() {
    $('img').hover(function() {
        $(this).attr('src', 'img/skitchtocat.png');
    }, function() {
        $(this).attr('src', 'img/privateinvestocat.jpg');
    });
});