*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/HyperArray.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class HyperArray

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.HyperArray

All Implemented Interfaces:
:   `Serializable`

---

```
public class HyperArray
extends Object
implements Serializable
```

A storage for multi-dimensional data used primarily in system dynamics
models. Each data element is of Java type double. This construct (also
known as "data with subscripts" or "array") allows for easy and intuitive writing
of formulas and equations, and flexible manipulating with dimensions.
Arithmetic operations on arrays are performed element-by-element (unlike
on matrixes in linear algebra).

Hyper arrays are constructed by specifying their dimensions and, optionally,
the initial data, for example:
`people = HyperArray( Region, Gender, AgeGroup );` or
`people = HyperArray( initialPeople, Region, Gender, AgeGroup );`
where Region, Gender, ... are objects of class Dimension
may contain e.g. the population of a country broken down by region, gender
and age group.

You can set and get values of individual elements of the hyper array by
calling the corresponding methods, e.g:
`people.get( NORTH, MALE, ADULT )` or
`people.set( 23000, NORTH, MALE, ADULT )`

The class also supports calculations over a subsets of elements, like
sum, product, minimum or maximum. For example, calling:
`people.sum( NORTH, INDEX_CAN_VARY, ADULT )`
will calculate the number of adults of both genders in the north region.

The multi-dimensional data is stored in a flat array so that the first
dimension index varies first. Thus, for a hyper array [ Region, Gender ]
where Region is { N, S, E, W } and Gender is { M, F }, the flat data array woould
contain: [ (N,M), (S,M), (E,M), (W,M), (N,F), (S,F), (E,F), (W,F) ].
Position of an element with particular indexes can be obtained by
calling getPosOf( indexes... ).

An object of class HyperArray occupies 14 + ( 8 \* Number of dimensions ) +
( 8 \* Product of sizes of all dimensions ) bytes of memory.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.HyperArray)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final int` | `INDEX_CAN_VARY` | A special constant that, being placed at an index position, tells the methods that perform operation over subsets of hyper array elements that they can vary the corresponding index. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `HyperArray(double[] values, Dimension... dims)` | Creates a hyper array with the dimensions specified and initializes it with the given values from a flat array, where the first dimension index varies first. |
| `HyperArray(double value, Dimension... dims)` | Creates a hyper array with the dimensions specified and initializes all its elements with the same value. |
| `HyperArray(Dimension... dims)` | Creates a hyper array with the dimensions specified. |
| `HyperArray(HyperArray original)` | Creates a copy of a given hyper array. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `average()` | Returns the average of all elements of the hyper array. |
| `void` | `copyFrom(HyperArray original)` | Copies all data from another hyperarray. |
| `void` | `decrement(int... indexes)` | Decrements (-1) element(s) with the given index(es). |
| `void` | `decrementBy(double value, int... indexes)` | Decrements value(s) of given element(s) by the given value. |
| `boolean` | `equal(double val)` | Checks if all elements of the hyper array equal a particular value. |
| `boolean` | `equal(HyperArray a)` | Compares the hyper array with another one. |
| `double` | `get(int... indexes)` | Returns the value of the element of this array specified by the given dimension indexes. |
| `double[]` | `getData()` | Returns the flat array of doubles holding the hyper array elements. |
| `Dimension[]` | `getDimensions()` | Returns the dimensions of the hyper array. |
| `int` | `getPosOf(int... indexes)` | Returns the position of the element in the flat data array specified by the given dimension indexes. |
| `boolean` | `hasNegativeValues()` | Checks if there are any negative elements in the hyper array. |
| `void` | `increment(int... indexes)` | Increments value(s) of given element(s) by 1. |
| `void` | `incrementBy(double value, int... indexes)` | Increments value(s) of given element(s) by the given value. |
| `double` | `max()` | Returns the maximum of all elements of the hyper array. |
| `double` | `max(int... indexes)` | Returns a partial maximum of hyper array elements, namely maximum across all dimensions whose indexes equal INDEX\_CAN\_VARY in the given index array. |
| `double` | `min()` | Returns the minimum of all elements of the hyper array. |
| `double` | `min(int... indexes)` | Returns a partial minimum of hyper array elements, namely minimum across all dimensions whose indexes equal INDEX\_CAN\_VARY in the given index array. |
| `void` | `multiply(double factor, int... indexes)` | Multiplies element(s) with the given index(es) by the given `factor`. |
| `double` | `prod()` | Returns a product of all hyper array elements. |
| `double` | `prod(int... indexes)` | Returns a partial product of hyper array elements, namely product across all dimensions whose indexes equal INDEX\_CAN\_VARY in the given index array. |
| `void` | `set(double value)` | Sets all elements of this array to a given value. |
| `void` | `set(double[] values)` | Sets the hyper array elements to the values from a given array, where the first dimension index varies first. |
| `void` | `set(double value, int... indexes)` | Sets the element of this array specified by the dimension indexes to a given value. |
| `void` | `setData(double[] values, int srcPos)` | Sets the hyper array elements to the values from a given array starting from the specified position, where the first dimension index varies first. |
| `int` | `size()` | Returns the total number of elements in the hyper array. |
| `double` | `stddev()` | Returns the standard deviation across all elements of the hyper array. |
| `double` | `sum()` | Returns the sum of all elements of the hyper array. |
| `double` | `sum(int... indexes)` | Returns a partial sum of hyper array elements, namely sum across all dimensions whose indexes equal INDEX\_CAN\_VARY in the given index array. |
| `String` | `toString()` | Prints out the hyper array in the following form:  - if the hyper array is dimensionless, just prints its only element value  - for a uni-dimensional hyper array prints every element value on a separate line  - for two-dimensional hyper array prints as a tab separated 2D table with element values (dimension 0 vs dimension 1)  - for three and more dimensions prints a number of such tables, a table for each combination of indexes in dimensions 2 and higher. |
