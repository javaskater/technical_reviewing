var nameIdObject = { name: "my Name", id: 1, print: function () { } };
nameIdObject = { id: 2, name: "another Name", print: function () { console.log("".concat(this.id, " - ").concat(this.name)); } };
nameIdObject.print();
nameIdObject = { id: 3, name: "Third Name" };
