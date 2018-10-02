$(document).ready(function() {
    $('label input').click(function() {
        this.value = "";
    });

    $('form').submit(function() {
    
        $('tbody').append("<tr></tr>");

        $('tr').last().append('<td>'+userForm.Fname.value+'</td>'+
        '<td>'+userForm.Lname.value+'</td>'+
        '<td>'+userForm.eAddress.value+'</td>'+
        '<td>'+userForm.contactNo.value+'</td>');

        $("#addForm")[0].reset();

        return false;
    });
});