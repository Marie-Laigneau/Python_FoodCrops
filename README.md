# Python FoodCrops
Python project at Mines d'Alès
## Environment
Developed and tested with Python-3.7.3
System: Debian GNU/Linux 10 (Buster) x86_64
## Execution
To run the program
```
$ ./run
```
or
```
$ python3 main.py
```

Then you'll be prompt to enter the option. There are 3 options available: help, exit, filter.
To quit the program, enter 'exit' (without quotation marks).
Enter 'filter', you'll be directed to a command-line menu, where the criterion are requested.

Example below:

```
$ ./run
Enter csv file path: YOURCSVFILEPATH
Enter your option: filter
Which commodity group? Enter 'N' for None: N
...

```
## Groupwork
We seperate the task into 5 parts:
1. Creating basic classes such as Unit, Commodity, Indicator, etc (Zian LI & Romain Grosse)
2. Implementing FoodCropFactory class which handles the creation of the basic classes (Hugo Roch & )
3. Implementing FoodCropsDataset class which handles the reading and filtering (Marie Laigneau & )
4. Creating main.py for merging everything under the user interface (Zian LI & )
5. Summary and documentation (Zian LI & Marie Laigneau)

In principle, the seperation of work is as above.
In reality, due to the the different skills of each member, we help and correct each other's part too.
We have intensively used git for controlling the development process and for correcting each others' codes.

## Difficulties
There are several difficulties during the development process:
1. Difficulties in understanding the diagram
- Solved: in the course "Requirements", references were provided, thus the problem has been solved once we understood the diagram.
2. Difficulties with the filtering algorithm (cannot merge the list according to the correct index)
- When reading each keywork in the csv file, the content and the index should be processed at the same time
- The index should be well kept when applying intersection, otherwise the order would be wrong, so does the result 
3. Large input data takes long time to run
- Solved: Cut out some lines from the original csv in order to speed up the test
4. Implementing the descriptor interface
- This problem happens because of our poor understanding of abstract method, as well as python decorator syntax

## Conclusion
This project aims to implement a program for analysing corps statistics. 
It provides an interface between the database and corresponding Python classes.
The user is able to view the resulting measurement corresponding to the criterion selected.

## Bonus
Version 2 (in constant development) :
https://github.com/Leethine/Python_FoodCrops

