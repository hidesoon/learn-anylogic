*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Dimension.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Dimension

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Dimension

All Implemented Interfaces:
:   `Serializable`

---

```
public final class Dimension
extends Object
implements Serializable
```

A dimension of a HyperArray - a set of non-negative integers (or identifiers
mapped to non-negative integers) that are used as indexes in hyper arrays.
An index cannot be included in a dimension more than once.
A dimension can be a sub-dimension of another dimension, in this case it
contains a subset (or maybe a full set) of the super dimension indexes.
The top level dimension in the dimension hierarchy does not have a super-
dimension.
Optionally, you can provide names for indexes at a top-level dimension.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Dimension)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `DIMENSIONS_CONTAINER_CLASS_NAME` | Deprecated. |
| `final int[]` | `indexes` | An array of indexes included in this dimension. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Dimension(String packageName, String name, int... indexes)` | Creates a top-level dimension with a given name and given set of integer indexes not having names. |
| `Dimension(String packageName, String name, int[] indexes, String[] indexnames)` | Creates a top-level dimension with a given name and given set of integer indexes, each having a name. |
| `Dimension(String packageName, String name, Dimension superdim, int... indexes)` | Creates a sub-dimension of another dimension. |
| `Dimension(String packageName, String name, Dimension superdim, String indexes)` | Creates a sub-dimension of another dimension. |
| `Dimension(String packageName, String name, String indexes)` | Creates a top-level dimension with a given name and given set of integer indexes not having names. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `getIndexByName(String name)` | Returns the index having the specified textual name. |
| `int` | `getIndexByPosition(int position)` | Returns the index having the specified position in this dimension (from 0 to size()-1). |
| `String` | `getIndexName(int ind)` | Returns the textual name of the given index, or its formatted integer value in case index name is not set. |
| `String` | `getIndexNameByPosition(int position)` | Returns the textual name of the index located at the given position, or formatted integer value of the index in case index name is not set. |
| `int` | `getIndexPosition(int ind)` | Returns the position of an index in this dimension, starting from 0. |
| `int` | `getIndexPositionByName(String name)` | Returns the position of the index in this dimension (from 0 to size()-1) having the specified textual name. |
| `String` | `getName()` | Returns the name of the dimension. |
| `Dimension` | `getSuperDimension()` | Returns super-dimension of this dimension or null if this is a top-level dimension. |
| `static int[]` | `parseRangeIndexes(String str)` | Deprecated. |
| `int` | `size()` | Returns the number of indexes in the dimension. |
