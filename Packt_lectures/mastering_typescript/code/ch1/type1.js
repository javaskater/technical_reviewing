var myBoolean = true;
var myNumber = 1234;
var myStringArray = ["first:".concat(myNumber), "second", "third"];
myBoolean = myNumber == 456;
myStringArray = [myNumber.toString(), "5678"];
myNumber = myStringArray.length;
console.log("myBoolean = ".concat(myBoolean));
console.log("myStringArray = ".concat(myStringArray));
console.log("myNumber = ".concat(myNumber));
