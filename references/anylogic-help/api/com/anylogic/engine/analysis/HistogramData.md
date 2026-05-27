*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/HistogramData.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class HistogramData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.HistogramData

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `HistogramSimpleData`, `HistogramSmartData`

---

```
public abstract class HistogramData
extends ChartItem
```

A base class for unidimensional histograms data objects.
Histogram data always calculates the probability distribution function (PDF) and
discrete statistics, and may or may not calculate the cumulative distribution
function (CDF) and low/high percentiles.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.HistogramData)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `add(double val)` | Adds a sample data item to the histogram data. |
| `boolean` | `arePercentilesEnabled()` | Checks if percentile calculation is enabled. |
| `int` | `count()` | Returns the number of samples added to the histogram data. |
| `void` | `destroyUpdater_xjal()` | This method is used to 'disconnect' this data class from the agent/experiment this object was defined in.  It is usually called on agent destroy so that experiment could use this data object e.g. |
| `double` | `deviation()` | Returns the standard deviation of the histogram data. |
| `double` | `getCDF(int index)` | Returns the CDF (cumulative distribution function) at the END of the given interval. |
| `double` | `getIntervalWidth()` | Returns the interval width, i.e. |
| `double` | `getMaxPDF()` | Returns the maximum PDF value across all intervals, i.e. |
| `int` | `getNumberOfIntervals()` | Returns the number of intervals in the histogram data. |
| `double` | `getPDF(int index)` | Returns the PDF (probability distribution function) at the given interval. |
| `double` | `getPercentHigh()` | Returns the high percent value used for percentile calculation (1 is 100%). |
| `double` | `getPercentLow()` | Returns the low percent value used for percentile calculation (1 is 100%). |
| `List<List<Object>>` | `getPlainDataTable()` |  |
| `StatisticsDiscrete` | `getStatistics()` | Returns the statisctics object embedded into the histogram data. |
| `abstract double` | `getXMax()` | Returns the upper bound of the range covered by intervals. |
| `abstract double` | `getXMin()` | Returns the lower bound of the range covered by intervals. |
| `boolean` | `isCDFEnabled()` | Checks if the CDF calculation is enabled. |
| `double` | `max()` | Returns the maximum sample value, or `-infinity` if no samples have been added. |
| `double` | `mean()` | Returns the mean of the histogram. |
| `double` | `meanConfidence()` | Returns the mean confidence interval of the histogram data.  Interval is calculated for the confidence level of 95%. |
| `double` | `min()` | Returns the minimum sample value, or `+infinity` if no samples have been added. |
| `void` | `reset()` | Fully resets the histogram data: discards all PDF/CDF data and statistics. |
| `void` | `setCDFEnabled(boolean yes)` | Enables or disables the CDF calculation. |
| `void` | `setPercentilesEnabled(boolean yes)` | Enables or disables calculation of percentiles (the data values corresponding to a certain low and high percent bounds). |
| `void` | `setPercents(double low, double high)` | Sets the percent bounds for percentile calculation. |
| `String` | `toString()` | Returns a tab-separated multi-line textual representation of the histogram data. |
| `void` | `update()` | Should be overridden and call add( val ) if the user has specified the value to add. |
