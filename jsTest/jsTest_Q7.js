function randomNum() {
  var num = Math.floor(Math.random() * 101);
  console.log(num);

  return num;
}

document.write("첫번째 랜덤난수 : " + randomNum() + "<br>");
document.write("두번째 랜덤난수 : " + randomNum() + "<br>");
document.write("세번째 랜덤난수 : " + randomNum() + "<br>");
