function getSecondsToday() {
  var nowDate = new Date();
  var todayStart = new Date(
    nowDate.getFullYear(),
    nowDate.getMonth(),
    nowDate.getDate(),
    0,
    0,
    0
  );
  var seconds = Math.floor((nowDate.getTime() - todayStart.getTime()) / 1000);

  return seconds;
}

var secondsToday = getSecondsToday();
alert(secondsToday);
console.log(secondsToday);
