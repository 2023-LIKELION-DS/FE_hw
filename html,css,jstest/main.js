function showComment() {
  var comment = document.getElementById("commentInput").value;
  alert("댓글 내용: " + comment);
}

function deleteComment() {
  document.getElementById("commentInput").value = "";
}

function toggleReplyList() {
  var replyList = document.getElementById("replyList");
  var replyButton = document.getElementById("replyButton");
  var replyButtonIcon = replyButton.querySelector("i");

  if (replyList.style.display === "none") {
    replyList.style.display = "block";
    replyButtonIcon.classList.replace("fa-chevron-down", "fa-chevron-up");
    replyButton.classList.add("active");
  } else {
    replyList.style.display = "none";
    replyButtonIcon.classList.replace("fa-chevron-up", "fa-chevron-down");
    replyButton.classList.remove("active");
  }
}
