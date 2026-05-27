*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/StatisticsContinuous.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class StatisticsContinuous

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.StatisticsContinuous

All Implemented Interfaces:
:   `Serializable`

---

```
public class StatisticsContinuous
extends Object
implements Serializable
```

Statistics on a value that persists in continuous time but changes only
at discrete time moments (like e.g. queue length). The samples must be
added to this statistics with ascending time stamps. The [mean](#mean()),
[variance](#variance()), etc. return data at the time of last update.
Also there are alternative methods - with `time` argument,
which assume the last value added holds until the given time.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.StatisticsContinuous)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StatisticsContinuous()` | Creates a continuous statistics. |
| `StatisticsContinuous(DataUpdater_xjal updater)` | Creates a continuous statistics. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double value, double time)` | Adds a new data sample to the statistics, i.e. |
| `int` | `count()` | Returns the number of samples added to the statistics. |
| `void` | `destroyUpdater_xjal()` | This method is used to 'disconnect' this data class from the agent/experiment this object was defined in.  It is usually called on agent destroy so that experiment could use this data object e.g. |
| `double` | `deviation()` | Returns the deviation of the statistics at the time of last update. |
| `double` | `deviation(double time)` | Returns the standard deviation of the statistics at the given time assuming the last value added holds until the given time. |
| `double` | `getTimeStart()` | This method is needed to calculate totalTime in cloud. |
| `double` | `integral()` | Returns the mean integral of the statistics at the time of last update, or 0 if no samples have been added. |
| `double` | `integral(double time)` | Returns the integral of the statistics at the given time assuming the last value added holds until the given time, or 0 if no samples have been added. |
| `double` | `max()` | Returns the maximum sample value, or `-infinity` if no samples have been added. |
| `double` | `mean()` | Returns the mean of the statistics at the time of last update, or 0 if no samples have been added. |
| `double` | `mean(double time)` | Returns the mean of the statistics at the given time assuming the last value added holds until the given time, or 0 if no samples have been added. |
| `double` | `meanConfidence()` | Returns the mean confidence of the statistics at the time of last update, or 0 if no samples have been added.  Interval is calculated for the confidence level of 95%. |
| `double` | `meanConfidence(double time)` | Returns the mean confidence interval of the statistics at the given time assuming the last value added holds until the given time, or `+infinity` if less than 2 samples have been added or if no time has elapsed.  Interval is calculated for the confidence level of 95%. |
| `double` | `min()` | Returns the minimum sample value, or `+infinity` if no samples have been added. |
| `void` | `reset()` | Discards all statistics accumulated. |
| `String` | `toString()` | Returns the tab-separated multiline textual representation of the statistics corresponding to the time of last update. |
| `void` | `update()` | Should be overridden and call add( val, time() ) if the user has specified the value. |
| `double` | `variance()` | Returns the variance of the statistics at the time of last update, or 0 if no samples have been added. |
| `double` | `variance(double time)` | Returns the variance of the statistics at the given time assuming the last value added holds until the given time, or 0 if no samples have been added. |
