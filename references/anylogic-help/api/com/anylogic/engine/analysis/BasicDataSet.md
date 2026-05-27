*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/BasicDataSet.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class BasicDataSet

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.BasicDataSet

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `DataSet`

---

```
public class BasicDataSet
extends ChartItem
```

A data set capable of storing 2D (X,Y) data of type double and maintaining the
up-to-date minimum and maximum of the stored data for each dimension. The data
set keeps a given limited number of the latest data items.
Please note that adding a new item when the dataset is full will cause loss of
the oldest sample and, if the lost item contained minimum or maximum, will
initiate a new search for min/max, which may be quite time consuming for large
datasets. Therefore for large datasets it is recommended to have the size not
less than the number of items yoiu plan to add.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.BasicDataSet)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BasicDataSet(int capacity)` | Constructs a 2D data set with data of type double with a given capacity. |
| `BasicDataSet(int capacity, DataUpdater_xjal updater)` | Constructs a 2D data set with data of type double with a given capacity.  Registers the given updater so that dataset uses it while being updated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double y)` | Adds a new data item to the data set. |
| `void` | `add(double x, double y)` | Adds a new data item to the data set. |
| `void` | `allowDuplicateX(boolean yes)` | Sets the way of handling two subsequent calls of add() with identical X values. |
| `void` | `allowDuplicateY(boolean yes)` | Sets the way of handling two subsequent calls of add() with identical Y values. |
| `void` | `destroyUpdater_xjal()` | This method is used to 'disconnect' this data class from the agent/experiment this object was defined in.  It is usually called on agent destroy so that experiment could use this data object e.g. |
| `boolean` | `duplicateXAllowed()` | Tests if subsequent data items with same X values are allowed in this dataset. |
| `boolean` | `duplicateYAllowed()` | Tests if subsequent data items with same Y values are allowed in this dataset. |
| `void` | `fillFrom(BasicDataSet ds)` | Makes this dataset an exact copy of the given original dataset. |
| `void` | `fillFrom(TableFunction tf)` | Discards all existing data, sets the capacity to equal to the number of entries in the given table function and fills the dataset from the given table function. |
| `int` | `getCapacity()` | Returns the capacity of the data set. |
| `List<List<Object>>` | `getPlainDataTable()` |  |
| `double` | `getX(int i)` | Returns the x of the data items with a given index (which must be in the range 0..size()-1). |
| `double` | `getXMax()` | Returns the maximum of all x values of all stored items, or `-infinity` in case there are no items. |
| `double` | `getXMean()` | Returns the average of all x values of all stored items, or `0` in case there are no items. |
| `double` | `getXMedian()` | Returns the median of all x values of all stored items, or `0` in case there are no items.  Note that this median calculation is time consuming |
| `double` | `getXMin()` | Returns the minimum of all x values of all stored data items, or `+infinity` in case there are no items. |
| `double` | `getY(int i)` | Returns the y of the data items with a given index (which must be in the range 0..size()-1). |
| `double` | `getYMax()` | Returns the maximum of all y values of all stored items, or `-infinity` in case there are no items. |
| `double` | `getYMean()` | Returns the average of all y values of all stored items, or `0` in case there are no items. |
| `double` | `getYMedian()` | Returns the median of all y values of all stored items, or `0` in case there are no items.  Note that this median calculation is time consuming |
| `double` | `getYMin()` | Returns the minimum of all y values of all stored items, or `+infinity` in case there are no items. |
| `void` | `reset()` | Discards all stored data and their minimum/maximum. |
| `void` | `setCapacity(int newcapacity)` | Resizes the data set according to the new capacity. |
| `int` | `size()` | Returns the number of items stored in the data set. |
| `String` | `toString()` | Returns a tab-separated multi-line textual representation of the data set containing not more than 1000 data items. |
| `void` | `update()` | Should be overridden and call add( x, y ) if the user has specified the values for horizontal and/or vertical axes. |
