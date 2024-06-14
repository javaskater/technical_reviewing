var myBoolean: boolean = true;
var myNumber: number = 1234;
var myStringArray: string[] = [`first:${myNumber}`, `second`, `third`];
myBoolean = myNumber == 456;
myStringArray = [myNumber.toString(), `5678`];
myNumber = myStringArray.length;

console.log(`myBoolean = ${myBoolean}`);
console.log(`myStringArray = ${myStringArray}`);
console.log(`myNumber = ${myNumber}`);