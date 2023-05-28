document.querySelector("#btn").onclick = function () {
    let img = document.createElement("img");
    img.setAttribute("src", "./vaundy.webp");
    img.setAttribute("style", "width:300px;margin-top:20px");
    document.body.append(img); /*append 추가한다 확장시킨다*/
};
