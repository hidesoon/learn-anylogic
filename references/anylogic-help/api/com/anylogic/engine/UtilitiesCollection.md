*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesCollection.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class UtilitiesCollection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.UtilitiesStream](UtilitiesStream.md "class in com.anylogic.engine")

com.anylogic.engine.UtilitiesCollection

---

```
public final class UtilitiesCollection
extends UtilitiesStream
```

This class provides a lot of commonly used functions for operations with collections / agent populations

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T> boolean` | `addAll(Collection<? super T> c, Collection<T> elements)` | Adds all of the elements in the specified collection to this collection. |
| `static <T> boolean` | `addAll(Collection<? super T> c, T... elements)` | Adds all of the specified elements to the specified collection. |
| `static double` | `average(Iterable<? extends Number> collection)` | Returns average value in the given collection with numbers. |
| `static <T> double` | `average(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns average value in the given collection.  Usage examples: |
| `static <T> double` | `averageWhere(Iterable<T> collection, ToDoubleFunction<? super T> value, Predicate<? super T> condition)` | Returns average of values in the given collection  among elements which meet the given condition.  Usage examples: |
| `static <T> int` | `count(Iterable<T> collection, Predicate<? super T> condition)` | Returns the number of elements/agents in the given collection which meet the given condition.  Usage examples: |
| `static <T> List<T>` | `filter(Iterable<T> collection, Predicate<? super T> condition)` | Returns new list with elements/agents from the original collection which meet the given condition.  Usage examples: |
| `static <T> List<T>` | `filter(T[] array, Predicate<? super T> condition)` | Returns new list with elements/agents from original array which meet the given condition.  Usage examples: |
| `static <T> List<T>` | `findAll(Iterable<T> collection, Predicate<? super T> condition)` | This function is the same as [`filter(Iterable, Predicate)`](#filter(java.lang.Iterable,java.util.function.Predicate)) |
| `static <T> List<T>` | `findAll(T[] array, Predicate<? super T> condition)` | This function is the same as [`filter(Object[], Predicate)`](#filter(T%5B%5D,java.util.function.Predicate)) |
| `static <T> T` | `findFirst(Iterable<T> collection, Predicate<? super T> condition)` | Returns the first element/agent from the given collection which meets the given condition.  Usage example: |
| `static <T> T` | `findFirst(T[] array, Predicate<? super T> condition)` | Returns the first element/agent from the given array which meets the given condition.  Usage example: |
| `static <T extends Comparable<? super T>> T` | `findMax(Iterable<T> collection)` | Returns 'maximum' element in the given collection according to [natural ordering](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang") (elements should be comparable).  If there are multiple elements which are the 'maximum', the first one is returned. |
| `static <T> T` | `findMax(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns element having maximum value in the given collection.  Usage examples: |
| `static <T extends Comparable<? super T>> T` | `findMin(Iterable<T> collection)` | Returns 'minimum' element in the given collection according to [natural ordering](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang") (elements should be comparable).  If there are multiple elements which are the 'minimum', the first one is returned. |
| `static <T> T` | `findMin(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns element having minimum value in the given collection.  Usage examples: |
| `static <T> int` | `indexOfFirst(Iterable<T> collection, Predicate<? super T> condition)` | Returns the index of the first element/agent from the given collection which meets the given condition.  Usage example: |
| `static <T> int` | `indexOfFirst(T[] array, Predicate<? super T> condition)` | Returns the index of the first element/agent from the given array which meets the given condition.  Usage example: |
| `static double` | `max(Iterable<? extends Number> collection)` | Returns maximum value in the given collection with numbers. |
| `static <T> double` | `max(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns maximum value in the given collection.  Usage examples: |
| `static <T> double` | `maxWhere(Iterable<T> collection, ToDoubleFunction<? super T> value, Predicate<? super T> condition)` | Returns maximum value of element in the given collection  among elements which meet the given condition.  Usage examples: |
| `static double` | `min(Iterable<? extends Number> collection)` | Returns minimum value in the given collection with numbers. |
| `static <T> double` | `min(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns minimum value in the given collection.  Usage examples: |
| `static <T> double` | `minWhere(Iterable<T> collection, ToDoubleFunction<? super T> value, Predicate<? super T> condition)` | Returns minimum value of element in the given collection  among elements which meet the given condition.  Usage examples: |
| `static <T> List<T>` | `sortAscending(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Deprecated. use [`sorted(Iterable, ToDoubleFunction)`](#sorted(java.lang.Iterable,java.util.function.ToDoubleFunction)) |
| `static <T extends Comparable<? super T>> void` | `sortAscending(List<T> list)` | Sorts (**modifies**) the specified list into ascending order, according to the [natural ordering](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang") of its elements. |
| `static <T> List<T>` | `sortDescending(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Deprecated. use [`sortedDescending(Iterable, ToDoubleFunction)`](#sortedDescending(java.lang.Iterable,java.util.function.ToDoubleFunction)) |
| `static <T extends Comparable<? super T>> void` | `sortDescending(List<T> list)` | Sorts (**modifies**) the specified list into ascending order, according to the **inverted** [natural ordering](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang") of its elements. |
| `static <T extends Comparable<? super T>> List<T>` | `sorted(Iterable<T> collection)` | Returns a new list with rearranged elements from the given collection sorted *ascending*, according to the [natural ordering](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang"). |
| `static <T> List<T>` | `sorted(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns a new list with rearranged elements/agents from the given collection sorted *ascending* by some numeric value. |
| `static <T extends Comparable<? super T>> List<T>` | `sortedDescending(Iterable<T> collection)` | Returns a new list with rearranged elements from the given collection sorted *descending*, i.e. |
| `static <T> List<T>` | `sortedDescending(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns a new list with rearranged elements/agents from the given collection sorted *descending* by some numeric value. |
| `static double` | `sum(Iterable<? extends Number> collection)` | Returns sum of values in the given collection with numbers. |
| `static <T> double` | `sum(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Returns sum of values in the given collection.  Usage examples: |
| `static <T> double` | `sumWhere(Iterable<T> collection, ToDoubleFunction<? super T> value, Predicate<? super T> condition)` | Returns sum of values in the given collection  among elements which meet the given condition.  Usage examples: |
| `static <T> T` | `top(Iterable<T> collection, ToDoubleFunction<? super T> value)` | Deprecated. please use [`findMax(Iterable, ToDoubleFunction)`](#findMax(java.lang.Iterable,java.util.function.ToDoubleFunction)) |
