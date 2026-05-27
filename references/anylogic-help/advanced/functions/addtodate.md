*来源 (Source): <https://anylogic.help/advanced/functions/addtodate.html>*

---

# addToDate

* [addToDate( date, timeUnit, amount )](#addtodate-date-timeunit-amount-)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### addToDate( date, timeUnit, amount )

Description
:   Returns the date, which will be after the given amount of given time units from the given date e.g. addToDate(date(), DAY, 1 ) returns the “tomorrow” date: (current date + 1 day ).

    This method correctly handles leap years, daylight saving time tweaks, e.g. its ( DAY, 1 ) may actually add to the date 23 or 25 hours during DST switch, in order to get the correct result

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | date | java.util.Date | The original date. |
    | timeUnit | Valid values:   MILLISECOND  SECOND  MINUTE  HOUR  DAY  WEEK  MONTH  YEAR | Defines the time units. |
    | amount | double | The number of time units (may be negative — in this case the returned date will be in the past relative to the given date). |

Result
:   | Type | Description |
    | --- | --- |
    | java.util.Date | The new date obtained by adding the given amount of specified time units to the original date. |
