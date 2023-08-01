There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

**Example**

$strings = ['a','b','abc']$

$queries = ['ab','abc','bc']$

There are 2 instances of $ab'$, $1$ of $'abc'$ and 0 of $'bc'$. For each query, add an element to the return array, results = [2,1,0].

**Function Description**

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search

string queries[q] - an array of query strings

**Returns**

int[q]: an array of results for each query

**Input Format**

The first line contains and integer n, the size of strings[].

Each of the next n lines contains a string strings[i].

The next line contains q, the size of queries[].

Each of the next q lines contains a string queries[i].

**Constraints**

$1\leq n \leq 1000$

$1\leq q \leq 1000$

$1\leq |strings[i]|,|queries[i]| \leq20$


![image](https://github.com/Trinity-SYT-SECURITY/Hackerrank-challenges/assets/96654161/2e4c1726-3d91-4a0e-915c-b76a58b10073)

![image](https://github.com/Trinity-SYT-SECURITY/Hackerrank-challenges/assets/96654161/fed5697e-0756-431a-aaf5-8296fc0257c1)

![image](https://github.com/Trinity-SYT-SECURITY/Hackerrank-challenges/assets/96654161/7b1f2218-c0b9-4a7e-92fc-11ad3aac3634)
