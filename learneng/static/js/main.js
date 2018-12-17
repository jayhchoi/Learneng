const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

if (document.getElementById("message")) {
  setTimeout(function() {
    document.getElementById("message").remove();
  }, 3000);
}
