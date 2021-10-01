function validateForm() {

    var firstName = document.getElementById("first_name");
    var middleName = document.getElementById("middle_name");
    var lastName = document.getElementById("last_name");
    var ipAddress = document.getElementById("ip-address");
    var phoneNumber = document.getElementById("phone-number");
    var date = document.getElementById("date");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var rePassword = document.getElementById("rePassword");
    
    var checkName = /^[a-z]+$/i;
    var checkEmail = /^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/;
    var check_password = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
    var check_ip = /^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$/;
    var check_date = /^([0-9]{2})\/([0-9]{2})\/([0-9]{4})$/;
    var check_middle = /^[a-zA-Z0-9]+$/;

    if (firstName.value.trim() == '' || lastName.value.trim() == '') {
        alert("Please enter first name and last name :)");
        firstName.style.border = "solid 2px red";
        lastName.style.border = "solid 2px red";
        return false;
    }
    else if (!checkName.test(firstName.value) || !checkName.test(lastName.value)) {
        alert("Please enter name properly :)");
        firstName.style.border = "solid 2px red";
        lastName.style.border = "solid 2px red";
        return false;
    }
    else if (!check_middle.test(middleName.value)) {
        alert("Please enter middle name properly :)");
        middleName.style.border = "solid 2px red";
        return false;
    }
    else if (!check_date.test(date.value)) {
        alert("Please date properly :)");
        date.style.border = "solid 2px red";
        return false;
    }
    else if (phoneNumber.value.length < 10) {
        alert("Please enter atleast 10 character in phone number :)");
        phoneNumber.style.border = "solid 2px red";
        return false;
    }
    else if (ipAddress.value == "" || !check_ip.test(ipAddress.value)) {

        // valid ips : 
        // 127.0.0.1
        // 192.168.1.1
        // 255.255.255.255

        //invalid ips : 
        // 30.168.1.255.1
        // 127.1
        // 3...3

        alert("Please enter valid ip address");
        ipAddress.style.border = "solid 2px red";
        return false;
    }
    else if (email.value == "" || !checkEmail.test(email.value)) {
        alert("Please enter valid email address [valid format is : DDCCCDD@nirmauni.ac.in]");
        email.style.border = "solid 2px red";
        return false;
    }
    else if (password.value.trim().length < 8) {
        alert("Password must contain 8 characters :)");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (!check_password.test(password.value)) {
        alert("Password must be a combination of uppercase letter, lowercase letter, and digits :)");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (password.value != rePassword.value) {
        alert("Password doesn't match !");
        password.style.border = "solid 2px red";
        rePassword.style.border = "solid 2px red";
        return false;
    }
    else {
        return true;
    }
}