*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/DataUpdater_xjal.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class DataUpdater\_xjal

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.DataUpdater\_xjal

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalCodegenAPI
public class DataUpdater_xjal
extends Object
implements Serializable
```

This class provides another way to override [update()](ChartItem.md#update()) method of data set, histogram and other data elements. Subclass
should override one of methods and may be passed to appropriate constructor
of data element, e.g. [`DataSet(int, DataUpdater_xjal)`](DataSet.md#%3Cinit%3E(int,com.anylogic.engine.analysis.DataUpdater_xjal))

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.DataUpdater_xjal)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DataUpdater_xjal()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDataXValue()` | Override this method to enable [`BasicDataSet.add(double)`](BasicDataSet.md#add(double)) method.  Default implementation throws exception. |
| `void` | `update(BasicDataSet ds)` | Another way to override [`BasicDataSet.update()`](BasicDataSet.md#update()) |
| `void` | `update(Histogram2DData data)` | Another way to override [`Histogram2DData.update()`](Histogram2DData.md#update()) |
| `void` | `update(HistogramData data)` | Another way to override [`HistogramData.update()`](HistogramData.md#update()) |
| `void` | `update(StatisticsContinuous statistics)` | Another way to override [`StatisticsContinuous.update()`](StatisticsContinuous.md#update()) |
| `void` | `update(StatisticsDiscrete statistics)` | Another way to override [`StatisticsDiscrete.update()`](StatisticsDiscrete.md#update()) |
