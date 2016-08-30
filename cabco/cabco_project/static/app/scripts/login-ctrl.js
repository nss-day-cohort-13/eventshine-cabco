app.controller('LoginCtrl', function($http, $location) {
  const login = this;
  console.log('Carter Loves CONSOLE LOGS');
  login.app_name = 'CabCo'


  login.loginUser = function() {
    $http({
      url: "/login/",
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "username": login.userName,
        "password": login.password,
      }
    }).success((res) => {
      $location.path('/events');
    }).error(() => {
      $location.path('/failed_user');
    })
  }
});
