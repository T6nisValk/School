# Competition task

Source file:
````
6
10 10 20 15 15 20
2 2 5 3 3 5
Ignas 12 22 0 10 12 17
Skirmantas 5 12 0 40 12 30
Milda 10 10 20 22 31 23
Asta 5 0 17 10 23 23
Rima 8 0 14 23 12 23
````
1. Amount of tasks in competition
2. Amount of time that is given for each task to be solved
3. Max amount of points for each task
4. Data of 5 participants:
- Name
- Amount of time in minutes that participant took to solve each task, 0 would show that participant did not solve or failed to solve the task.

Write a program, that will calculate the amount of points the participants collected, amount of correctly solved tasks and amount of time it took to solve these tasks.

Points:
- If participant solved the task correctly and within the time limit, he/she gets full points.
- If participant solved the task correctly but went over the time limit, he/she gets half of the points, rounding to healthy number eg. 3//2=1
- If participant did not solve the task, 0 points.

Result should be provided in a file, like this:

```
13
Milda 6 116
Ignas 5 73
Asta 5 78
Rima 5 80
```

1. The most points collected in competition
2. The list of participants who collected this amount of points
- Name, amount of correctly solved tasks, amount of time the participant took in minutes.
- The list sorted by the amount of correctly solved tasks going from high to low.