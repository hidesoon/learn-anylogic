*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/StatisticsDiscrete.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class StatisticsDiscrete

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.StatisticsDiscrete

All Implemented Interfaces:
:   `Serializable`

---

```
public class StatisticsDiscrete
extends Object
implements Serializable
```

Statistics on a series of data samples of type double. Compared to
StatisticsContinuous, data samples here have no relation to time
(like e.g. products cost or patients LOS).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.StatisticsDiscrete)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StatisticsDiscrete()` | Creates a discrete statistics. |
| `StatisticsDiscrete(DataUpdater_xjal updater)` | Creates a discrete statistics. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(double value)` | Adds a sample value to the statistics. |
| `int` | `count()` | Returns the number of samples added to the statistics. |
| `void` | `destroyUpdater_xjal()` | This method is used to 'disconnect' this data class from the agent/experiment this object was defined in.  It is usually called on agent destroy so that experiment could use this data object e.g. |
| `double` | `deviation()` | Returns the standard deviation of the statistics. |
| `double` | `max()` | Returns the maximum sample value, or `-infinity` if no samples have been added. |
| `double` | `mean()` | Returns the mean of the statistics, or 0 if no samples have been added. |
| `double` | `meanConfidence()` | Returns the mean confidence interval of the statistics, or `0` if no samples have been added. |
| `double` | `min()` | Returns the minimum sample value, or `+infinity` if no samples have been added. |
| `void` | `reset()` | Discards all statistics accumulated. |
| `double` | `sum()` | The method returns sum of the samples added to the statistics, or 0 if no samples have been added. |
| `String` | `toString()` | Returns the tab-separated multiline textual representation of the statistics. |
| `void` | `update()` | Should be overridden and call add( val ) if the user has specified the value. |
| `double` | `variance()` | Returns the variance of the statistics, or 0 if less than 2 samples have been added. |
