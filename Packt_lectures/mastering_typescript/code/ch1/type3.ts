var nameIdObject = { name: "my Name", id: 1, print(){}};
nameIdObject = {id: 2, name: "another Name", print(){console.log(`${this.id} - ${this.name}`)}};
nameIdObject.print();
nameIdObject = {id: 3, name: "Third Name"};