angular.module('TicketBurst')
.config(function($interpolateProvider, $routeProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');

  $routeProvider
    .when('/', {
      controller: 'RegisterCtrl',
      controllerAs: 'register',
      templateUrl: 'static/templates/login.html'
    })
})
