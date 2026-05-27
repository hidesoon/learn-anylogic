*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/package-summary.html>*

---

# Package com.anylogic.engine.analysis

---

| Class | Description |
| --- | --- |
| [AnalysisInternalsAccessor\_xjal](AnalysisInternalsAccessor_xjal.md "class in com.anylogic.engine.analysis") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [BarChart](BarChart.md "class in com.anylogic.engine.analysis") | The chart that displays a number of data items as bars with dimension proportional to their values (which can be negative). |
| [BasicDataSet](BasicDataSet.md "class in com.anylogic.engine.analysis") | A data set capable of storing 2D (X,Y) data of type double and maintaining the up-to-date minimum and maximum of the stored data for each dimension. |
| [Chart](Chart.md "class in com.anylogic.engine.analysis")<E extends [ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")> | The base class for all charts. |
| [Chart.Direction](Chart.Direction.md "enum class in com.anylogic.engine.analysis") | multipurpose direction/position constants |
| [Chart.GridPosition](Chart.GridPosition.md "enum class in com.anylogic.engine.analysis") | grid text position constants |
| [Chart.InterpolationType](Chart.InterpolationType.md "enum class in com.anylogic.engine.analysis") | interpolation types |
| [Chart.LegendOrientation](Chart.LegendOrientation.md "enum class in com.anylogic.engine.analysis") |  |
| [Chart.PointStyle](Chart.PointStyle.md "enum class in com.anylogic.engine.analysis") | line point styles |
| [Chart.ScaleType](Chart.ScaleType.md "enum class in com.anylogic.engine.analysis") | scale types |
| [Chart.TimeWindowMovementType](Chart.TimeWindowMovementType.md "enum class in com.anylogic.engine.analysis") |  |
| [Chart1D](Chart1D.md "class in com.anylogic.engine.analysis") | The base class for all charts that display a collection of single data items, like Pie, Bar, or Stack. |
| [Chart1DSum](Chart1DSum.md "class in com.anylogic.engine.analysis") | A base class for all charts that display the fractions of the data items of their total (like Pie or Stack). |
| [Chart2D](Chart2D.md "class in com.anylogic.engine.analysis") | The base class for all charts that display a collection of two-dimensional data sets, like Plot, TimePlot, TimeStack, Color. |
| [Chart2DPlot](Chart2DPlot.md "class in com.anylogic.engine.analysis") | The base class for all charts that display a collection of two-dimensional data sets in the form of plots, like Plot, TimePlot. |
| [Chart2DPlot.Appearance](Chart2DPlot.Appearance.md "class in com.anylogic.engine.analysis") | Descriptor or a data set plot appearance. |
| [ChartItem](ChartItem.md "class in com.anylogic.engine.analysis") | An item that holds data and can be displayed by a chart (a unit of what can be displayed by the chart). |
| [ColorMapping](ColorMapping.md "class in com.anylogic.engine.analysis") | Conditional expression which determines the color of the value in [`TimeColorChart`](TimeColorChart.md "class in com.anylogic.engine.analysis") |
| [ColorMappingOperator](ColorMappingOperator.md "enum class in com.anylogic.engine.analysis") | Operator for [`ColorMapping`](ColorMapping.md "class in com.anylogic.engine.analysis") - conditional expression which determines the color of the value in [`TimeColorChart`](TimeColorChart.md "class in com.anylogic.engine.analysis") |
| [DataItem](DataItem.md "class in com.anylogic.engine.analysis") | A chart item that contains a single scalar value of type double. |
| [DataSet](DataSet.md "class in com.anylogic.engine.analysis") | A data set capable of storing 2D (X,Y) data of type double and maintaining the up-to-date minimum and maximum of the stored data for each dimension. |
| [DataSet.SvgSynchronizationHandler](DataSet.SvgSynchronizationHandler.md "class in com.anylogic.engine.analysis") |  |
| [DataUpdater\_xjal](DataUpdater_xjal.md "class in com.anylogic.engine.analysis") | This class provides another way to override [update()](ChartItem.md#update()) method of data set, histogram and other data elements. |
| [Histogram](Histogram.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of histograms. |
| [Histogram.Appearance](Histogram.Appearance.md "class in com.anylogic.engine.analysis") | Descriptor or a histogram appearance. |
| [Histogram2D](Histogram2D.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of two-dimensional histograms. |
| [Histogram2D.Appearance](Histogram2D.Appearance.md "class in com.anylogic.engine.analysis") | Descriptor or histogram 2D appearance. |
| [Histogram2DData](Histogram2DData.md "class in com.anylogic.engine.analysis") | Data (PDF, CDF, etc.) of an array of histograms, each having a certain range of base (x) values and a range of data - y values. |
| [HistogramData](HistogramData.md "class in com.anylogic.engine.analysis") | A base class for unidimensional histograms data objects. |
| [HistogramSimpleData](HistogramSimpleData.md "class in com.anylogic.engine.analysis") | Data of a histogram with a fixed minimum, maximum and number of intervals. |
| [HistogramSmartData](HistogramSmartData.md "class in com.anylogic.engine.analysis") | Data of a histogram with a fixed number of intervals but auto-adjustable data range. |
| [PieChart](PieChart.md "class in com.anylogic.engine.analysis") | The chart that displays a number of data items in the form of a pie where each data item has a sector with angular extension proportional to its fraction the total sum of the data items. |
| [Plot](Plot.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of data sets as plots - polylines with point at each data point and straingh lines in between. |
| [StackChart](StackChart.md "class in com.anylogic.engine.analysis") | The chart that displays a number of data items in the form of a stack where each data item has a bar with dimension proportional to its fraction the total sum of the data items. |
| [StatisticsContinuous](StatisticsContinuous.md "class in com.anylogic.engine.analysis") | Statistics on a value that persists in continuous time but changes only at discrete time moments (like e.g. |
| [StatisticsDiscrete](StatisticsDiscrete.md "class in com.anylogic.engine.analysis") | Statistics on a series of data samples of type double. |
| [TimeColorChart](TimeColorChart.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of data sets as a number of horizontal strips with color varying along the X (time) axis. |
| [TimeColorChart.ColorMap](TimeColorChart.ColorMap.md "class in com.anylogic.engine.analysis") | Deprecated. |
| [TimePlot](TimePlot.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of data sets as plots - polylines with point at each data point and straight lines in between. |
| [TimeStackChart](TimeStackChart.md "class in com.anylogic.engine.analysis") | The chart that displays a collection of data sets in the form of a timed stack, i.e. |
