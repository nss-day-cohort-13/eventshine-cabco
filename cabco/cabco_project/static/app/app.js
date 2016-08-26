var app = angular
  .module('TicketBurst', ['interpolateProvider', 'ngRoute'])
  .config(function($interpolateProvider, $routeProvider) {
    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');

    $routeProvider
      .when('/', {
        controller: 'RegisterCtrl',
        controllerAs: 'register',
        templateUrl: '/static/templates/login.html'
      })
      .otherwise('/')

  });

  //  Changed the symbols on line 4 and 5 so Django doesn't try to inject data

