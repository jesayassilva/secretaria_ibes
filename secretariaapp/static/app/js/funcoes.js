var app = angular.module('myApp', ['ngStorage']);
app.controller('appCtrl',function($scope, $http) {
  //$scope.url_server = "http://192.168.133.156:8000";
  $scope.url_server = "http://localhost:8000";
  $scope.usuario_id = localStorage.usuario_id;
  $scope.nome_produto = "";

  $scope.lista_doacoes =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/doacoes/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          $scope.lista_de_doacoes = response.data;
          console.log(response.data.token);
          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };
  $scope.pesquisar_categoria =  function(id){
    $http({
        method : "GET",
        url : $scope.url_server+"/doacoes/"+id+"/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          $scope.lista_de_doacoes = response.data;
          //console.log(response.data.token);
          //alert(response.data);
        }, function myError(response) {
          //alert(response.data.Erro);
          $('.mini.modal').modal('show');
        });
  };
  $scope.lista_categorias =  function(){
    $http({
        method : "GET",
        url : $scope.url_server+"/categoria/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          $scope.lista_de_categorias = response.data;
          //alert(response.data);
        }, function myError(response) {
            //alert(response.data.Erro);
            $scope.lista_de_categorias = "";

        });
  };

  $scope.euquero =  function(id_doacao){
    $http({
        method : "GET",
        url : $scope.url_server+"/euquero/"+id_doacao+"/",
        headers:{"token":localStorage.token},
        timeout: 2000
        })
        .then(function mySuccess(response) {
          alert("Doação Solicitada com Sucesso");
          location.href="minhas_solicitacoes2.html";
        }, function myError(response) {
          alert(response.data.Erro);
        });
  };

  $scope.sair_app =  function(){
    location.href="index.html"
    //localStorage.token = null;
    //alert(response.data.Erro);
  };


  $scope.minhas_doacoes =  function(){
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


  $scope.pesquisa_doacao =  function(){
    $http({
        method : "POST",
        url : $scope.url_server+"/pesquisa_doacao/",
        headers:{"token":localStorage.token},
        data: {
          "nome_produto":$scope.nome_produto,
        },
        timeout: 2000
        })
        .then(function mySuccess(response) {
          $scope.lista_de_doacoes = response.data;
          alert("foi");
          //console.log(response.data.token);
          //alert(response.data);
        }, function myError(response) {
          alert(response.data.Erro);

        });
  };



  $scope.lista_doacoes();
  $scope.lista_categorias();
});
