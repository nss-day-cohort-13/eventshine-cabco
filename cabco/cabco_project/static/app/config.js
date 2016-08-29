angular.module('TicketBurst')
.config(['$interpolateProvider', '$routeProvider', '$httpProvider',
function($interpolateProvider, $routeProvider, $httpProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  //  Changed the symbols on line 3 and 4 so Django doesn't try to inject data

  $routeProvider.when('/', {
    controller: 'RegisterCtrl',
    controllerAs: 'register',
    templateUrl: 'static/templates/register.html'
  }).when('/login', {
    controller: 'LoginCtrl',
    controllerAs: 'login',
    templateUrl: 'static/templates/login.html'
  })
}]);
