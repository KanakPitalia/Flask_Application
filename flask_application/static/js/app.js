function show() {
    var check = document.getElementById("show2");
    var text = document.getElementById("password")
    if (check.checked == true){
         text.type = "text";
    }
    else {
        text.type = "password";
    }
}
function show1() {
    var check = document.getElementById("show_h");
    var text = document.getElementById("password1")
    if (check.checked == true){
         text.type = "text";
    }
    else {
        text.type = "password";
    }
}