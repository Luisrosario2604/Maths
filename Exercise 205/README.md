# Project Mathematics 205

Name : 205 IQ

## Requirement

Language : Python3

No package needed

## Usage

```
> ./205Iq.py u s [IQ1] [IQ2]

DESCRIPTION
    u       mean
    s       standar deviation
    IQ1     minimum IQ
    IQ2     maximum IQ
```

## Example

```
> ./205Iq.py 100 15 > data
> head -n 2 data
0 0.00000
1 0.00000
> head -n 120 data | tail -n 10
110 0.02130
111 0.02033
112 0.01931
113 0.01827
114 0.01721
115 0.01613
116 0.01506
117 0.01399
118 0.01295
119 0.01192
> tail -n 2 data
199 0.00000
200 0.00000
```
```
> ./205Iq.py 100 24 90
33.8% of people have an IQ inferior to 90
```
```
> ./205Iq.py 100 24 90 95
7.9% of people have an IQ between 90 and 95
```

## Grade
For this project i had the score of 18.5 out of 20 

18.5/20

## Year

This project was done in 2019

## License
Project from [EPITECH](https://www.epitech.eu/) school made by Luis ROSARIO
