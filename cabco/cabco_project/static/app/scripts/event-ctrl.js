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
    console.log("All Events: ", res.data);
    events.allEvents = res.data;
  })

  events.buyTicket = (eventPK) => {
    var eventLimit;
    for(var i = 0; i < events.allEvents.length; i++){
      eventObjects = events.allEvents[i];
      eventLimit = eventObjects.fields.atendee_limit;
    };
    console.log('eventLimit', eventLimit);
    $http({
      url: '/get_ticket_count/',
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        'event_pk': eventPK
      }
    }).then((res) => {
      console.log('All Tickets for specified Event: ', res.data);
      events.allSpecifiedTickets = res.data;
      if(events.allSpecifiedTickets < eventLimit){
        console.log('eventPK2', eventPK);
        // create a new ticket
        $http({
          url: '/new_ticket/',
          method: 'POST',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            'event_pk': eventPK,
          }
        })
      } else {
        alert('Sorry, Sold Out! 😎');
      }
    })
  };


}); // end
