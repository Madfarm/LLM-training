var ShowPasswordToggle = document.querySelector("[type='password']");
ShowPasswordToggle.onclick = function () {
  document.querySelector("[type='password']").classList.add("input-password");
  document.getElementById("toggle-password").classList.remove("d-none");

  var passwordField = document.querySelector("[type='password']");
  if (passwordField.type === "password") {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
  }


};