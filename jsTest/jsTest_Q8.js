function change() {
  var element = document.getElementById("hz");
  var currentValue = element.innerHTML;

  if (currentValue === "A") {
    element.innerHTML = "B";
  } else if (currentValue === "B") {
    element.innerHTML = "C";
  } else if (currentValue === "C") {
    element.innerHTML = "A";
  }
}
