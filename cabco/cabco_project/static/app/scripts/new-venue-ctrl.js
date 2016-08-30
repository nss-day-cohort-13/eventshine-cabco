app.controller('NewVenueCtrl', function($http, $location) {
  const venue = this;
  console.log("New Venue");
  venue.app_name = 'CabCo'


  venue.createVenue = function() {
    // Construct $http POST verb XHR
    // IN ORDER TO HAVE A POST TO DJANGO MUST USE ORIGINAL HTTP CALL AS BELOW
    // CANNOT USE SHORTCUT METHODS, DOES NOT WORK CORRECTLY
    $http({
      url: "/new_venue/",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "venue_name": venue.venue_name,
        "seating_capacity": venue.seating_capacity
      }
    }).success((res) => {
      $location.path('/homepage');
    }).error(() => {
      $location.path('/failed_user');
    })
  }

});