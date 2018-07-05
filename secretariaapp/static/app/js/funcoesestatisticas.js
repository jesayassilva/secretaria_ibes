var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.url_server = "http://localhost:8000";
  $scope.token = localStorage.token;
  $scope.caregar_select =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/estatisticas/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.estatisticas = response.data;
          console.log(response.data.token);
          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };



$scope.caregar_select();



});
