*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Utilities.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Utilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

com.anylogic.engine.Utilities

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

Direct Known Subclasses:
:   `Agent`, `Experiment`

---

```
public abstract class Utilities
extends Presentable
implements EnvironmentConstants, AgentConstants, UtilitiesRandom, UtilitiesMath, UtilitiesString, CodeValueExecutor
```

This class provides a lot of commonly used functions and constants, including the
probability distributions and mathematical functions. The class is a superclass
for [`Agent`](Agent.md "class in com.anylogic.engine") and [`Experiment`](Experiment.md "class in com.anylogic.engine"), so that its functions can be called without any
prefixing from any code written by the user within those subclasses.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Utilities)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final int` | `AM` | Value of the [`getAmPm(Date)`](#getAmPm(java.util.Date)) method indicating the period of the day from midnight to just before noon. |
| `static final int` | `APRIL` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the fourth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `AUGUST` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the eighth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `DECEMBER` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the twelfth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `FEBRUARY` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the second month of the year in the Gregorian and Julian calendars. |
| `static final int` | `FRIDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Friday. |
| `static final int` | `JANUARY` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the first month of the year in the Gregorian and Julian calendars. |
| `static final int` | `JULY` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the seventh month of the year in the Gregorian and Julian calendars. |
| `static final int` | `JUNE` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the sixth month of the year in the Gregorian and Julian calendars. |
| `static final LengthUnits` | `LENGTH_UNIT_CENTIMETER` |  |
| `static final LengthUnits` | `LENGTH_UNIT_FOOT` |  |
| `static final LengthUnits` | `LENGTH_UNIT_INCH` |  |
| `static final LengthUnits` | `LENGTH_UNIT_KILOMETER` |  |
| `static final LengthUnits` | `LENGTH_UNIT_METER` |  |
| `static final LengthUnits` | `LENGTH_UNIT_MILE` |  |
| `static final int` | `MARCH` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the third month of the year in the Gregorian and Julian calendars. |
| `static final int` | `MAY` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the fifth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `MONDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Monday. |
| `static final int` | `NOVEMBER` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the eleventh month of the year in the Gregorian and Julian calendars. |
| `static final int` | `OCTOBER` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the tenth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `PM` | Value of the [`getAmPm(Date)`](#getAmPm(java.util.Date)) method indicating the period of the day from noon to just before midnight. |
| `static final int` | `SATURDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Saturday. |
| `static final int` | `SEPTEMBER` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the ninth month of the year in the Gregorian and Julian calendars. |
| `static final int` | `SUNDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Sunday. |
| `static final int` | `THURSDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Thursday. |
| `static final long` | `TIME_UNIT_DAY` | One of the possible time units. |
| `static final long` | `TIME_UNIT_HOUR` | One of the possible time units. |
| `static final long` | `TIME_UNIT_MILLISECOND` | One of the possible time units. |
| `static final long` | `TIME_UNIT_MINUTE` | One of the possible time units. |
| `static final long` | `TIME_UNIT_MONTH` | One of the possible time units. |
| `static final long` | `TIME_UNIT_SECOND` | One of the possible time units. |
| `static final long` | `TIME_UNIT_WEEK` | One of the possible time units. |
| `static final long` | `TIME_UNIT_YEAR` | One of the possible time units. |
| `static final int` | `TUESDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Tuesday. |
| `static final int` | `UNDECIMBER` | Value of the [`getMonth(Date)`](#getMonth(java.util.Date)) method indicating the thirteenth month of the year. |
| `static final int` | `WEDNESDAY` | Value of the [`getDayOfWeek(Date)`](#getDayOfWeek(java.util.Date)) method indicating Wednesday. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Utilities()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static Date` | `addToDate(Date date, int timeUnit, double amount)` | Returns the date, which will be after the given `amount` of `timeUnit`s from the given date  e.g. |
| `static Date` | `addToDate(Date date, TimeUnits timeUnit, double amount)` | Returns the date, which will be after the given `amount` of `timeUnit`s from the given date  e.g. |
| `static double` | `atan2fast(double y, double x)` | Returns the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta). |
| `static int` | `bernoulli(double p, Random r)` | Generates a sample of the Bernoulli distribution using the specified random number generator. |
| `static double` | `beta(double min, double max, double p, double q, double shift, double stretch, Random r)` | Generates a sample of truncated Beta distribution using the specified random number generator.  Distribution `beta(p, q, 0, 1)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `beta(double p, double q, double min, double max, Random r)` | Generates a sample of the Beta distribution using the specified random number generator. |
| `static double` | `binomial(double min, double max, double p, double n, double shift, double stretch, Random r)` | Generates a sample of truncated Binomial distribution using the specified random number generator.  Distribution `binomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static int` | `binomial(double p, int n, Random r)` | Generates a sample of the Binomial distribution using the specified random number generator. |
| `static String` | `briefInfoOn(Object object)` | Returns a brief one-line textual information on the given object. |
| `<RT> RT` | `castNumberTypes(Number number, Class<RT> returnType)` | Deprecated. this method is internal and deprecated, and may be removed in future |
| `<RT> RT` | `castTypes(Object result, Class<RT> returnType)` | Deprecated. this method is internal and deprecated, and may be removed in future |
| `static Object` | `castTypesBack(Object value)` | Deprecated. this method is deprecated and may be removed in future |
| `static double` | `cauchy(double lambda, double theta, Random r)` | Generates a sample of the Cauchy distribution using the specified random number generator. |
| `static double` | `chi2(double nu, double min, Random r)` | Generates a sample of the Chi Squared distribution using the specified random number generator. |
| `static MarkupSegment[]` | `convertMarkupSegmentDescriptors_xjal(MarkupSegmentDescriptor[] descriptors)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `copyToClipboard(String text)` | Copies the given text to the system clipboard  Due to the security policy of the browser, the actual copying may be preceded by a prompt. |
| `static void` | `copyToClipboard(List<List<Object>> table)` | Deprecated. |
| `static void` | `copyToClipboard(List<List<Object>> table, List<Integer> sqlTypes)` |  |
| `TableElementDatabaseBuilder` | `createTableElementDatabaseBuilder()` |  |
| `static URL` | `createURL_xjal(String url)` | Creates an [`URL`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") object from the [`String`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") representation |
| `Date` | `date()` | Returns the current model date with respect to the start time/date and the model time unit. |
| `double` | `dateToTime(Date d)` | Converts the given date to model time with respect to the start date, start time and model time unit settings |
| `double` | `day()` | Returns a time value equal to 24-hour day according to the current time unit setting. |
| `DeleteQuery` | `deleteFrom(com.querydsl.sql.RelationalPathBase<?> table)` | Returns DeleteQuery that allows to build queries by chaining calls |
| `static double` | `difference(BasicDataSet ds1, BasicDataSet ds2)` | Difference function which is always not-negative and reflects difference between 2 given data sets in their common arguments range |
| `static double` | `difference(BasicDataSet ds, TableFunction f)` | Difference function which is always not-negative and reflects difference between given data set and table function in their common arguments range |
| `double` | `differenceInCalendarUnits(TimeUnits timeUnit, double time1, double time2)` | Returns the difference `(time2 - time1)` between two model dates (corresponding to the given model times) in the given time units.  Result is the number of date units that should be added to the model time `time1` to obtain `time2`  The result may be negative and may have fractional part depending on the given dates. |
| `static double` | `differenceInCalendarUnits(TimeUnits timeUnit, Date date1, Date date2)` | Returns the difference `(date2 - date1)` between two dates in the given time units.  Result is the number of time units that should be added to `date1` to obtain `date2`  The result may be negative and may have fractional part depending on the given dates. |
| `double` | `differenceInDateUnits(int timeUnit, double time1, double time2)` | Deprecated. |
| `static double` | `differenceInDateUnits(int timeUnit, Date date1, Date date2)` | Deprecated. |
| `double` | `differenceInDateUnits(TimeUnits timeUnit, double time1, double time2)` | Deprecated. please use [`differenceInCalendarUnits(TimeUnits, double, double)`](#differenceInCalendarUnits(com.anylogic.engine.TimeUnits,double,double)) instead |
| `static double` | `differenceInDateUnits(TimeUnits timeUnit, Date date1, Date date2)` | Deprecated. please use [`differenceInCalendarUnits(TimeUnits, Date, Date)`](#differenceInCalendarUnits(com.anylogic.engine.TimeUnits,java.util.Date,java.util.Date)) instead |
| `static double` | `dirToAngle(CellDirection dir)` | Returns the angle value corresponding to the given direction |
| `static Date` | `dropTime(Date date)` | This utility method drops time-of-the-day information and returns the `date` with the time `00:00:00.000` |
| `static double` | `erlang(double beta, int m, double min, Random r)` | Generates a sample of the Erlang distribution using the specified random number generator. |
| `RuntimeException` | `error(String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `RuntimeException` | `error(String errorTextFormat, Object... args)` | The same as [`error(String)`](#error(java.lang.String)) but allows error format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `abstract RuntimeException` | `error(Throwable cause, String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `RuntimeException` | `error(Throwable cause, String errorTextFormat, Object... args)` | The same as [`error(String)`](#error(java.lang.String)) but allows error format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `RuntimeException` | `errorInModel(String errorText)` | Signals an model logic error during the model run by throwing a ModelException with errorText preceded by the agent full name.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `RuntimeException` | `errorInModel(String errorTextFormat, Object... args)` | The same as [`errorInModel(String)`](#errorInModel(java.lang.String)) but allows error format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `abstract RuntimeException` | `errorInModel(Throwable cause, String errorText)` | Signals an model logic error during the model run by throwing a ModelException with errorText preceded by the agent full name.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `RuntimeException` | `errorInModel(Throwable cause, String errorTextFormat, Object... args)` | The same as [`errorInModel(String)`](#errorInModel(java.lang.String)) but allows error format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `void` | `executeAction(String code, Object... argDescriptors)` | Executes action. |
| `<T> T` | `executeExpression(Class<T> returnType, String code, Object... argDescriptors)` | Executes/evaluates the given code, e.g. |
| `<T> T` | `executeExpression(String code, Object... argDescriptors)` | Executes/evaluates the given code, e.g. |
| `int` | `executeStatement(String sql, Object... params)` | Executes insert, delete and update statements in AnyLogic database with given sql query string and parameters |
| `static double` | `exponential(double min, double max, double shift, double stretch, Random r)` | Generates a sample of truncated Exponential distribution using the specified random number generator.  Distribution `exponential(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `exponential(double lambda, double min, Random r)` | Generates a sample of the Exponential distribution using the specified random number generator. |
| `static String` | `findExistingFile(String filePath)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static String` | `format(boolean value)` | Formats a boolean value |
| `static String` | `format(char value)` | Formats a character to [`String`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") |
| `static String` | `format(double value)` | Formats a double value using the default AnyLogic formatter |
| `static String` | `format(double value, IUnits<?> units)` | Formats a double value with units, using the default AnyLogic formatter |
| `static String` | `format(int value)` | Formats an integer value using the default AnyLogic formatter |
| `static String` | `format(long value)` | Formats a long value using the default AnyLogic formatter |
| `static String` | `format(Date date)` | Formats a date using the default AnyLogic formatter |
| `static String` | `formatAmountUnits(double value, AmountUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatDayOfWeek(int dayOfWeek, boolean fullName)` | Returns the full or short name of the weekday |
| `static String` | `formatFlowRateUnits(double value, FlowRateUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatGeoHeading(double radians)` | Formats given heading angle (measured in radians CW, starting from North direction) as human-readable geographical heading (azimuth). |
| `static String` | `formatLatitude(double degrees)` | Formats latitude |
| `static String` | `formatLengthUnits(double value, LengthUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatLengthUnits(LengthUnits unit, boolean fullName)` | Returns the full or short name of the length units |
| `static String` | `formatLongitude(double degrees)` | Formats longitude |
| `static String` | `formatMonth(int month, boolean fullName)` | Returns the full or short name of the month |
| `static String` | `formatSpeedUnits(double value, SpeedUnits units)` | Converts value to required units and turns it into String |
| `String` | `formatTimeInterval(double dt)` | Returns a string representation of a given time interval, according to the current time unit settings, in the form 123 days 21h 0'56". |
| `static double` | `gamma(double min, double max, double alpha, double shift, double stretch, Random r)` | Generates a sample of truncated Gamma distribution using the specified random number generator.  Distribution `gamma(alpha, 1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `gamma(double alpha, double beta, double min, Random r)` | Generates a sample of the Gamma distribution using the specified random number generator. |
| `static double` | `gammaLog(double x)` | Returns the natural logarithm of the gamma function of `x`:  `ln(Γ(x))`.  The gamma function is an extension of the factorial function that works on all positive values of `x`.  If `n` is a positive integer, then: `Γ(n) = (n - 1)!`.    The `gammaLog` function may be useful in System Dynamics models for computing combinatorial factors. |
| `static int` | `geometric(double p, Random r)` | Generates a sample of the Geometric distribution using the specified random number generator. |
| `int` | `getAmPm()` | Indicates whether the hour of the current model date with respect to the start time/date and the model time unit is before (`AM`) or after (`PM`) noon.  This method is used for the 12-hour clock.  E.g., at 10:04:15.250 PM the result is `PM`. |
| `static int` | `getAmPm(Date date)` | Indicates whether the hour of the given `date` is before (`AM`) or after (`PM`) noon.  This method is used for the 12-hour clock.  E.g., at 10:04:15.250 PM the result is `PM`. |
| `static String` | `getCanonicalPath(File file)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Tries getting canonical path for the given file, on any error return absolute path |
| `Connection` | `getDatabaseConnection()` | Returns connection to AnyLogic database |
| `static Date` | `getDateWithTimeNextTo(Date date, int hourOfDay, int minute, int second)` | Returns the date which the next date after the given `date` and has the specified time (in the default time zone) |
| `int` | `getDayOfMonth()` | Returns the day of the month of the current model date with respect to the start time/date and the model time unit.  The first day of the month has value 1. |
| `static int` | `getDayOfMonth(Date date)` | Returns the day of the month of the given `date`.  The first day of the month has value 1. |
| `int` | `getDayOfWeek()` | Returns the day of the week of the current model date with respect to the start time/date and the model time unit.  Returned value is one of: `SUNDAY` `MONDAY` `TUESDAY` `WEDNESDAY` `THURSDAY` `FRIDAY` `SATURDAY` |
| `static int` | `getDayOfWeek(Date date)` | Returns the day of the week of the given `date`.  Returned value is one of: `SUNDAY` `MONDAY` `TUESDAY` `WEDNESDAY` `THURSDAY` `FRIDAY` `SATURDAY` |
| `static int` | `getDayOfYear(Date date)` | Returns the day of the year of the given `date`.  The first day of the year has value 1. |
| `Random` | `getDefaultRandomGenerator()` | Retrieves the random number generator used by all probability distributions by default, i.e. |
| `static final double` | `getDistance(double x1, double y1, double x2, double y2)` | Returns the distance between two given points `(x1, y1)` and `(x2, y2)` |
| `static final double` | `getDistance(double x1, double y1, double z1, double x2, double y2, double z2)` | Returns the distance between two given points `(x1, y1, z1)` and `(x2, y2, z2)` |
| `static final double` | `getDistanceFromPointToLine(double x1, double y1, double x2, double y2, double px, double py)` | Returns the distance from a point to a line. |
| `static final double` | `getDistanceFromPointToLineSq(double x1, double y1, double x2, double y2, double px, double py)` | Returns the square of the distance from a point to a line. |
| `static final double` | `getDistanceFromPointToSegment(double x1, double y1, double x2, double y2, double px, double py)` | Returns the distance from a point to a line segment. |
| `static final double` | `getDistanceFromPointToSegment(double x1, double y1, double z1, double x2, double y2, double z2, double px, double py, double pz)` | Returns the distance from a point to a line segment. |
| `static final double` | `getDistanceFromPointToSegmentSq(double x1, double y1, double x2, double y2, double px, double py)` | Returns the square of the distance from a point to a line segment. |
| `static final double` | `getDistanceFromPointToSegmentSq(double x1, double y1, double z1, double x2, double y2, double z2, double px, double py, double pz)` | Returns the square of the distance from a point to a line segment. |
| `static double` | `getDistanceGIS(double latitude1, double longitude1, double latitude2, double longitude2)` | Returns the distance measured in meters between two given points |
| `static double` | `getDistanceGIS(double latitude1, double longitude1, double latitude2, double longitude2, LengthUnits units)` | Returns the distance measured in meters between two given points |
| `static final double` | `getDistanceSq(double x1, double y1, double x2, double y2)` | Returns the square of the distance between two given points `(x1, y1)` and `(x2, y2)`.  This method is useful for comparing different distances, finding nearest point etc. |
| `static final double` | `getDistanceSq(double x1, double y1, double z1, double x2, double y2, double z2)` | Returns the square of the distance between two given points `(x1, y1, z1)` and `(x2, y2, z2)`.  This method is useful for comparing different distances, finding nearest point etc. |
| `static String` | `getFullName(Agent agent)` | Returns the name of the agent prefixed by the path from the top-level agent to this one. |
| `int` | `getHour()` | Returns the hour of the morning or afternoon of the current model date with respect to the start time/date and the model time unit.  This method is used for the 12-hour clock.  Noon and midnight are represented by 0, not by 12.  E.g., at 10:04:15.250 PM the result is 10. |
| `static int` | `getHour(Date date)` | Returns the hour of the morning or afternoon of the given `date`.  This method is used for the 12-hour clock.  Noon and midnight are represented by 0, not by 12.  E.g., at 10:04:15.250 PM the result is 10. |
| `int` | `getHourOfDay()` | Returns the hour of day of the current model date with respect to the start time/date and the model time unit.  This method is used for the 24-hour clock.  E.g., at 10:04:15.250 PM the result is 22. |
| `static int` | `getHourOfDay(Date date)` | Returns the hour of day of the given `date`.  This method is used for the 24-hour clock.  E.g., at 10:04:15.250 PM the result is 22. |
| `static final double` | `getLength(double dx, double dy)` | Returns the length of the vector `(dx, dy)` |
| `static final double` | `getLength(double dx, double dy, double dz)` | Returns the length of the vector `(dx, dy, dz)` |
| `static final double` | `getLengthSq(double dx, double dy)` | Returns the square of length of the vector `(dx, dy)` |
| `static final double` | `getLengthSq(double dx, double dy, double dz)` | Returns the square of length of the vector `(dx, dy, dz)` |
| `int` | `getMillisecond()` | Returns the millisecond within the second of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 250. |
| `static int` | `getMillisecond(Date date)` | Returns the millisecond within the second of the given `date`.  E.g., at 10:04:15.250 PM the result is 250. |
| `int` | `getMinute()` | Returns the minute within the hour of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 4. |
| `static int` | `getMinute(Date date)` | Returns the minute within the hour of the given `date`.  E.g., at 10:04:15.250 PM the result is 4. |
| `int` | `getMonth()` | Returns the month of the current model date with respect to the start time/date and the model time unit.  This is a calendar-specific value.  The first month of the year in the Gregorian and Julian calendars is `JANUARY` which is 0; the last depends on the number of months in a year.  Possible values: `JANUARY` `FEBRUARY` `MARCH` `APRIL` `MAY` `JUNE` `JULY` `AUGUST` `SEPTEMBER` `OCTOBER` `NOVEMBER` `DECEMBER` |
| `static int` | `getMonth(Date date)` | Returns the month of the given `date`.  This is a calendar-specific value.  The first month of the year in the Gregorian and Julian calendars is `JANUARY` which is 0; the last depends on the number of months in a year.  Possible values: `JANUARY` `FEBRUARY` `MARCH` `APRIL` `MAY` `JUNE` `JULY` `AUGUST` `SEPTEMBER` `OCTOBER` `NOVEMBER` `DECEMBER` |
| `static String` | `getName(Agent agent)` | Returns the name of the agent or `null` if the given agent is null.  This is a convenient function for formatting name of some agent when it may be `null`. |
| `static final Point` | `getNearestPointOnSegment(Point out, double x1, double y1, double x2, double y2, double px, double py)` | Finds a point on a segment that is closest to a given point. |
| `static final Point` | `getNearestPointOnSegment(Point out, double x1, double y1, double z1, double x2, double y2, double z2, double px, double py, double pz)` | Finds a point on a segment that is closest to a given point. |
| `static int` | `getPerformanceParallelWorkersCount_xjal()` | Returns number of processors (threads) when running parallel (multi-thread) experiments (with multiple runs) and some other features supporting parallel execution.  To get the number of processors reported by Java virtual machine, please use `Runtime.getRuntime().availableProcessors()` Please note that both methods shouldn't be generally used in the model logic because their results are inpredictable, not reproducible and depend on the underlying machine and AnyLogic installation |
| `<T> T` | `getRandom(Collection<T> collection)` | Same as `#randomFrom(Collection)` |
| `static <T> T` | `getRandom(Collection<T> collection, Random r)` | Same as `#randomFrom(Collection, Random)` |
| `<T> T` | `getResult(boolean cached, boolean mustBeUnique, Class<T> returnType, String sql, Object... params)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getSecond()` | Returns the second within the minute of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 15. |
| `static int` | `getSecond(Date date)` | Returns the second within the minute of the given `date`.  E.g., at 10:04:15.250 PM the result is 15. |
| `double` | `getTime()` | Deprecated. Use [`time()`](#time()) instead |
| `double` | `getTimeoutToNextTime(int hourOfDay, int minute, int second)` | Returns timeout, in model time units, to the nearest date which will have the specified in-day time (in the default time zone) |
| `int` | `getYear()` | Returns the year of the current model date with respect to the start time/date and the model time unit.  This is a calendar-specific value |
| `static int` | `getYear(Date date)` | Returns the year of the given `date`.  This is a calendar-specific value |
| `static double` | `gumbel1(double a, double b, Random r)` | Generates a sample of the Type I Gumbel distribution using the specified random number generator. |
| `static double` | `gumbel2(double a, double b, Random r)` | Generates a sample of the Type II Gumbel distribution using the specified random number generator. |
| `double` | `hour()` | Returns a time value equal to one hour according to the current time unit setting. |
| `static int` | `hypergeometric(int ss, int dn, int ps, Random r)` | Generates a sample of the Hypergeometric distribution using the specified random number generator. |
| `InsertQuery` | `insertInto(com.querydsl.sql.RelationalPathBase<?> table)` | Returns InsertQuery that allows to build queries by chaining calls |
| `static String` | `inspectOf(Object object)` | Returns a textual info on the object that can be displayed in the multi-line Inspect window. |
| `static String` | `inspectOfLink_xjal(Object object)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static boolean` | `isFinite(double v)` | Returns `true` if the given value is finite (not +/-infinity or NaN) |
| `static final boolean` | `isLineIntersectingLine(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4)` | Tests if the line segment from `(x1,y1)` to `(x2,y2)` intersects the line segment from `(x3,y3)` to `(x4,y4)`. |
| `static final boolean` | `isLineIntersectingRectangle(double x1, double y1, double x2, double y2, double rx, double ry, double rw, double rh)` | Check if the line intersects the given rectangle |
| `boolean` | `isLoggingClassToDB(LoggingType loggingType)` | Returns `true` if this agent type with all internals may log their data/changes/activity to AnyLogic built-in database (logging options are configurable in the properties of Database / Log in the Projects tree inside AnyLogic) |
| `boolean` | `isLoggingToDB(LoggingType loggingType)` | Returns `true` if this agent and its internals may log their data/changes/activity to AnyLogic built-in database (logging options are configurable in the properties of Database / Log in the Projects tree inside AnyLogic) |
| `static final boolean` | `isPointInsideRay(double x1, double y1, double x2, double y2, double px, double py)` | Tests if the specified point is inside the given ray. |
| `static final boolean` | `isPointInsideRectangle(double rx, double ry, double rw, double rh, double px, double py)` | Tests if the specified point is inside the given rectangle. |
| `static final boolean` | `isPointInsideSegment(double x1, double y1, double x2, double y2, double px, double py)` | Tests if the specified point is inside the given segment. |
| `static final boolean` | `isPointOnTheSameLine(double x1, double y1, double x2, double y2, double x3, double y3)` | Tests if the three point lie on the same line |
| `static final boolean` | `isRayIntersectingSegment(double rx1, double ry1, double rx2, double ry2, double sx1, double sy1, double sx2, double sy2)` | Tests if the ray from `(rx1,ry1)` in direction to `(rx2,ry2)` intersects the line segment from `(lx1,ly1)` to `(lx2,ly2)`. |
| `static int[]` | `joinArrays_xjal(boolean replaceAlways, boolean replaceWithNotEmpty, int[] a1, int[] a2)` | *This method is internal and isn't intended to be called by user (may be removed in future releases)* |
| `static double` | `laplace(double phi, double theta, Random r)` | Generates a sample of the Laplace distribution using the specified random number generator. |
| `static String` | `layoutTypeToString(LayoutType layoutType)` | Deprecated. please use [`LayoutType.formatName()`](LayoutType.md#formatName()) instead |
| `static double` | `limit(double min, double x, double max)` | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| `static int` | `limit(int min, int x, int max)` | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| `static double` | `limitMax(double x, double max)` | Returns x if it is less or equal to max, otherwise returns max. |
| `static int` | `limitMax(int x, int max)` | Returns x if it is less or equal to max, otherwise returns max. |
| `static double` | `limitMin(double min, double x)` | Returns x if it is greater or equal to min, otherwise returns min. |
| `static int` | `limitMin(int min, int x)` | Returns x if it is greater or equal to min, otherwise returns min. |
| `static int` | `logarithmic(double theta, Random r)` | Generates a sample of the Logarithmic distribution using the specified random number generator. |
| `static double` | `logistic(double beta, double alpha, Random r)` | Generates a sample of the Logistic distribution using the specified random number generator. |
| `static double` | `lognormal(double mu, double sigma, double min, Random r)` | Generates a sample of the Lognormal distribution using the specified random number generator. |
| `void` | `logToDB(DataSet dataSet, String name)` | Writes the given element to the corresponding log table of model database.  If logging is enabled this method should be called in `#onDestroy()` method |
| `void` | `logToDB(HistogramData histogramData, String name)` | Writes the given element to the corresponding log table of model database.  If logging is enabled this method should be called in `#onDestroy()` method |
| `void` | `logToDB(StatisticsContinuous statistics, String name)` | Writes the given element to the corresponding log table of model database.  If logging is enabled this method should be called in `#onDestroy()` method |
| `void` | `logToDB(StatisticsDiscrete statistics, String name)` | Writes the given element to the corresponding log table of model database.  If logging is enabled this method should be called in `#onDestroy()` method |
| `double` | `millisecond()` | Returns a time value equal to one millisecond according to the current time unit setting. |
| `double` | `minute()` | Returns a time value equal to one minute according to the current time unit setting. |
| `double` | `month()` | Returns a time value equal to 30 days according to the current time unit setting. |
| `static double` | `negativeBinomial(double min, double max, double p, double n, double shift, double stretch, Random r)` | Generates a sample of truncated Negative Binomial distribution using the specified random number generator.  Distribution `negativeBinomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static int` | `negativeBinomial(double p, double n, Random r)` | Generates a sample of the Negative Binomial distribution using the specified random number generator. |
| `static double` | `normal(double min, double max, double shift, double stretch, Random r)` | Generates a sample of truncated Normal distribution using the specified random number generator.  Distribution `normal(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `normal(double sigma, double mean, Random r)` | Generates a sample of the Normal distribution using the specified random number generator. |
| `static double` | `pareto(double alpha, double min, Random r)` | Generates a sample of the Pareto distribution using the specified random number generator. |
| `static double` | `pert(double min, double max, double mode, Random r)` | Generates a sample of the PERT distribution using the specified random number generator. |
| `static double` | `poisson(double min, double max, double mean, double shift, double stretch, Random r)` | Generates a sample of truncated Poisson distribution using the specified random number generator.  Distribution `poisson(mean)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static int` | `poisson(double lambda, Random r)` | Generates a sample of the Poisson distribution using the specified random number generator. |
| `static void` | `prepareBeforeExperimentStart_xjal(Class<?> experimentClass)` | *This method is internal and isn't intended to be called by user (may be removed in future releases)* |
| `PreparedStatement` | `prepareStatement(String sql, Object... params)` | Deprecated. this method is deprecated and may be removed in future |
| `double` | `pulse(double startTime, double pulseWidth)` | Returns `1`, starting at `startTime`, and lasting for interval `pulseWidth`; `0` is returned at all other times. |
| `double` | `pulseTrain(double startTime, double pulseWidth, double timeBetweenPulses, double endTime)` | Returns `1`, starting at `startTime`, and lasting for interval `pulseWidth` and then repeats this pattern every `timeBetweenPulses` time until `endTime`; `0` is returned at all other times.  If the value of `timeBetweenPulses` is smaller than `pulseWidth` then `1` will be returned between `startTime` and `endTime`. |
| `static double` | `quantum(double value, double quantizer)` | Returns the number smaller (by absolute value) than or equal to `value` that is an integer multiple of `quantizer`.  If `quantizer` is less than or equal to zero, then `value` is returned unchanged.  For example, `quantum(PI, 0.01)` will return `3.14` |
| `double` | `ramp(double slope, double startTime, double endTime)` | Returns `0` until the `startTime` and then slopes upward until `endTime` and then holds constant. |
| `Color` | `randomColor()` | Returns random standard color, one of possible standard colors |
| `static boolean` | `randomFalse(double p, Random r)` | Generates `false` with the given probability `p` using the specified random number generator.  For more details see [`UtilitiesRandom.randomFalse(double)`](UtilitiesRandom.md#randomFalse(double)) |
| `static <T extends Enum<T>> T` | `randomFrom(Class<T> enumeration, Random r)` | Returns the randomly chosen enumeration constant. |
| `static <T> T` | `randomFrom(Iterable<T> collection, Random r)` | Returns the randomly chosen element of the given collection. |
| `static <T> T` | `randomFrom(T[] array, Random r)` | Returns the randomly chosen element of the given array. |
| `static <T> T` | `randomlyCreate(Random r, Class<? extends T>... classes)` | Creates a randomly chosen object using one of the given constructors. |
| `static <T> T` | `randomlyCreate(Random r, Supplier<? extends T>... constructors)` | Creates a randomly chosen object using one of the given constructors. |
| `static boolean` | `randomTrue(double p, Random r)` | Generates `true` with the given probability `p` using the specified random number generator.  For more details see [`UtilitiesRandom.randomTrue(double)`](UtilitiesRandom.md#randomTrue(double)) |
| `static <T> T` | `randomWhere(Iterable<T> collection, Predicate<T> condition, Random r)` | Returns the randomly chosen element of the given collection which meets the given condition. |
| `static <T> T` | `randomWhere(T[] array, Predicate<T> condition, Random r)` | Returns the randomly chosen element of the given array which meets the given condition. |
| `static double` | `rayleigh(double sigma, double min, Random r)` | Generates a sample of the Rayleigh distribution using the specified random number generator. |
| `static double` | `roundToDecimal(double v, int nDecimalDigits)` | Rounds the value to the given precision. |
| `static int` | `roundToInt(double v)` | Returns `int` closest to the given value. |
| `double` | `second()` | Returns a time value equal to one second according to the current time unit setting. |
| `int` | `selectAndDoForEach(Consumer<ResultSet> action, String sql, Object... params)` | Perform some action with each of results for the given sql and params.  Example: |
| `double[]` | `selectArrayOfDouble(String sql, Object... params)` | Returns the array of numbers from the first column returned by the given sql and params. |
| `int[]` | `selectArrayOfInt(String sql, Object... params)` | Returns the array of numbers from the first column returned by the given sql and params. |
| `boolean` | `selectExists(boolean cached, String sql, Object... params)` | Returns `true` if the given sql and params returns at least one result This function caches its results, to speed up default behavior Use selectExists(false, sql, params) to get non cached result every time |
| `boolean` | `selectExists(String sql, Object... params)` | Returns `true` if the given sql and params returns at least one result This function caches its results, to speed up default behavior Use selectExists(false, sql, params) to get non cached result every time |
| `<T> T` | `selectFirstValue(boolean cached, Class<T> returnType, String sql, Object... params)` | Returns first result for given sql and params or null if no result is found This function caches its results, to speed up default behavior Use selectFirstValue(false, returnType, sql, params) to get non cached result every time |
| `<T> T` | `selectFirstValue(boolean cached, String sql, Object... params)` | Returns first result for given sql and params or null if no result is found |
| `<T> T` | `selectFirstValue(Class<T> returnType, String sql, Object... params)` | Returns first result for given sql and params or null if no result is found This function caches its results, to speed up default behavior Use selectFirstValue(false, returnType, sql, params) to get non cached result every time |
| `<T> T` | `selectFirstValue(String sql, Object... params)` | Returns first result for given sql and params or null if no result is found This function caches its results, to speed up default behavior Use selectFirstValue(false, sql, params) to get non cached result every time |
| `SelectQuery` | `selectFrom(com.querydsl.sql.RelationalPathBase<?> table)` | Returns SelectQuery that allows to build queries by chaining calls |
| `ResultSet` | `selectResultSet(String sql, Object... params)` | Get the results as a result set object for the given sql and params |
| `TableFunction` | `selectTableFunction(TableFunction tableFunction, String sql, Object... params)` | Executes the given SELECT query which should return data in 2 columns: the first column contains arguments numbers, the second column contains values numbers. |
| `<T> T` | `selectUniqueValue(boolean cached, Class<T> returnType, String sql, Object... params)` | Returns an unique result for given sql and params This function caches its results, to speed up default behavior Use selectUniqueValue(false, returnType, sql, params) to get non cached result every time |
| `<T> T` | `selectUniqueValue(boolean cached, String sql, Object... params)` | Returns an unique result for given sql and params This function caches its results, to speed up default behavior Use selectUniqueValue(false, sql, params) to get non cached result every time |
| `<T> T` | `selectUniqueValue(Class<T> returnType, String sql, Object... params)` | Returns an unique result for given sql and params This function caches its results, to speed up default behavior Use selectUniqueValue(false, returnType, sql, params) to get non cached result every time |
| `<T> T` | `selectUniqueValue(String sql, Object... params)` | Returns an unique result for given sql and params This function caches its results, to speed up default behavior Use selectUniqueValue(false, sql, params) to get non cached result every time |
| `<T> List<T>` | `selectValues(Class<T> returnType, String sql, Object... params)` | List the results for given sql and params Given sql query must return single column An empty list is returned for no results |
| `<T> List<T>` | `selectValues(String sql, Object... params)` | List the results for given sql and params Given sql query must return single column An empty list is returned for no results |
| `void` | `setDefaultRandomGenerator(Random r)` | Sets the random number generator used by all probability distributions by default, i.e. |
| `<T> T` | `sqlGetObject(ResultSet rs, int index, Class<T> returnType)` | Deprecated. this method is deprecated and may be removed in future |
| `<T> T` | `sqlGetObject(ResultSet rs, String columnLabel, Class<T> returnType)` | Deprecated. this method is deprecated and may be removed in future |
| `<T> T` | `sqlGetObject(ResultSet rs, int index, Class<T> returnType)` | Deprecated. this method is deprecated and may be removed in future |
| `<T> T` | `sqlGetObject(ResultSet rs, String columnLabel, Class<T> returnType)` | Deprecated. this method is deprecated and may be removed in future |
| `void` | `sqlSetObject(PreparedStatement st, int index, Object object)` | Deprecated. this method is deprecated and may be removed in future |
| `static double` | `sqr(double v)` | Returns the square of the given value (`v2`) |
| `double` | `step(double height, double stepTime)` | Returns `0` until the `stepTime` and then returns `height` |
| `double` | `time()` | Returns the current model (logical) time. |
| `double` | `time(TimeUnits units)` | Returns the current model (logical) time. |
| `Date` | `timeToDate(double t)` | Converts the given model time to date with respect to the start date, start time and model time unit settings, null if the time is infinity. |
| `static Date` | `toDate(int year, int month, int day)` | Returns the date in the default time zone with given field values and the time set to a midnight. |
| `static Date` | `toDate(int year, int month, int day, int hourOfDay, int minute, int second)` | Returns the date in the default time zone with given field values. |
| `static Date` | `toDate(String dateFormat, String text)` | Parses the date from the given string using date format pattern. |
| `static long` | `toDateInMillis(int year, int month, int day, int hourOfDay, int minute, int second)` | Same as [`toDate(int, int, int, int, int, int)`](#toDate(int,int,int,int,int,int)) but returns the date in its milliseconds representation (see [`Date.getTime()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html#getTime() "class or interface in java.util")), i.e. |
| `static double` | `toLatitude(int degrees, int minutes, double seconds, boolean northOrSouth)` | Converts latitude from human-readable format (e.g. |
| `static double` | `toLongitude(int degrees, int minutes, double seconds, boolean eastOrWest)` | Converts longitude from human-readable format (e.g. |
| `double` | `toModelRate(double value, RateUnits units)` | Converts the given rate (in rate units) to units based on model time units (used e.g. |
| `double` | `toModelTime(double value, TimeUnits units)` | Converts the given timeout (in units) to model time units (used e.g. |
| `double` | `toRateUnits(double modelRateValue, RateUnits units)` | Converts the rate (in units based on model time units) to the given units |
| `static String` | `toStringAlignedNameValues(int minNameLength, Object... nameValueRows)` |  |
| `double` | `toTimeout(int timeUnit, double amount)` | Deprecated. |
| `double` | `toTimeout(TimeUnits timeUnit, double amount)` | Deprecated. please use [`toTimeoutInCalendar(TimeUnits, double)`](#toTimeoutInCalendar(com.anylogic.engine.TimeUnits,double)) instead |
| `double` | `toTimeoutInCalendar(TimeUnits timeUnit, double amount)` | Returns timeout, in model time units, which equals to the given `amount` of `timeUnit`s from current model date  e.g. |
| `double` | `toTimeUnits(double modelTimeValue, TimeUnits units)` | Converts the timeout (in model time units) to the given units |
| `static void` | `trace(Object o)` | Prints a string representation of an object to the standard output stream. |
| `static void` | `trace(String textFormat, Object... args)` | The same as [`trace(Object)`](#trace(java.lang.Object)) but allows text format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `static void` | `traceln()` | Prints a line delimiter to the standard output stream. |
| `static void` | `traceln(Color color, Object o)` | Prints a string representation of an object with a line delimiter at the end to the standard output stream. |
| `static void` | `traceln(Color color, String textFormat, Object... args)` | The same as [`traceln(Object)`](#traceln(java.lang.Object)) but allows text format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method. |
| `static void` | `traceln(Object o)` | Prints a string representation of an object with a line delimiter at the end to the standard output stream. |
| `static void` | `traceln(String textFormat, Object... args)` | The same as [`traceln(Object)`](#traceln(java.lang.Object)) but allows text format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `void` | `traceToDB(Object o)` | Prints a string representation of an object with a line delimiter at the end to the standard output stream. |
| `void` | `traceToDB(String textFormat, Object... args)` | The same as [`traceln(Object)`](#traceln(java.lang.Object)) but allows text format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `static double` | `triangular(double min, double max, double left, double mode, double right, Random r)` | Generates a sample of truncated Triangular distribution using the specified random number generator.  Distribution `triangular(left, right, mode)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `triangular(double min, double max, double mode, Random r)` | Generates a sample of the Triangular distribution using the specified random number generator. |
| `static double` | `triangularAV(double average, double variability, Random r)` | Generates a sample of the Triangular distribution with `mode` set to `average`.  Defines distribution in the form like "roughly this, +/-20%".  Is equivalent to `triangular( average * (1 - variability), average * (1 + variability) )` . |
| `static double` | `uniform(double min, double max, Random r)` | Generates a sample of the Uniform distribution on the interval [min, max) using the specified random number generator. |
| `static double` | `uniform(Random r)` | Generates a random value uniformly distributed on the interval [0,1), using the specified random number generator. |
| `static int` | `uniform_discr(int min, int max, Random r)` | Generates a sample of the Discrete Uniform distribution on the interval [min, max] using the specified random number generator, both 0 and max included! For more details see [`UtilitiesRandom.uniform_discr(int,int)`](UtilitiesRandom.md#uniform_discr(int,int)). |
| `static double` | `uniform_pos(Random r)` | Generates a positive random value uniformly distributed on the interval (0,1), using the specified random number generator. |
| `UpdateQuery` | `update(com.querydsl.sql.RelationalPathBase<?> table)` | Returns UpdateQuery that allows to build queries by chaining calls |
| `abstract void` | `warning(String warningText)` | Signals a warning during the model run with warningText preceded by the agent full name.  Warnings may be turned off in the AnyLogic preferences (runtime section) or by API: [`AnyLogicRuntimePreferences.setEnableWarnings(Boolean)`](AnyLogicRuntimePreferences.md#setEnableWarnings(java.lang.Boolean)).  This method checks against numerous warnings output: In case of multiple warnings having equal `warningText`, only the first 10 of them are displayed. |
| `abstract void` | `warning(String warningTextFormat, Object... args)` | Signals a warning during the model run with warningText preceded by the agent full name. |
| `double` | `week()` | Returns a time value equal to one week according to the current time unit setting. |
| `static double` | `weibull(double min, double max, double alpha, double shift, double stretch, Random r)` | Generates a sample of truncated Weibull distribution using the specified random number generator.  Distribution `weibull(alpha, stretch, 0)` is shifted to the right by `shift` and then truncated to fit in `[min, max]` interval. |
| `static double` | `weibull(double alpha, double beta, double min, Random r)` | Generates a sample of the Weibull distribution using the specified random number generator. |
| `static double` | `xidz(double a, double b, double x)` | Tries to divide the first argument by the second. |
| `double` | `year()` | Returns a time value equal to 365 days according to the current time unit setting. |
| `static double` | `zidz(double a, double b)` | Tries to divide the first argument by the second. |
