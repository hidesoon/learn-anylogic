*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Schedule.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Schedule<V extends Serializable>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Schedule<V>

Type Parameters:
:   `V` - the type of schedule values

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

Direct Known Subclasses:
:   `ScheduleWithUnits`

---

```
public class Schedule<V extends Serializable>
extends Object
implements Serializable, com.anylogic.engine.internal.Child
```

Schedule class. Allows to track moments specified using time table with some
period. Also, annual and single exceptions may be added to the schedule.
Schedule provides 4 types of information:

* the current value: [`getValue()`](#getValue())
* the moment since the schedule has been holding its current value:
  [`getTimeOfValue()`](#getTimeOfValue()), [`getDateOfValue()`](#getDateOfValue())
* the next value of the schedule (which will be set in future):
  [`getNextValue()`](#getNextValue())
* the time of the moment schedule switches to the next value:
  [`getTimeOfNextValue()`](#getTimeOfNextValue()), [`getDateOfNextValue()`](#getDateOfNextValue()),
  [`getTimeoutToNextValue()`](#getTimeoutToNextValue())

All these accessor methods are available in several forms:

* without any argument - data is retrieved for the current
  [model time](Utilities.md#time())
* with argument *`time`* of type `double`: data is
  retrieved for the provided model `time`. In case of
  `+/-infinity` or
  `NaN` argument value, `getValue*` and
  `getDate*` methods return `null`, and `getTime*`
  and `getTimeout*` methods return [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang")
* with argument *`date`* of type `Date`: data
  is retrieved for the provided model `date`. In case of
  `null` argument value, `getValue*` and
  `getDate*` methods return `null`, and `getTime*`
  and `getTimeout*` methods return [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang")

This object may be used for event scheduling. See the following code example
(please note, that it is more preferable to use [`getTimeOfNextValue()`](#getTimeOfNextValue())
method instead of [`getTimeoutToNextValue()`](#getTimeoutToNextValue()) because of possible
numeric calculation errors). Create the [timeout event](EventTimeout.md "class in com.anylogic.engine")
which *[occurs once](AgentConstants.md#EVENT_TIMEOUT_MODE_ONCE)* at the time:

```
        schedule.getTimeOfValue() == time() ? time() : schedule.getTimeOfNextValue()
```

and has the following action code:

```
        // ...your custom actions are here...
        event.restartTo( schedule.getTimeOfNextValue() );
```

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Schedule)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Schedule()` | Creates new schedule object |
| `Schedule(Utilities owner, boolean calendarType, int firstDayOfWeek, long period, long timeUnits, Long snapTo, V defaultValue, long[] starts, long[] ends, Object[] values, boolean glueIntervals, boolean[] exceptionsAnnually, boolean singleThreadMode)` | Creates new schedule object |
| `Schedule(Utilities owner, boolean calendarType, int firstDayOfWeek, long period, long timeUnits, Long snapTo, V defaultValue, long[] exStarts, long[] exEnds, Object[] exValues, boolean glueIntervals, boolean[] exceptionsAnnually, boolean singleThreadMode, boolean isLateInit)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addException(int startYear, int startMonth, int startDay, int startHour, int startMinute, int startSecond, int endYear, int endMonth, int endDay, int endHour, int endMinute, int endSecond, V value, boolean annually)` | Adds new particular time intervals when the value defined by this schedule should have other values |
| `void` | `addInterval(int startWeek, int startDayOfWeek, int startHour, int startMinute, int startSecond, int endWeek, int endDayOfWeek, int endHour, int endMinute, int endSecond, V value)` | Adds new particular time interval to this schedule |
| `void` | `addInterval(int startDay, int startHour, int startMinute, int startSecond, int endDay, int endHour, int endMinute, int endSecond, V value)` | Adds new particular time interval to this schedule |
| `void` | `addInterval(int startHour, int startMinute, int startSecond, int endHour, int endMinute, int endSecond, V value)` | Adds new particular time interval to this schedule |
| `void` | `addInterval(int startHour, int startMinute, int startSecond, int endHour, int endMinute, int endSecond, V value, int[] weekDays)` | Adds new particular time intervals to this schedule |
| `void` | `addInterval(long start, long end, V value)` | Adds new particular time interval to this schedule |
| `void` | `addMoment(int week, int dayOfWeek, int hour, int minute, int second, V value)` | Adds new particular time moment to this schedule |
| `void` | `addMoment(int day, int hour, int minute, int second, V value)` | Adds new particular time moment to this schedule |
| `void` | `addMoment(int hour, int minute, int second, V value)` | Adds new particular time moment to this schedule |
| `void` | `addMoment(int hour, int minute, int second, V value, int[] weekDays)` | Adds new particular time moment to this schedule |
| `void` | `addMoment(long time, V value)` | Adds new particular time moment to this schedule |
| `Date` | `getDateOfNextValue()` | Returns the model date of the next change moment in the schedule.  In case when there is no 'next' value, returns `null` |
| `Date` | `getDateOfNextValue(double time)` | Returns the model date of the schedule change moment next to the given model `time`.  In case when there is no 'next' value, returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Date` | `getDateOfNextValue(Date date)` | Returns the model date of the schedule change moment next to the given model `date`.  In case when there is no 'next' value, returns `null`.  In case of `null` argument value, returns `null` |
| `Date` | `getDateOfValue()` | Returns the model date the current value of the schedule has been held since.  If the schedule has always been holding the current value, the method returns `null` |
| `Date` | `getDateOfValue(double time)` | Returns the model date of the schedule change moment of the value corresponding to the given model `time`.  If the schedule has always been holding the current value (up to the given `time`), the method returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `Date` | `getDateOfValue(Date date)` | Returns the model date of the schedule change moment of the value corresponding to the given model `date`.  If the schedule has always been holding the current value (up to the given `date`), the method returns `null`.  In case of `null` argument value, returns `null` |
| `Set<V>` | `getDistinctValues_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `V` | `getNextValue()` | Returns the value of the next change moment in the schedule.  In case when there is no 'next' value, returns `null` |
| `V` | `getNextValue(double time)` | Returns the value of the schedule change moment next to the given model `time`.  In case when there is no 'next' value, returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `V` | `getNextValue(double time, TimeUnits units)` | Returns the value of the schedule change moment next to the given `time`.  In case when there is no 'next' value, returns `null`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `V` | `getNextValue(Date date)` | Returns the value of the schedule change moment next to the given model `date`.  In case when there is no 'next' value, returns `null`.  In case of `null` argument value, returns `null` |
| `double` | `getTimeOfNextValue()` | Returns the model time of the next change moment in the schedule.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity) |
| `double` | `getTimeOfNextValue(double time)` | Returns the model time of the schedule change moment next to the given model `time`.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity).  In case of `+/-infinity` or `NaN` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `double` | `getTimeOfNextValue(Date date)` | Returns the model time of the schedule change moment next to the given model `date`.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity).  In case of `null` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `double` | `getTimeOfValue()` | Returns the model time the current value of the schedule has been held since.  If the schedule has always been holding the current value, the method returns negative infinity |
| `double` | `getTimeOfValue(double time)` | Returns the model time of the schedule change moment of the value corresponding to the given model `time`.  If the schedule has always been holding the current value (up to the given `time`), the method returns negative infinity.  In case of `+/-infinity` or `NaN` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `double` | `getTimeOfValue(Date date)` | Returns the model time of the schedule change moment of the value corresponding to the given model `date`.  If the schedule has always been holding the current value (up to the given `date`), the method returns negative infinity.  In case of `null` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `double` | `getTimeoutToNextValue()` | Returns timeout to the next change moment in the schedule, measured in the model time units from the current model time.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity) |
| `double` | `getTimeoutToNextValue(double time)` | Returns timeout to the schedule change moment next to the given `time`, measured in the model time units from that `time`.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity).  In case of `+/-infinity` or `NaN` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `double` | `getTimeoutToNextValue(Date date)` | Returns timeout to the schedule change moment next to the given model `date`, measured in the model time units from that model `date`.  In case when there is no 'next' value, returns [positive infinity](UtilitiesMath.md#infinity).  In case of `null` argument value, returns [`Double.NaN`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#NaN "class or interface in java.lang") |
| `long` | `getTimeUnits()` | Returns time units of the schedule |
| `V` | `getValue()` | Returns the value corresponding to the current model time |
| `V` | `getValue(double time)` | Returns the value of the schedule corresponding to the given model `time`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `V` | `getValue(double time, TimeUnits units)` | Returns the value of the schedule corresponding to the given `time`.  In case of `+/-infinity` or `NaN` argument value, returns `null` |
| `V` | `getValue(Date date)` | Returns the value of the schedule corresponding to the given model `date`.  In case of `null` argument value, returns `null` |
| `void` | `initialize()` |  |
| `boolean` | `isInitialized()` |  |
| `void` | `lazyInit(long[] starts, long[] ends, Object[] values)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setCalendarType(boolean calendarType)` | Sets the calendar type |
| `void` | `setDefaultValue(V defaultValue)` | Sets the default value used when there is no interval defined in the schedule |
| `void` | `setFirstDayOfWeek(int firstDayOfWeek)` | Sets the first day of the week |
| `void` | `setGlueIntervals(boolean glueIntervals)` |  |
| `void` | `setOwner(Utilities owner)` | Sets the owner agent or experiment owning the schedule |
| `void` | `setPeriod(int period)` | Sets the recurrence period of the schedule |
| `void` | `setSingleThreadMode(boolean singleThreadMode)` | Sets the thread mode |
| `void` | `setSnapTo(int year, int month, int day, int hour, int minute, int second)` | Sets start time of the schedule |
| `void` | `setSnapTo(long snapTo)` | Sets start time of the schedule |
| `void` | `setTimeUnits(long timeUnits)` | Sets the time units of the schedule |
| `String` | `toString()` |  |
