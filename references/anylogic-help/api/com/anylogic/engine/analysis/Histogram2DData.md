*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Histogram2DData.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Histogram2DData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.Histogram2DData

All Implemented Interfaces:
:   `Serializable`

---

```
public class Histogram2DData
extends ChartItem
```

Data (PDF, CDF, etc.) of an array of histograms, each having a certain range of base
(x) values and a range of data - y values. When an item (x,y) is added to
Histogram2DData, it first finds which individual histogram this item belongs
to (this depends on the x value) and then adds y value to that histigram.
The PDF and CDF are calculated for each individual histogram in the array.
In addition, Histogram2DData is capable of calculating envelopes - the areas
containing a given percent of data in each simple histogram.
Histogram2DData is particularly useful for analyzing a number of stochastic data sets,
e.g. a number of realizations of a stochastic process in time obtained in
different simulation runs.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Histogram2DData)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Histogram2DData(int nXIntervals, double xmin, double xmax, int nYIntervals, double ymin, double ymax, double[] env)` | Constructs a Histigram2DData with a given number of individual historgams each having a given number of intervals, and sets x and y ranges. |
| `Histogram2DData(int nXIntervals, double xmin, double xmax, int nYIntervals, double ymin, double ymax, double[] env, DataUpdater_xjal updater)` | Constructs a Histigram2DData with a given number of individual historgams each having a given number of intervals, and sets x and y ranges. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double xval, double yval)` | Adds a sample data item to the histogram data, updates PDF, CDF and count. |
| `void` | `add(BasicDataSet dataset)` | Adds the whole contents of a given dataset to the histogram data, updates PDF, CDF and count. |
| `int` | `count(int xindex)` | Returns the number of samples added to the histogram with xindex. |
| `void` | `destroyUpdater_xjal()` | This method is used to 'disconnect' this data class from the agent/experiment this object was defined in.  It is usually called on agent destroy so that experiment could use this data object e.g. |
| `double` | `getCDF(int xindex, int yindex)` | Returns the CDF (cumulative distribution function) at the END of the interval yindex of the histogram with xindex. |
| `int` | `getNumberOfXIntervals()` | Returns the number of base (x) intervals, i.e. |
| `int` | `getNumberOfYIntervals()` | Returns the number of data (y) intervals in each individual historgam. |
| `double` | `getPDF(int xindex, int yindex)` | Returns the PDF (probability distribution function) of the histogram with xindex at the interval yindex. |
| `double` | `getPDFOutsideHigh(int xindex)` | Returns the percent of samples (0..1) in the histogram xindex higher than the specified maximum. |
| `double` | `getPDFOutsideLow(int xindex)` | Returns the percent of samples (0..1) in the histogram xindex lower than the specified data (y) minimum. |
| `List<List<Object>>` | `getPlainDataTable()` |  |
| `double` | `getXMax()` | Returns the maximum x (base) value. |
| `double` | `getXMin()` | Returns the minimum x (base) value. |
| `double` | `getYMax()` | Returns the maximum y (data) value. |
| `double` | `getYMin()` | Returns the minimum y (data) value. |
| `void` | `reset()` | Fully resets the histogram data: discards all PDF/CDF data and statistics. |
| `void` | `setEnvelopes(double[] env)` | Sets the array of envelopes to calculate. |
| `String` | `toString()` | Returns a tab-separated multi-line textual representation of the histogram data. |
| `void` | `update()` | Should be overridden and call add( xval, yval ) if the user has specified the values to add. |
