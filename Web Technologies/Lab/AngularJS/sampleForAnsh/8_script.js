function validateForm() {

    var name = document.getElementById("name");
    var check_name = /^[a-z]+$/i;
    var email = document.getElementById("email");
    var check_email = /[0-9]{2}[a-zA-Z]{3}[0-9]{3}@nirmauni.ac.in/;
    var password = document.getElementById("");

    if (name.value.trim() == '') {
        alert("Empty name.");
        name.style.border = "solid 2px red";
        return false;
    }
    else if (!check_name.test(name.value)) {
        alert("Only Alphabets allowed in name.");
        name.style.border = "solid 2px red";
        return false;
    }
    else if (email.value == "" || !check_email.test(email.value)) {
        alert("Please enter valid email address [valid format is : DDCCCDD@nirmauni.ac.in]");
        email.style.border = "solid 2px red";
        return false;
    }
    else {
        owner_name.style.border = "solid 2px blue";
        email.style.border = "solid 2px blue";
        return true;
    }
}