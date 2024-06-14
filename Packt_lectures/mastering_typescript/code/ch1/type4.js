var obj1 = { id: 1, print: function () { } };
var obj2 = { id: 2, print: function () { }, select: function () { } };
obj1 = obj2;
console.dir(obj1);
obj2 = obj1;
console.dir(obj2);
