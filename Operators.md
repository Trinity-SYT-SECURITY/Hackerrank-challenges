**Objective**

In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

**Task**

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

**Example**

+ mealcost = 100
+ tippercent = 15
+ taxpercent = 8

A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value `123` and return from the function.

**Function Description**

Complete the solve function in the editor below.

solve has the following parameters:

+ int meal_cost: the cost of food before tip and tax
+ int tip_percent: the tip percentage
+ int tax_percent: the tax percentage

Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

**Note**: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

**Input Format**

There are 3 lines of numeric input:

The first line has a double, `mealcost` (the cost of the meal before tax and tip).
The second line has an integer, `tippercent` (the percentage of `mealcost` being added as tip).

The third line has an integer, `taxpercent` (the percentage of `mealcost` being added as tax).

**Sample Input**

```
12.00
20
8
```

**Sample Output**

`15`

**Explanation**

Given:

`meal_cost = 12, tip_percent = 20, tax_percent = 8`

Calculations:

+ tip = 12 and 12/100 * 20 = 2.4
+ tax = 8 and 8/100 * 12 = 0.96

total_cost = meal_cost + tip + tax = 12 + 2.4 + 0.96 = 15.36

round(total_cost) = 15

We round `total_cost` to the nearest integer and print the result, `15`.