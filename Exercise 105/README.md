# Project Mathematics 105

Name : 105 Torus

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
> ./105torus opt a0 a1 a2 a3 a4 n

DESCRIPTION
    opt     method option:
            1 for the bisection method
            2 for Newton’s method
            3 for the secant method
    a[0-4]  coefficients of the equation
    n       precision (the application of the polynomial to the solution should be smaller than 10ˆ-n)
```

## Example

```
> ./105torus 1 -1 0 6 -5 1 6

x = 0.5
x = 0.75
x = 0.625
x = 0.5625
x = 0.53125
x = 0.515625
x = 0.523438
x = 0.519531
x = 0.521484
x = 0.522461
x = 0.522949
x = 0.522705
x = 0.522827
x = 0.522766
x = 0.522736
x = 0.522751
x = 0.522743
x = 0.522739
x = 0.522741
x = 0.522740
```

```
> ./105torus 3 -1 0 6 -5 1 8

x = 0.5
x = 0.52941176
x = 0.52274853
x = 0.52274000
x = 0.52274000
```

## Grade

I scored 13.5 out of 20 for this project

13.5/20

## Year

This project was done in 2017

## Authors

* **Luis Rosario** - *Member 1* - [Luisrosario2604](https://github.com/Luisrosario2604)
