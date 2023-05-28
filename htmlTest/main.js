function change_add() {
  var comment = document.getElementById("new-comment-text-content");
  var newComment = prompt();

  comment.innerHTML = newComment;
}

function change_erase() {
  var comment = document.getElementById("new-comment-text-content");
  var initialComment = "댓글 추가...";

  comment.innerHTML = initialComment;
}

document
  .querySelector("#reply-comment-click-test")
  .addEventListener("click", () => {
    var reply = document.getElementById("reply-comment-click-test");
    var currentReply = reply.innerHTML;

    if (currentReply === "▽ 답글 1개") {
      reply.innerHTML = "△ 답글 1개";
    } else if (currentReply === "△ 답글 1개") {
      reply.innerHTML = "▽ 답글 1개";
    }
  });

let reply_do = false;
document.querySelector(".reply-comment").style.display = "none";

document
  .querySelector("#reply-comment-click-test")
  .addEventListener("click", () => {
    var replyComment = document.querySelector(".reply-comment");

    if (reply_do) {
      replyComment.style.display = "none";
      reply_do = false;
    } else {
      replyComment.style.display = "flex";
      reply_do = true;
    }
  });
