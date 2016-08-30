angular.module('TicketBurst')
.config(['$interpolateProvider', '$routeProvider', '$httpProvider',
function($interpolateProvider, $routeProvider, $httpProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  //  Changed the symbols on line 3 and 4 so Django doesn't try to inject data

  $routeProvider.when('/', {
    controller: 'LoginCtrl',
    controllerAs: 'login',
    templateUrl: 'static/templates/login.html'
  }).when('/register', {
    controller: 'RegisterCtrl',
    controllerAs: 'register',
    templateUrl: 'static/templates/register.html'
  }).when('/events', {
    controller: 'EventsCtrl',
    controllerAs: 'events',
    templateUrl: 'static/templates/events.html'
  }).when('/new-event', {
    controller: 'NewEventCtrl',
    controllerAs: 'newEvent',
    templateUrl: 'static/templates/new-event.html'
  }).when('/venues', {
    controller: 'VenuesCtrl',
    controllerAs: 'venues',
    templateUrl: 'static/templates/venues.html'
  }).when('/new-venue', {
    controller: 'NewVenueCtrl',
    controllerAs: 'newVenue',
    templateUrl: 'static/templates/new-venue.html'
  })
}]);
