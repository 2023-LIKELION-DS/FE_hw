document.querySelector("#btn").onclick = function () {
  let img = document.createElement("img");
  img.setAttribute("src", "read.png");
  img.setAttribute("style", "width:300px;margin-top:20px;"); //img는 attribute이므로
  document.body.append(img); //확장시킨다.
};
