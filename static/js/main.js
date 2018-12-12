const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(function() {
  document.getElementById("message").remove();
}, 3000);
