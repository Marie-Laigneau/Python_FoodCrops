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
Enter csv file path: <span style="color: green">YOURCSVFILEPATH</span>
Enter your option: <span style="color: green">filter</span>
Which commodity group? Enter 'N' for None:
...

```
## Groupwork
We seperate the task into 5 parts:
1. Creating basic classes such as Unit, Commodity, Indicator, etc (Zian LI & Romain Grosse)
2. Implementing FoodCropFactory class which handles the creation of the basic classes (Hugo Roch &)
3. Implementing FoodCropsDataset class which handles the reading and filtering (Marie Laigneau &)
4. Creating main.py for merging everything under the user interface (Zian LI & )
5. Summary and documentation (Zian LI & Marie Laigneau)

In principle, the seperation of work is as above.
In reality, due to the development process and the different skills, we help or correct each other's part.

## Difficulties
There are several difficulties during the development process:
1. Difficulties in understanding the diagram
- Solution: in the course "Requirements", references were provided, thus the problem has been solved once we understood the diagram.
2. Difficulties with the filtering
3. ...


