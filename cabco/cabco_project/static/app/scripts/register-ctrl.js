app.controller('RegisterCtrl', function($http, $location) {
  const register = this;
  console.log("i missed you");
  register.app_name = 'CabCo'


  register.registerUser = function() {
    // Construct $http POST verb XHR
    // console.log("register", register);
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
    }).then(() => {
      $location.path('/login')
    })
  }

});
