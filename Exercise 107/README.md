# Project Mathematics 107

Name : 107 Transfer

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
> ./107transfer [num den]*

DESCRIPTION
    num     polynomial numerator defined by its coefficients
    den     polynomial denominator defined by its coefficients
```

## Example

```
> ./107transfer "0*1*2*3*4" "1" > file

> head -n 12 file
0.000 -> 0.00000
0.001 -> 0.00100
0.002 -> 0.00201
0.003 -> 0.00302
0.004 -> 0.00403
0.005 -> 0.00505
0.006 -> 0.00607
0.007 -> 0.00710
0.008 -> 0.00813
0.009 -> 0.00916
0.010 -> 0.01020
0.011 -> 0.01125
> tail file
0.991 -> 9.73282
0.992 -> 9.76223
0.993 -> 9.79171
0.994 -> 9.82126
0.995 -> 9.85087
0.996 -> 9.88056
0.997 -> 9.91031
0.998 -> 9.94014
0.999 -> 9.97003
1.000 -> 10.00000
```

```
> ./107transfer "0*0*9" "1*3*5" "2*4*6" "8*8*8"> file

> head file
0.000 -> 0.00000
0.001 -> 0.00000
0.002 -> 0.00001
0.003 -> 0.00002
0.004 -> 0.00004
0.005 -> 0.00006
0.006 -> 0.00008
0.007 -> 0.00011
0.008 -> 0.00014
0.009 -> 0.00018
```
## Grade
For this project i had the score of 16 out of 20 

16/20

## Year

This project was done in 2018

## License
Project from [EPITECH](https://www.epitech.eu/) school made by Luis ROSARIO
