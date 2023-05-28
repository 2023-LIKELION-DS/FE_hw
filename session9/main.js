document.querySelector("#btn2").onclick = function () {
    alert(document.getElementById('text').value);
};

document.querySelector("#btn1").onclick = function () {
    document.getElementById('text').value = "";
};