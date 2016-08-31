app.controller('NewVenueCtrl', function($http, $location) {
  const newVenue = this;
  console.log("New Venue");
  newVenue.app_name = 'CabCo'


  newVenue.createVenue = function() {
    // Construct $http POST verb XHR
    // IN ORDER TO HAVE A POST TO DJANGO MUST USE ORIGINAL HTTP CALL AS BELOW
    // CANNOT USE SHORTCUT METHODS, DOES NOT WORK CORRECTLY
    $http({
      url: "/new_venue/",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "venue_name": newVenue.venueName,
        "seating_capacity": newVenue.seatingCapacity
      }
    }).success((res) => {
      $location.path('/venues');
    }).error(() => {
      $location.path('/failed_user');
    })
  }

});
