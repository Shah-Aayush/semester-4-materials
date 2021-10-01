var mainApp = angular
                    .module("mainApp", [])
                    .controller('detailsOfPerson', function($scope) { 
                        $scope.person = {
                            name: "",
                            age: "",
                            weight: "",
                            height: "",
                            skills: "",
                        };
                    });