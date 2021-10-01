var mainApp = angular
  .module("mainApp", [])
  .controller('data', function ($scope) {
    $scope.shopping = {
      total_items: 0,
    };
    $scope.items_list = [
      false,false,false,false,false,false,false,false,false,false,false,false,
    ]

    $scope.counterForItem = function(number) {
      if ( $scope.items_list[number] == false ) {
        $scope.items_list[number] = true;
        $scope.shopping.total_items+=1;
      }
      else {
        $scope.items_list[number] = false;
        $scope.shopping.total_items-=1;
      }
    };
    
  });
