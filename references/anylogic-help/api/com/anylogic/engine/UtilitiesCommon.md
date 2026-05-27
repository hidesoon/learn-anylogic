*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesCommon.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface UtilitiesCommon

---

```
@AnyLogicInternalAPI
public interface UtilitiesCommon
```

Various utilities, e.g. date calculations.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static long` | `addToDate(long dateInMillis, int timeUnit, double amount, Calendar context)` | Returns the date, which will be after the given `amount` of `timeUnit`s from the given date  e.g. |
| `static void` | `dropTime(Calendar c)` | Sets the given calendar to the time `00:00:00.000` |
| `static Date` | `dropTime(Date date, Calendar context)` | This utility method drops time-of-the-day information and returns the `date` with the time `00:00:00.000` |
| `static long` | `getDateWithTimeNextTo(long dateMillis, int hourOfDay, int minute, int second, Calendar context)` | Returns the date which the next date after the given `date` and has the specified time (in the default time zone) |
