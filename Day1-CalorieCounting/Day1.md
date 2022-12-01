# [Day 1: Calorie Counting](https://adventofcode.com/2022/day/1)

## Solution

### Part 1

was just basic programming, read in a file summarise the list of values, find greatest sum

### Part 2

---

## Reflection

*was pretty easy*, just had to learn how to use python again which was just `file`, `list`, & `dict` comprehension

**however...**

i feel like my approach to the solution isnt the most efficient, and it might come back to bite me in the ass as the questions complexity increases and i have to reuse this code

i feel like i should go back and study dynamic programming algorithms and brush up on my regex...

---

## Extra

after submitting i replaced this function:

```python
def count_calories(inputList):
    caloriesDict = {}

    for i, val in enumerate(inputList):
        caloriesDict.update({ i+1: sum(val) })

    return caloriesDict
```

with this:

```python
def count_calories(inputList):
    return dict([ (k+1, sum(v)) for k, v in enumerate(inputList) ])
```

why?

idk