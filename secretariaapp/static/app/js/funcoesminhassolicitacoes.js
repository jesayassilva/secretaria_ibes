var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.url_server = "http://localhost:8000";


  $scope.doacoes_pedidas =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/doacoes_pedidas/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.lista_doacoes_pedidas = response.data;
          console.log(response.data.token);

          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.doacoes_concluidas =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/doacoes_concluidas/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.lista_doacoes_concluidas = response.data;
          console.log(response.data.token);

          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.recusar_doacao =  function(id_doacao){
    $http({
        method : "GET",
        url : $scope.url_server+"/recusar_doacao/"+id_doacao+"/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          alert("Dessistencia Atualizada da Doação");
          location.href="minhas_solicitacoes2.html";
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.doacoes_pedidas();
  $scope.doacoes_concluidas();




});
