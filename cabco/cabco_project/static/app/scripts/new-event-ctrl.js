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
        'event_name': newEvent.eventName,
        'description': newEvent.description,
        'city': newEvent.city,
        'begin_date_time': newEvent.beginDateTime,
        'end_date_time': newEvent.endDateTime,
        'atendee_limit': newEvent.atendeeLimit,
        'event_price': newEvent.eventPrice,
        'event_venue': newEvent.eventVenue
      }
    }).success((res) => {
      $location.path('/events'); //change later
    }).error(() => {
      $location.path('/failed_user'); // we will change this later it just needs to go somewhere for now
    })
  }

  $http.get('/venues/')
  .then((res) => {
          console.log("All Venues: ", res.data);
          newEvent.allVenues = res.data
  })

});
