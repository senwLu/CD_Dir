$(document).ready(function() {
    $('label input').click(function() {
        this.value = "";
    });

    $('form').submit(function() {
    
        // $('table').append("<tr></tr>");

        // $('tr').last().append('<td>'+userForm.Fname.value+'</td>'+
        // '<td>'+userForm.Lname.value+'</td>'+
        // '<td>'+userForm.eAddress.value+'</td>'+
        // '<td>'+userForm.contactNo.value+'</td>');

        $('table').append('<tr><td>'+ $('input[name="Fname"]').val() + 
            '</td><td>' + $('input[name="Lname"]').val() + '</td><td>' +
            $('input[name="eAddress"]').val() + '</td><td>'+
            $('input[name="contactNo"]').val() + '</td></tr>');

        $("#addForm")[0].reset();

        return false;
    });
});