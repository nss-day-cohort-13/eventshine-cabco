app.controller('VenuesCtrl', function($http, $location) {

  const venues = this;


  venues.app_name = 'CabCo'

  venues.logout = () => {
    window.location = '/logout/'
  }

  venues.events = () => {
    $location.path('/events/');
  }

  venues.createEvent =  () => {
    $location.path('/new-event/');
  }

  venues.createVenue =  () => {
    $location.path('/new-venue/');
  }

  $http.get('/venues/')
  .then((res) => {
          console.log("All Venues: ", res )
          venues.allVenues = res.data
  })

});


















// Make venue.htlm
    // button- create venues
    // ng-repeat over all venues with get call - <div ng-repeat li button inside
    //logout

// controller - app name - get call to get all venues - ng-repeat var