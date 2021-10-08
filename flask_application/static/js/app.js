function show(target) {
    var tag = document.getElementById(target);
    // var check = document.getElementById(tag);
    var link = document.getElementById("showhide");
    if (link.innerHTML == "show password"){
        tag.type = "text";
        link.innerHTML = "hide password";
    }
    else {
        tag.type = "password";
        link.innerHTML = "show password";

    }
}
function show1(target) {
    var tag = document.getElementById(target);
    // var check = document.getElementById(tag);
    var link = document.getElementById("showhide1");
    if (link.innerHTML == "show password"){
        tag.type = "text";
        link.innerHTML = "hide password";
    }
    else {
        tag.type = "password";
        link.innerHTML = "show password";
        
    }
}
function Close(target) {
    var tag = document.getElementById(target);
    tag.style.display = "none";
}
