app.controller('EventsCtrl', function($http, $location) {
  const events = this;

  events.app_name = 'CabCo'

  events.logout = () => {
    window.location = '/logout/'
  }

  events.createEvent =  () => {
    $location.path('/new-event/');
  }

  events.createVenue =  () => {
    $location.path('/new-venue/');
  }

  $http.get('/events/')
  .then((res) => {
          console.log("All Events: ", res.data)
          events.allEvents = res.data
  })


  events.buyTicket = (eventPK) => {
    // console.log('eventPK', eventPK);
    $http.get('/events/')
    .then((res) => {
      allEvents = res.data
      for(var i = 0; i < allEvents.length; i++){
        eventObjects = allEvents[i];
        // console.log('eventFields', eventFields);
        if(eventPK === eventObjects.pk){
          // console.log('eventPK', eventPK);
          $http.get('/tickets/').then((res) => {
            allTickets = res.data
            console.log('allTickets', res.data);
            var eventLimit = eventObjects.fields.atendee_limit;
            for(var i = 0; i < eventLimit; i++){
              counter = i + 1;
              console.log('counter', counter);
              if(counter < eventLimit){
                // create a new ticket
              }
            }
          })
        }

      }
    })
  }

}); // end
