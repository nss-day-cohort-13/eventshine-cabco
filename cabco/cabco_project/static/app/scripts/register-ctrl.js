app.controller('RegisterCtrl', function($http, $location) {
  const register = this;
  console.log("i missed you");
  register.app_name = 'CabCo'


  register.registerUser = function() {
    // Construct $http POST verb XHR
    // IN ORDER TO HAVE A POST TO DJANGO MUST USE ORIGINAL HTTP CALL AS BELOW
    // CANNOT USE SHORTCUT METHODS, DOES NOT WORK CORRECTLY
    $http({
      url: "/register/",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "username": register.userName,
        "password": register.password,
        "email": register.email,
        "first_name": register.firstName,
        "last_name": register.lastName
      }
    }).success((res) => {
      $location.path('/events');
    }).error(() => {
      $location.path('/failed_user');
    })
  }

});
