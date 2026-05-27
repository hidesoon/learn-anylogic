*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/DataSet.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class DataSet

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.BasicDataSet](BasicDataSet.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.DataSet

All Implemented Interfaces:
:   `Serializable`

---

```
public class DataSet
extends BasicDataSet
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
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.DataSet)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `DataSet.SvgSynchronizationHandler` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DataSet(int capacity)` | Constructs a 2D data set with data of type double with a given capacity. |
| `DataSet(int capacity, DataUpdater_xjal updater)` | Constructs a 2D data set with data of type double with a given capacity.  Registers the given updater so that dataset uses it while being updated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double x, double y)` | Adds a new data item to the data set. |
| `void` | `add(double x, IStatechartState<?,?> state)` | Adds a new statechart state data item to the data set. |
| `DataSet.SvgSynchronizationHandler` | `createSvgSyncHandler()` |  |
| `void` | `fillFrom(BasicDataSet ds)` | Makes this dataset an exact copy of the given original dataset. |
| `void` | `fillFrom(TableFunction tf)` | Discards all existing data, sets the capacity to equal to the number of entries in the given table function and fills the dataset from the given table function. |
| `void` | `reset()` | Discards all stored data and their minimum/maximum. |
| `void` | `setCapacity(int newcapacity)` | Resizes the data set according to the new capacity. |
