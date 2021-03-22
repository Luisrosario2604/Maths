# Project Mathematics 106

Name : 106 Bombyx

## Requirement

Language : C

No package needed

## Compiling

######Go in the project directory

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
> ./106bombyx n [k | i0 i1]

DESCRIPTION
    n   number of first generation individuals
    k   growth rate from 1 to 4
    i0  initial generation (included)
    i1  final generation (included)
```

## Example

```
> ./106bombyx 10 3.3 > data

> head data
1 10.00
2 32.67
3 104.29
4 308.26
5 703.68
6 688.10
7 708.24
8 681.89
9 715.82
10 671.29
> tail data
91 823.60
92 479.43
93 823.60
94 479.43
95 823.60
96 479.43
97 823.60
98 479.43
99 823.60
100 479.43
```

```
> ./106bombyx 10 10000 10010 > data

> head -n 30 data
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.00 0.10
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.01 9.90
1.02 19.61
1.02 19.61
1.02 19.61
1.02 19.61
1.02 19.61
1.02 19.61
1.02 19.61
1.02 19.61
```
## Grade
For this project i had the score of 14.3 out of 20 

14.3/20

## Year

This project was done in 2018

## License
Project from [EPITECH](https://www.epitech.eu/) school made by Luis ROSARIO
