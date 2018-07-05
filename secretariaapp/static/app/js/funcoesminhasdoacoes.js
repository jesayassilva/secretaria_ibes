var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.url_server = "http://localhost:8000";

  $scope.lista_doacoes =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/minhas_doacoes/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.lista_de_doacoes = response.data;
          console.log(response.data.token);

          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.lista_doacoes_solicitadas =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/minhas_doacoes_solicitadas/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.lista_de_doacoes_solicitadas = response.data;
          console.log(response.data.token);

          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.lista_doacoes_finalizadas =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/minhas_doacoes_finalizadas/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          //alert("aki");
          $scope.lista_de_doacoes_finalizadas = response.data;
          console.log(response.data.token);

          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.aceitar_doacao =  function(id_doacao){
    $http({
        method : "GET",
        url : $scope.url_server+"/aceitar_doacao/"+id_doacao+"/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          alert("Doação Finalizada");
          location.href="minhas_doacoes2.html";
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
          //alert(response.data);
          alert("Doação Recusada");
          location.href="minhas_doacoes2.html";
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.lista_doacoes();
  $scope.lista_doacoes_solicitadas();
  $scope.lista_doacoes_finalizadas();


});
