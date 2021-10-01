var mainApp = angular
    .module("mainApp", [])
    .controller('detailsOfStudent', function ($scope) {
        $scope.student = {
            first_name: "",
            middle_name: "",
            last_name: "",
            date_of_birth: "",
            course: "",
            gender: "",
            hobby: {
                value1: "",
                value2: "",
                value3: ""
            },
            phone_number: "",
            address: "",
            email: "",
            password: "",
            re_password: "",
        };
    });

mainApp.filter('capitalize', function () {
    return function (input) {
        return (angular.isString(input) && input.length > 0) ? input.charAt(0).toUpperCase() + input.substr(1).toLowerCase() : input;
    }
});

function validateForm() {

    var firstName = document.getElementById("first_name");
    var lastName = document.getElementById("last_name");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var rePassword = document.getElementById("rePassword");
    var checkName = /^[a-z]+$/i;
    var checkEmail = /[0-9]{2}[a-zA-Z]{3}[0-9]{3}@nirmauni.ac.in/;
    var checkPassword = /^(?=.\d)(?=.[a-z])(?=.*[A-Z]).{8,20}$/;

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
    else if (email.value == "" || !checkEmail.test(email.value)) {
        alert("Please enter valid email address [valid format is : DDCCCDD@nirmauni.ac.in]");
        email.style.border = "solid 2px red";
        return false;
    }
    else if (checkPassword.value.trim().length < 8) {
        alert("Password must contain 8 characters :)");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (!checkPassword.test(Password.value)) {
        alert("Password must be a combination of uppercase letter, lowercase letter, and digits :)");
        password.style.border = "solid 2px red";
        return false;
    }
    else if (checkPassword.value != rePassword.value) {
        alert("Password doesn't match !");
        password.style.border = "solid 2px red";
        rePassword.style.border = "solid 2px red";
        return false;
    }
    else {
        return true;
    }
}