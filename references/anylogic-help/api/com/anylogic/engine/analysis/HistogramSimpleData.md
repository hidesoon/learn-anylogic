*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/HistogramSimpleData.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class HistogramSimpleData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.HistogramData](HistogramData.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.HistogramSimpleData

All Implemented Interfaces:
:   `Serializable`

---

```
public class HistogramSimpleData
extends HistogramData
```

Data of a histogram with a fixed minimum, maximum and number of intervals.
The outlaying samples are registered in special "too low" and "too high"
intervals.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.HistogramSimpleData)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `HistogramSimpleData(int nIntervals, double min, double max, boolean calcCDF, boolean calcPercentiles, double lowPercent, double highPercent)` | Constructs a simple histogram data object with the given number of intervals and range. |
| `HistogramSimpleData(int nIntervals, double min, double max, boolean calcCDF, boolean calcPercentiles, double lowPercent, double highPercent, DataUpdater_xjal updater)` | Constructs a simple histogram data object with the given number of intervals and range. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double val)` | Adds a sample data item to the histogram data object, updates PDF, CDF and statistics. |
| `double` | `getPDFOutsideHigh()` | Returns the percent of samples (0..1) higher than the specified maximum. |
| `double` | `getPDFOutsideLow()` | Returns the percent of samples (0..1) lower than the specified minimum. |
| `double` | `getXMax()` | Returns the upper bound of the range covered by intervals. |
| `double` | `getXMin()` | Returns the lower bound of the range covered by intervals. |
| `void` | `reset()` | Fully resets the histogram data: discards all PDF/CDF data and statistics. |
| `void` | `setMinMax(double min, double max)` | Fully resets the histogram data and sets the new range covered by intervals. |
