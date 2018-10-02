$(document).ready(function() {

    $('label input').click(function() {
        // this.value = "";
        $(this).attr('value', "");
    });

    $('form').submit(function() {
        $('#displaySide').append('<div class="cardBox"><h1>' + $('input[name="Fname"]').val() + ' '
            + $('input[name=Lname').val() + '</h1><p class="hideIt">' + $('textArea[name="userDes"]').val()
            + '</p><p>Click for description</p></div>');

        return false;
    });

    $(document).on('click', 'div .cardBox', function() {
        $(this).children().toggle();
    });

});