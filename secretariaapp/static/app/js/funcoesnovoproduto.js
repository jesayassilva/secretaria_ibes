var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.url_server = "http://localhost:8000";
  $scope.token = localStorage.token;
  $scope.categoria = "";
  $scope.nome = "";

  $scope.caregar_select =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/categoria/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          $scope.lista_de_categorias = response.data;
          //$scope.lista_produtos = response.data;
          //console.log(response.data.token);
          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.novo_produto =  function(){
    $http({
        method : "POST",
        url : $scope.url_server+"/produto/",
        headers:{"token":localStorage.token},
        data: {
       "nome":$scope.nome,
      "categoria":$scope.categoria,
        },
        timeout: 1500
        })
        .then(function mySuccess(response) {
          //localStorage.token = response.data.token;
          //console.log(response.data.token);
          //location.href="index.html"
          alert("Cadastrado Com Sucesso");
        }, function myError(response) {
          alert(response.data.Erro);
        });
      };





$scope.caregar_select();



});
