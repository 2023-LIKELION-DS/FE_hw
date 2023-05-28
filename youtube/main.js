// 댓글 받아서 alert창으로 띄워주기
document.querySelector("#submit").onclick = function () {
  var comment = document.getElementById("comment-input");

  alert(comment.value); //value를 넣으면서 안에 있는 값을 가져오게 함
};

//취소 누르면 모든 댓글 없어짐

document.querySelector("#remove").onclick = function () {
  var texts_dumipart = document.getElementsByClassName("texts_dumipart")[0];

  if (texts_dumipart.style.display === "none") {
    texts_dumipart.style.display = "block";
  } else {
    texts_dumipart.style.display = "none";
  }
};

// 답글 누르면 답글 보임!

function reply() {
  var texts_dumipart2 = document.getElementsByClassName("texts_replaypart")[0];

  if (texts_dumipart2.style.display === "none") {
    texts_dumipart2.style.display = "flex";
  } else {
    texts_dumipart2.style.display = "none";
  }
}
