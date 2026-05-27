*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ScheduleWithUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ScheduleWithUnits<U extends IUnits<U>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Schedule](Schedule.md "class in com.anylogic.engine")<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang")>

com.anylogic.engine.ScheduleWithUnits<U>

Type Parameters:
:   `V` - the type of schedule values
:   `U` - the type of units used by this schedule

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class ScheduleWithUnits<U extends IUnits<U>>
extends Schedule<Double>
```

Schedule with units (Time, Rate etc.). For more information, see [`Schedule`](Schedule.md "class in com.anylogic.engine").
Usage:

```
 ScheduleWithUnits<Double, RateUnits> s = new ScheduleWithUnits<Double, RateUnits>(PER_HOUR);

 // configure 's': s.setPeriod() etc.
 s.initialize();

 double rate = s.getValue(PER_MINUTE);
```

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Schedule`](Schedule.md "class in com.anylogic.engine")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ScheduleWithUnits)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ScheduleWithUnits(Utilities owner, boolean calendarType, int firstDayOfWeek, long period, long timeUnits, Long snapTo, Double defaultValue, long[] exStarts, long[] exEnds, Object[] exValues, boolean glueIntervals, boolean[] exceptionsAnnually, boolean singleThreadMode, boolean isLateInit, U units)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ScheduleWithUnits(Utilities owner, boolean calendarType, int firstDayOfWeek, long period, long timeUnits, Long snapTo, Double defaultValue, long[] starts, long[] ends, Object[] values, boolean glueIntervals, boolean[] exceptionsAnnually, boolean singleThreadMode, U units)` |  |
| `ScheduleWithUnits(U units)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Double` | `getNextValue(double time, TimeUnits timeUnits, U valueUnits)` | Returns the value of the schedule change moment next to the given `time`.  In case when there is no 'next' value, returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Double` | `getNextValue(double time, U units)` | Returns the value of the schedule change moment next to the given `time`.  In case when there is no 'next' value, returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Double` | `getNextValue(Date date, U units)` | Returns the value of the schedule change moment next to the given model `date`.  In case when there is no 'next' value, returns `null`.  In case of `null` argument value, returns `null` |
| `Double` | `getNextValue(U units)` | Returns the value of the next change moment in the schedule.  In case when there is no 'next' value, returns `null` |
| `U` | `getUnits()` | Returns units used by functions like [`Schedule.getValue()`](Schedule.md#getValue()) |
| `Double` | `getValue(double time, TimeUnits timeUnits, U valueUnits)` | Returns the value of the schedule corresponding to the given `time`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Double` | `getValue(double time, U units)` | Returns the value of the schedule corresponding to the given model `time`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Double` | `getValue(Date date, U units)` | Returns the value of the schedule corresponding to the given model `date`.  In case of `null` argument value, returns `null` |
| `Double` | `getValue(U units)` | Returns the value corresponding to the current model time |
