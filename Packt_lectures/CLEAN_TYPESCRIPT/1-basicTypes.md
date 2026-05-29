# 43

- My Corporate VSCodium makes typescript completion, linting and error signaling (checking types)
  - and it gives you th Ts error code (232 for example)
  - seems to be no special extension needed see this [TypeScript Tutorial on VSCode](https://code.visualstudio.com/docs/typescript/typescript-tutorial)

## my first program

```typescript
type Person = {
  name: string;
  age: number;
  greet: () => void;
};

const persons: Person[] = [
  {
    name: "Alice",
    age: 30,
    greet() {
      //the object stays red underlined until I define greet
      console.log(`Hello my name is ${this.name} and I am ${this.age} old`);
    },
  },
  {
    name: "Bob",
    age: 25,
    greet() {
      console.log(`Hello my name is ${this.name} and I am ${this.age} old`);
    },
  },
];

persons.forEach((p) => p.greet()); //like in J§avascript
```

- When I compile + run this program

```bash
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ npx tsc
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ node index.js
Hello my name is Alice and I am 30 old
Hello my name is Bob and I am 25 old
```
