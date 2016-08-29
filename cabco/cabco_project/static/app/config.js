angular.module('TicketBurst')
.config(['$interpolateProvider', '$routeProvider', '$httpProvider', function($interpolateProvider, $routeProvider, $httpProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
  //  Changed the symbols on line 3 and 4 so Django doesn't try to inject data

  $routeProvider.when('/', {
      controller: 'RegisterCtrl',
      controllerAs: 'register',
      templateUrl: 'static/templates/register.html'
    })
}]);
