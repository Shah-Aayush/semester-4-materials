var mainApp = angular
                    .module("mainApp", [])
                    .controller('personalDetails', function($scope) { 
                        $scope.student = {
                            firstName: "",
                            lastName: "",
                            mobNum: "",
                            emailID: "",
                            educationalQualification: "",
                        };
                    });