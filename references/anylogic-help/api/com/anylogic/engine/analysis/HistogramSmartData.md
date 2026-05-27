*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/HistogramSmartData.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class HistogramSmartData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.HistogramData](HistogramData.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.HistogramSmartData

All Implemented Interfaces:
:   `Serializable`

---

```
public class HistogramSmartData
extends HistogramData
```

Data of a histogram with a fixed number of intervals but auto-adjustable data range.
The data range covered by the intervals always includes the full range of
data samples added.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.HistogramSmartData)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `HistogramSmartData(int nIntervals, double initialIntervalWidth, boolean calcCDF, boolean calcPercentiles, double lowPercent, double highPercent)` | Constructs a smart histogram data object with the given number of intervals and initial interval width. |
| `HistogramSmartData(int nIntervals, double initialIntervalWidth, boolean calcCDF, boolean calcPercentiles, double lowPercent, double highPercent, DataUpdater_xjal updater)` | Constructs a smart histogram data object with the given number of intervals and initial interval width. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double val)` | Adds a sample data item to the histogram data object. |
| `double` | `getIntervalWidth()` | Returns the current interval width, i.e. |
| `double` | `getLowerBound()` | Returns the lower bound of the range covered by intervals. |
| `double` | `getXMax()` | Returns the upper bound of the range covered by intervals. |
| `double` | `getXMin()` | Returns the lower bound of the range covered by intervals. |
| `void` | `reset()` | Fully resets the histogram data object: discards all PDF/CDF data and statistics; also restores the initial interval width. |
