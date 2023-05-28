const toggle_btn_down = document.querySelector("#toggle-btn-down");
const toggle_btn_up = document.querySelector("#toggle-btn-up");
const recomment = document.querySelector(".recomment");
const comment_box = document.querySelector(".comment-box");

document.querySelector("#toggle-btn-down").addEventListener("click", () => {
  show();
});

function show() {
  recomment.style.display = "flex";
  toggle_btn_down.style.display = "none";
  toggle_btn_up.style.display = "block";
}

document.querySelector("#toggle-btn-up").addEventListener("click", () => {
  hide();
});

function hide() {
  recomment.style.display = "none";
  toggle_btn_down.style.display = "block";
  toggle_btn_up.style.display = "none";
}

document.querySelector("#btn-clear").addEventListener("click", () => {
  clear();
});

function clear() {
  comment_box.value = null;
}

document.querySelector("#btn-show").addEventListener("click", () => {
  show_msg();
});

function show_msg() {
  alert(comment_box.value);
}
