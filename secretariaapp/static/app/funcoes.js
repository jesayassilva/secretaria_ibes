var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.menu_completo = "teste";
  var texto = "nada";

  $scope.iniciar_app =  function(){
    $scope.menu_completo = "teste";
    alert(texto);
  };


  //$scope.iniciar_app();
});
