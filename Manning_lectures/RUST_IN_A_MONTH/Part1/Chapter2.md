## page 47
### 2.5
* The problem appends only if the immutable reference
  * is declared or used
  * __after__ the mutable reference has been declared
```rust
fn main() {
    let mut number = 10;
    let number_change = &mut number;
    let num_ref = &number; //non mutable reference to my_number won't be accepted beacause the mutable reference has already been decalred
    *number_change += 10;
    println!("{}", number_change);
}
```
_the compiler is smarter than it used to be. It can understand not just what we type, but when and how we use (most) everything._

## 2.7

* how to give back the variable owned by the function
  * don't forget to indicate that the function returns a String
```rust
fn print_country(country_name:String) -> String{
    println!("[print_country] - {country_name}");
    country_name
}

fn main(){
    let country = String::from("Austria");

    let country2 = print_country(country);
    print_country(country2);
}
```
* (only way to attribute the possession of the variable to a new variable) ?
  * this does not pass the compilation phase because _value borrowed here after move_
```rust
fn main(){
    let country = String::from("Austria");
    let country2 = country;
    println!("{}", country2);
    println!("{}", country);

}
```

* With a reference _function can only view the data but never takes ownership_

* [references and mutable references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#mutable-references) in RUST

## page 51
* __So adds_hungary can take country as mutable (because it owns it), and it is perfectly safe to do so - nobody else owns it__
```rust
fn add_hungary(mut string_to_add_hungary_to: String) {
    string_to_add_hungary_to.push_str("-Hungary");
    println!("[add_hungary] Now it says: {}", string_to_add_hungary_to);
}

fn main(){
    let country = String::from("Austria");
    add_hungary(country);
    //println!("[main] the country is {}", country); // will output an error because country is owned bay the function

}
```

##  p 54/546 playing with ref
* a reference does not consume the original variable
  * you only may not uncomment the last line because _borrow later used here_
  * the ref has been taken (used) by the function which now owns it
```rust
fn prints_country(country: String) {

    println!("[prints_country] Now it says: {}", country);
}
fn prints_country_ref(country_ref: &String) {

    println!("[prints_country-ref] Now it says: {}", *country_ref);
}

fn main(){
    let mut country_main = String::from("Kiribati");
    let country_main_ref = &country_main;
    prints_country(country_main.clone());
    prints_country_ref(country_main_ref);
    country_main = format!("{}-{}", country_main, "Hello");
    prints_country(country_main.clone());
    //prints_country(country_main);
    //prints_country_ref(country_main_ref);

}
```
### last code
* note about reference, you don't have unreference it to call a funtion on String...
* the function __split_whitespace()__ applies to String, or to references of a String...

## page 57/546
* playing with raw strings:
```rust
fn main() {
    let my_string = "'Ice to see you,' he said.";
    let quote_string = r#""Ice to see you," he said"#;
    let hashtag_string = r##"The hashtag "#IceToSeeYou" had become very popular."##;
    let many_hashtags = r####"You don't have to type "###" to use a hashtag. Tou can just use #."####;
    println!("{}\n{}\n{}\n{}", my_string, quote_string, hashtag_string,many_hashtags);
}
```
### printing and debugging
* It is by [using the ?](https://stackoverflow.com/questions/38157335/what-does-mean-in-a-rust-format-string)
  * printing a string in binary format can only be done in _Debug mode_
  * for debugging a raw string it must be _br_: you have to define the raw string first !!!
### Hex Codes of UTF chars:
* it works !!!
```rust
fn main() {
    println!("{:X}", '행' as u32);
    println!("{:X}", 'H' as u32);
    println!("{:X}", '居' as u32);
    println!("{:X}", 'い' as u32);
    //The following command effectively prints korean and chinese characters
    println!("\u{D589} \u{48} \u{5C45} \u{3044}");
}
```
## p58/546
* the variable _number_ does not implement the pointer trait so the only way to display the adress of a variable is through its pointer
  * both lines print the same result...
```rust
fn main() {
    let number = 9;
    let number_ref = &number;
    println!("The pointer address is {:p}", number_ref);
    println!("The variable address is {:p}", &number);
}
```
* using the same variable/position in many formats
```rust
fn main() {
    let number = 555;
    println!("Binary {0:b}, hexadecimal {0:x}, octal {0:o}", number);
}
```
## pa 60/546
* for special padding chars you can also use the UTF8 code
```rust
fn main() {
    let letter:char = 'a';
    println!("{:ᄒ^11.15}", letter);
    println!("{:\u{D589}^11.15}", letter);
}
```