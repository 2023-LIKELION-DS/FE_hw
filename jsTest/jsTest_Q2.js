let age = prompt("나이를 입력하세요.");
let welcome = (wel_age) => {
  wel_age < 20 ? alert(wel_age + " : 미성년자") : alert(wel_age + " : 성인");
  console.log(wel_age);
};

welcome(age);
