# Project Mathematics 104

Name : 104 Intersection

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
> ./104intersection opt xp yp zp xv yv zv p 

DESCRIPTION
    opt             surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone
    (xp, yp, zp)    coordinates of a point by which the light ray passes through
    (xv, yv, zv)    coordinates of a vector parallel to the light ray
    p               parameter: radius of the sphere, radius of the cylinder, orangle formed by the cone and the Z-axis
```

## Example

```
> ./104intersection 1 0 0 2 1 1 0 1

Sphere of radius 1
Line passing through the point (0, 0, 2) and parallel to the vector (1, 1, 0)
No intersection point.
```

```
> ./104intersection 3 -1 -1 -1 1 1 5 30

Cone with a 30 degree angle
Line passing through the point (-1, -1, -1) and parallel to the vector (1, 1, 5)
2 intersection points:
(-1.568, -1.568, -3.842)
(-0.537, -0.537, 1.315)
```

## Grade

I scored 15.2 out of 20 for this project

15.2/20

## Year

This project was done in 2017

## Authors

* **Luis Rosario** - *Member 1* - [Luisrosario2604](https://github.com/Luisrosario2604)
