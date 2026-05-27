*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesArray.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class UtilitiesArray

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.UtilitiesArray

---

```
public final class UtilitiesArray
extends Object
```

This class provides a lot of commonly used functions for operations with arrays

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static boolean` | `arrayContains(double[] array, double value)` | Returns `true` if the array contains the given value.  The result is the same as from expression: `indexOf( array, value ) >= 0` |
| `static boolean` | `arrayContains(int[] array, int value)` | Returns `true` if the array contains the given value.  The result is the same as from expression: `indexOf( array, value ) >= 0` |
| `static boolean` | `arrayContains(Object[] array, Object object)` | Returns `true` if the array contains the given object.  Objects are compared using `.equals()` method.  Arrays of any object type are supported, e.g.: |
| `static <T> T[]` | `concatenateArrays(T[] a, Collection<? extends T> b)` | Concatenates specified array with elements from the given collection.  Result is new array with contents of `a` followed by all other elements (`b`) |
| `static <T> T[]` | `concatenateArrays(T[] a, T... b)` | Concatenates specified array with the given elements.  Result is new array with contents of `a` followed by all other elements (`b`) |
| `static <T> T[]` | `concatenateArrays(T[] a, T[]... b)` | Concatenates specified array with the given elements.  Result is new array with contents of `a` followed by all other elements (`b`) |
| `static int` | `indexOf(double[] array, double value)` | Returns the index of the first occurrence of the given value in the array.  Returns `-1` if value not found or if passed `array` is `null` or empty. |
| `static int` | `indexOf(double[] array, DoublePredicate test)` | Returns the index of the first occurrence of the matching value in the array.  Returns `-1` if no matching value is found or if passed `array` is `null` or empty. |
| `static int` | `indexOf(int[] array, int value)` | Returns the index of the first occurrence of the given value in the array.  Returns `-1` if value not found or if passed `array` is `null` or empty. |
| `static int` | `indexOf(int[] array, IntPredicate test)` | Returns the index of the first occurrence of the matching value in the array.  Returns `-1` if no matching value is found or if passed `array` is `null` or empty. |
| `static int` | `indexOf(Object[] array, Object object)` | Returns the index of the first occurrence of the given object in the array.  Objects are compared using `.equals()` method.  Returns `-1` if value not found or if passed `array` is `null` or empty.  Arrays of any object type are supported, e.g.: |
| `static <T> int` | `indexOf(T[] array, Predicate<? super T> test)` | Returns the index of the first occurrence of the matching object in the array.  Returns `-1` if value not found or if passed `array` is `null` or empty.  Arrays of any object type are supported, e.g.: |
| `static int` | `indexOfMax(double[] array)` | Returns the index of the maximum value from the given array. |
| `static int` | `indexOfMax(int[] array)` | Returns the index of the maximum value from the given array. |
| `static int` | `indexOfMin(double[] array)` | Returns the index of the minimum value from the given array. |
| `static int` | `indexOfMin(int[] array)` | Returns the index of the minimum value from the given array. |
| `static double` | `max(double[] array)` | Returns the maximum value from the given array.  Returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") if array contains only [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") values.  Throws error if passed `array` is `null` or empty. |
| `static int` | `max(int[] array)` | Returns the maximum value from the given array.  Throws error if passed `array` is `null` or empty. |
| `static double` | `min(double[] array)` | Returns the minimum value from the given array.  Returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") if array contains only [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") values.  Throws error if passed `array` is `null` or empty. |
| `static int` | `min(int[] array)` | Returns the minimum value from the given array.  Throws error if passed `array` is `null` or empty. |
| `static <T> T[]` | `toArray(T e, T... b)` | Creates array using concatenation of the specified element with given array/elements. |
