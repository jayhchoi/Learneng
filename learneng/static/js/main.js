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
    dateFormat: "yy-mm-dd",
    minDate: 0
  });
});

// Pick day from date
if (document.querySelector("#id_day")) {
  document.querySelector("#id_day").addEventListener("mouseover", e => {
    const DateInput = document.querySelector("#datepicker");
    let day = new Date(DateInput.value).getDay();
    switch (day) {
      case 0:
        e.target.value = "일요일";
        break;
      case 1:
        e.target.value = "월요일";
        break;
      case 2:
        e.target.value = "화요일";
        break;
      case 3:
        e.target.value = "수요일";
        break;
      case 4:
        e.target.value = "목요일";
        break;
      case 5:
        e.target.value = "금요일";
        break;
      case 6:
        e.target.value = "토요일";
        break;
    }
  });
}
