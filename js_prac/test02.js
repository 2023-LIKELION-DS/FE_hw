/*var el = document.getElementById("brand-title"); //id를 통헤 값 가져오기
console.log(el);

console.log(el.innerHTML); //html 태그만 제거
console.log(el.innerText); //텍스트만 로드

el.innerText = "안녕하세요:)"; //태그 안 텍스트 내용 변경

var el = document.getElementsByClassName("sub-title"); //class를 통해 값 가져오기
console.log(el);
*/
var el = document.getElementById("brand-title");

var myfunc = function () {
  alert("addEventListener");
};

el.addEventListener("click", myfunc);
