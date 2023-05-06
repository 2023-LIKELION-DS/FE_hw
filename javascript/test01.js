/*document.write("<p>JavaScript는 재밌어:)</p>");

var num;
num = 10;

var num = 10;
num = 20;
console.log(num);

var price = 10000;
console.log(price);

var myname = "테킷";
console.log(myname);
var myname2 = "멋사";
console.log(myname2);
var myname3 = "'멋쟁이'";
console.log(myname3);
var myname4 = '"사자"';
console.log(myname4);

var isTrue = true;
console.log(isTrue);
var isFalse = false;
console.log(isFalse);

var a;
console.log(a);

var student = {
  grade: 1,
  school: "lion school",
};
console.log(student);
console.log(typeof student);

var gradeInfo = student.grade;
console.log(gradeInfo);

var key = Object.keys(student)[0];
console.log(key);

student.class = 3;
console.log(student);
console.log(student["class"]);
console.log(student.class);

var teacher = new Object();
var teacher = {};

var name1 = "김멋사";
var name2 = "김멋사";
console.log(name1 == name2);
var name3 = symbol("이테킷");
var name4 = symbol("이테킷");
console.log(name3 == name4);
var myclass = {
  [symbol("이테킷")]: 1,
  [symbol("이테킷")]: 2,
};

var a = 10;
var b = 3;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a);
console.log(b);

var c = 7;
console.log(++c);
console.log(c++);
console.log(c);
console.log(--c);
console.log(c--);
console.log(c);

var d = 2;
d = 10;
console.log(d);

console.log((d += 3));
console.log((d -= 3));
console.log((d *= 3));
console.log((d /= 3));
console.log((d %= 3));

console.log(2 == 2);
console.log(2 == "2");
console.log(2 === "2");
console.log(2 != 2);
console.log(2 != "2");
console.log(2 !== "2");
console.log(4 > 2);
console.log(4 < 2);
console.log(4 >= 2);
console.log(4 <= 2);

console.log(true || true);
console.log(true || false);
console.log(true || false || false);
console.log(false || false);
console.log(2 > 3 || 5 == 5);
console.log(true && true);
console.log(true && false);
console.log(true && false && false);
console.log(false && false);
console.log(2 > 3 && 5 == 5);
console.log(2 < 3 && 5 == 5);
console.log(!true);
console.log(!false);
console.log(!(5 > 4));

console.log(typeof 1);
console.log(typeof "1");
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof symbol());
console.log(typeof null);

var greeting = "Hello!";
var farewell = "Bye!";
var myname = "김테킷";
var sentence = greeting + myname;
console.log(sentence);
var sentence = greeting + " " + myname;
console.log(sentence);
var sentence = greeting + "\n" + myname;
console.log(sentence);
console.log(farewell + 2);

var sentence = greeting + "\n" + myname;
console.log(sentence);
var sentence = greeting + "\t" + myname;
console.log(sentence);
var sentence = greeting + "'" + myname;
console.log(sentence);
var sentence = greeting + '"' + myname;
console.log(sentence);
var sentence = greeting + "\\" + myname;
console.log(sentence);

var a = "안녕하세요!";
console.log(a);
var a = "안녕하세요! 여러분:)";
console.log(a);

var price = 1000;
var b = "이 물건은 " + price + "원 입니다.";
console.log(b);

var c = "이 물건은 ${price}원 입니다.";
console.log(c);

var d = "이 물건은 ${200 + 450}원 입니다.";
console.log(d);

var abc = "I am Iron man";
console.log(abc.indexOf("man"));
console.log(abc.indexOf("I"));

console.log(abc.slice(0, 3));
console.log(abc.slice(0, 4));

console.log(abc.toUpperCase());
console.log(abc.toLowerCase());

var efg = "This is my car.";
console.log(efg.startsWith("Th"));
console.log(efg.startsWith("th"));

console.log(efg.startsWith("car"));

console.log(efg.includes("is"));

var mbti = ["INFP", "ENFJ", "INTJ"];
console.log(mbti[0]);
console.log(mbti.length);

mbti[3] = "ESFP";
console.log(mbti[3]);
console.log(mbti.length);

mbti[2] = "ISTJ";
console.log(mbti[2]);

console.log(mbti.push("ESFP", "ISTJ"));

var newMbti = [...mbti, "ESFP", "ISTJ"];
console.log(mbti);
console.log(newMbti);

console.log(mbti.pop());
console.log(mbti);

console.log(mbti.unshift("ESFP", "ISTJ"));
console.log(mbti);
var newMbti = ["ESFP", "ISTJ", ...mbti];
console.log(mbti);
console.log(newMbti);

console.log(mbti.shift());
console.log(mbti);

console.log(mbti.slice(0, 2));
console.log(mbti.slice());
console.log(mbti.slice(-1));

console.log(mbti.join());
console.log(mbti.join("-"));
console.log(mbti.join("|"));
console.log(mbti.join(""));

console.log(mbti.sort());
console.log(mbti.sort().reverse());

var a = 5;
if (a > 2) {
  console.log("a > 2");
} else {
  console.log("a <= 2");
}

var a = 2;
if (a > 2) {
  console.log("a > 2");
} else {
  console.log("a <= 2");
}

var a = 2;
if (a > 2) {
  console.log("a > 2");
} else if (a == 2) {
  console.log("a == 2");
} else if (a == 0) {
  console.log("a == 0");
} else {
  console.log("a < 2");
}

var mbti = "INFP";
var val;
switch (mbti) {
  case "INFP":
    val = "INFP";
    break;
  case "ENFP":
    val = "ENFP";
    break;
  case "ISTJ":
    val = "ISTJ";
    break;
  default:
    val = "유효한 값이 아닙니다.";
}
console.log(val);

for (var i = 0; i < 10; i++) {
  console.log(i);
}

for (var i = 10; i > 0; i--) {
  console.log(i);
}

for (var i = 0; i < 10; i++) {
  for (var j = 0; j < 10; j++) {
    console.log("${i}-${j}");
  }
}

var flag = 10;
while (flag > 0) {
  console.log(flag);
  flag--;
}

var flag = 10;
do {
  console.log(flag);
  flag--;
} while (flag > 0);

try {
  myfunc();
} catch (error) {
  console.log("에러 발생");
} finally {
  console.log("무조건 실행");
}

try {
  throw new Error("에러");
} catch (error) {
  console.log("에러 발생");
  console.log(error);
} finally {
  console.log("무조건 실행");
}
*/
