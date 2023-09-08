# Project Mathematics 103

Name : 103 Cipher

## Requirement

Language : C

No package needed

## Compiling

###### Go in the project directory

Clean (*.o files)
```
> make clean
```

Full clean (*.o and binary file)
```
> make fclean
```

Compile
```
> make
```

Full clean and compile
```
> make re
```

Compile with gdb (debugging)
```
> make gdb
```

## Usage

```
> ./103cipher message key flag

DESCRIPTION
    message a message, made of ASCII characters
    key     the encryption key, made of ASCII characters
    flag    0 for the message to be encrypted, 1 to be decrypted
```

## Example

```
> ./103cipher "Just because I don’t care doesn’t mean I don’t understand." "Homer S" 0

Key matrix :
72         111        109
101        114        32
83         0          0

Encrypted message :
26690 21552 11810 19718 16524 13668 25322 22497 14177 28422 26097 16433 12333 11874 5824 27541 23754 14452 -23637 -17922 -7366 19801 16524 13668 26881 23763 14221 21617 14952 6688 28017 24321 14689 -23637 -17922 -7366 20631 16524 13668 26199 22269 14113 12333 11874 5824 27541 23754 14452 -23637 -17922 -7366 21295 16524 13668 26403 23610 15190 29451 25764 16106 26394 23307 14093 3312 5106 5014
```

```
> ./103cipher "26690 21552 11810 19718 16524 13668 25322 22497 14177 28422 26097 16433 12333 11874 5824 27541 23754 14452 17180 17553 7963 26387 22047 13895 18804 14859 12033 27738 23835 15331 21487 16656 13238 21696 15978 6976 20750 23307 14093 16788 11751 8981 22339 24861 15619 21295 16524 13668 26403 23610 15190 29451 25764 16106 26394 23307 14093 3312 5106 5014" "Homer S" 1

Key matrix :
0.0      0.0      0.012
-0.004  0.012   -0.012
0.013   -0.013  0.004

Decrypted message :
Just because I don't care doesn't mean I don't understand.
```

## Grade

I scored 17.2 out of 20 for this project

17.2/20

## Year

This project was done in 2017

## Authors

* **Luis Rosario** - *Member 1* - [Luisrosario2604](https://github.com/Luisrosario2604)
