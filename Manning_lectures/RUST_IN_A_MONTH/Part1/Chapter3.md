# p 64

* We cannot add a *b* to five *a*
  * the compiler does not accept
```rust
let my_array = ["a";5, "b"];
```

* The follwing code creates a u8 array of length 11
```rust
fn main() {
   let word = b"Hello there";
   println!("{:?}", word);
}
```

* The slice is a [reference](https://linuxhint.com/rust-slices/) to a memory slice (with a beginning and an end)
```rust
fn main() {
   let array_of_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
   let two_to_five = &array_of_ten[2..5]; //second position inclusive, Fifth position exclusive
   let and_at_five = &array_of_ten[..=5]; //Fifth position inclusive
   let everything = &array_of_ten[1..];
   println!("Two to five {:?}", two_to_five);
   println!("End at five {:?}", and_at_five);
   println!("everything {:?}", everything);
}
```

