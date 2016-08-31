app.controller('EventsCtrl', function($http, $location) {
  const events = this;

  events.app_name = 'CabCo'

  events.logout = () => {
    window.location = '/logout'
  }

  events.createEvent =  () => {
    $location.path('/new-event');
  }

  events.createVenue =  () => {
    $location.path('/new-venue');
  }

  $http.get('http://localhost:8000/events')
  .then((res) => {
          console.log("All Events: ", res )
          events.allEvents = res.data
  })

}); // end
