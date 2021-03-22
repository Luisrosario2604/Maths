# Project Mathematics 102

Name : 102 Architect

## Requirement

Language : Python

No package needed

## Usage

```
> ./102architect.py x y transfo1 arg11 [arg12] [transfo2 arg12 [arg22]] ...

DESCRIPTION
    x       abscissa of the original point
    y       ordinate of the original point
    
    transfo arg1 [arg2]
    -t i j  translation along vector (i, j)
    -z m n  scaling by factors m (x-axis) and n (y-axis)
    -r d    rotation centered in O by a d degree angle
    -s d    reflection over the axis passing through O with an inclination
angle of d degrees

```

## Example

```
> ./102architect.py 1 2 -t 2 3 -z 1 -2 -r 45 -s 30

Translation by the vector (2, 3)
Scaling by factors 1 and -2
Rotation at a 45 degree angle
Symmetry about an axis inclined with an angle of 30 degrees
0.97     -0.52     0.38
0.26     1.93     6.31
0.00     0.00     1.00
(1.00, 2.00) => (0.31, 10.44)
```

## Grade
For this project i had the score of 19.8 out of 20 

19.8/20

## Year

This project was done in 2017

## License
Project from [EPITECH](https://www.epitech.eu/) school made by Luis ROSARIO
