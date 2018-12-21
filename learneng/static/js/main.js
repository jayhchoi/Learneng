const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// Timeout messages
if (document.getElementById("message")) {
  setTimeout(function() {
    document.getElementById("message").remove();
  }, 3000);
}

// Show datepicker for group.start_date
$(function() {
  $("#datepicker").datepicker({
    dateFormat: "yy-mm-dd"
  });
});
