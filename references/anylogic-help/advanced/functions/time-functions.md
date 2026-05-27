*来源 (Source): <https://anylogic.help/advanced/functions/time-functions.html>*

---

# Time functions

* [Finding out the current model time](#finding-out-the-current-model-time)
* [Finding out the current date, day of week, hour of day, etc.](#finding-out-the-current-date-day-of-week-hour-of-day-etc)
* [Making model independent of time unit settings](#making-model-independent-of-time-unit-settings)
* [Conversion functions](#conversion-functions)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### Finding out the current model time

You can get current model (logical) time using the function [time()](time.md). There are two notations: the simple one, time() returns the current model time as number of model time units simulated since the model start. Another, time(TIME\_UNIT) returns the number of specified time units simulated so far. For example, time(MINUTE) returns the number of simulated minutes (a double value).

### Finding out the current date, day of week, hour of day, etc.

The date in AnyLogic is stored in the form of the Java class Date. Date is composed of the year, month, day of month, hour of the day, minute, second, and millisecond. To find out the current date, you should call the function date().

A number of functions return particular components of the current date (and all those functions also have the form with a parameter Date date, in which case they return the component of the given, not current, date):

* int getYear() — returns the year of the current date.
* int getMonth() — returns the month of the current date: one of the constants JANUARY, FEBRUARY, etc.
* int getDayOfMonth() — returns the day of the month of the current date: 1, 2, …
* int getDayOfWeek() — returns the day of the week of the current model date as an integer constant: SUNDAY (1), MONDAY (2), and so on.
* int getHourOfDay() — returns the hour of the day of the current date in 24-hour format: for 10:20 PM, will return 22.
* int getHour() — returns the hour of the day of the current date in 12-hour format: for 10:20 PM, will return 10.
* int getAmPm() — returns the constant AM if the current date is before noon, and PM otherwise.
* int getMinute() — returns the minute within the hour of the current date.
* int getSecond() — returns the second within the minute of the current date.
* int getMillisecond() — returns the millisecond within the second of the current date.

### Making model independent of time unit settings

Let’s say the time unit in your model is hours. What if you need to schedule something to happen in 2 days? Or how would you define a duration of 5 minutes? Of course, you could write 48 and 5.0/60. But a much better solution is to use the special functions that return the value of a given time interval with respect to the current time unit settings:

* double millisecond() — returns the value of a one-millisecond time interval.
* double second() — returns the value of a one-second time interval.
* double minute() — returns the value of a one-minute time interval.
* double hour() — returns the value of a one-hour time interval.
* double day() — returns the value of a one-day time interval.
* double week() — returns the value of a one-week time interval.

For example, if the time unit is hours, minute() will return 0.0166, and week() will return 168.0. Thus, instead of remembering what the current time unit is and writing 48 or 5./60, you can simply write 2\*day() and 5\*minute(). You can also combine different units in one expression: 3 \* hour() 20 \* minute().

What is probably even more important about these functions is that the expressions using them are completely independent of the time unit settings: the expressions always evaluate to the correct time intervals. Therefore, we recommend always using multipliers such as minute(), hour(), day(), etc. in the numeric expressions that represent time intervals: this way, you can freely change the time units without changing the model.

### Conversion functions

* double addToDate(Date date, int timeUnit, double amount) — Returns the date obtained by adding the given amount of specified time units to the original date (with respect to daylight saving time), e.g. addToDate(date(), DAY, 1) returns the 'tomorrow' date: (current date + 1 day)
* Date getDateWithTimeNextTo(Date date, int hourOfDay, int minute, int second) — Returns the next date after the given date, with the specified time in the default system time zone.
* double dateToTime(Date date) — Converts the given date to model time with respect to the start date, start time and model time unit settings.
* double differenceInCalendarUnits([time unit constant](constants-time-units.md), double time1, double time2) — Returns the difference (time2 — time1) between two model dates (corresponding to the given model times) in the given time units. Result is the number of date units that should be added to the model time time1 to obtain time2. The result may be negative and may have fractional part depending on the given dates.
* Date dropTime(Date date) — Drops time-of-the-day information and returns the same date but with the time being set to 00:00:00.000
* Date timeToDate(double t) — Converts the given model time to date with respect to the start date, start time and model time unit settings, returns null if the time is infinity.
* Date toDate(int year, int month, int day, int hourOfDay, int minute, int second) — Returns the date in the default time zone, constructed from the given components (year, month, day, etc.).
* long toDateInMillis(int year, int month, int day, int hourOfDay, int minute, int second) — Returns the date in the default time zone, constructed from the given components (year, month, day, etc.). Same as toDate(int, int, int, int, int, int) but returns the date as the number of milliseconds since January 1, 1970, 00:00:00 GMT.
* double toModelTime(double value, [time unit constant](constants-time-units.md)) — Converts the timeout (given as the number of specified time units) to the model time units. You define the timeout using the function arguments: first, you pass the value as the value argument, and then specify the time units using the second argument, units. For example, the model time units in your model are minutes. In this case the function call toModelTime(195, SECOND) will return 195/60 = 3.25.
* double toTimeoutInCalendar([time unit constant](constants-time-units.md), double amount) — Returns the amount of time (in model time units) from the current time to the (current time + a given number of days, months, years, etc.) with respect to daylight saving time. Use one of the [time unit constants](constants-time-units.md) as the units.

  Because of daylight saving time, the time interval from 8 AM today to 8 AM tomorrow is not always 24 \* hour() or 1 \* day(). Therefore, if you wish, for example, an event to occur at 8 AM every day, you should set the recurrence time to toTimeoutInCalendar( DAY, 1 ). Since toTimeoutInCalendar() function returns a value in model time units, you must choose your model’s time units from the drop-down list to the right of the field where you call toTimeoutInCalendar().
* double getTimeoutToNextTime(int hourOfDay, int minute, int second) — Returns timeout in model time units that is needed to reach the nearest date that will have the specified time.
* double toTimeUnits( double modelTimeValue, [time unit constant](constants-time-units.md)) — Converts the timeout (specified as the number of model time units) to the specified time units. For example, the model time units are minutes. In this case the function call toTimeUnits(5.5, SECOND) will return 5.5\*60 = 330.
