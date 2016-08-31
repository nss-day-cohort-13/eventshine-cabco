app.controller('NewEventCtrl', function($http, $location) {
  const newEvent = this;
  newEvent.app_name = 'CabCo'


  newEvent.createEvent = function() {
    // Construct $http POST verb XHR
    // IN ORDER TO HAVE A POST TO DJANGO MUST USE ORIGINAL HTTP CALL AS BELOW
    // CANNOT USE SHORTCUT METHODS, DOES NOT WORK CORRECTLY
    $http({
      url: "/new-event/",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "event_name": newEvent.eventName,
        "event_date": newEvent.eventDate,
        "event_price": newEvent.eventPrice,
        "event_attendee_capacity": newEvent.eventAttendeeCapacity
      }
    }).success((res) => {
      $location.path('/homepage'); //change later
    }).error(() => {
      $location.path('/failed_user'); // we will change this later it just needs to go somewhere for now
    })
  }

});
