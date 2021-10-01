function validateForm() {

    var name = document.getElementById("name");
    var check_name = /^[a-z]+$/i;
    var email = document.getElementById("email");
    var check_email = /[0-9]{2}[a-zA-Z]{3}[0-9]{3}@nirmauni.ac.in/;
    var password = document.getElementById("password");
    var re_password = document.getElementById("rePassword");
    var check_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$";
    console.log(password.value + re_password.value);

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
        alert("Please enter valid email address [valid format is : DDCCCDD@nirmauni.ac.in].");
        email.style.border = "solid 2px red";
        return false;
    }
    else if (password.value.trim().length < 8) {
        alert("Password must contain 8 characters.");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (!check_password.test(password.value)) {
        alert("Password must be a combination of uppercase letter, lowercase letter, and digits.");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (password.value != re_password.value) {
        alert("Password doesn't match.");
        password.style.border = "solid 2px red";
        re_password.style.border = "solid 2px red";
        return false;
    }
    else {
        name.style.border = "solid 2px blue";
        email.style.border = "solid 2px blue";
        password.style.border = "solid 2px blue";
        re_password.style.border = "solid 2px blue";
        console.log(password.value + " " + re_password.value );
        return true;
    }
}
function validateFileType(){
    var fileName = document.getElementById("img").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        //TO DO
    }else{
        alert("Only jpg/jpeg and png files are allowed!");
    }   
}

{/*
     <input name="image" type="file" id="fileName" accept=".jpg,.jpeg,.png" onchange="validateFileType()"/>
<script type="text/javascript">
    function validateFileType(){
        var fileName = document.getElementById("fileName").value;
        var idxDot = fileName.lastIndexOf(".") + 1;
        var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
        if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
            //TO DO
        }else{
            alert("Only jpg/jpeg and png files are allowed!");
        }   
    }
</script> 
*/}