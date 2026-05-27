*来源 (Source): <https://anylogic.help/advanced/functions/todateinmillis.html>*

---

# toDateInMillis

* [toDateInMillis( year, month, day, hourOfDay, minute, second )](#todateinmillis-year-month-day-hourofday-minute-second-)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### toDateInMillis( year, month, day, hourOfDay, minute, second )

Description
:   Returns the date in the default time zone, constructed from the given components (year, month, day, etc.). Same as [toDate(int, int, int, int, int, int)](todate.md) but returns the date as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | year | int | The year. |
    | month | int | The number of month (0-based. e.g., 0 for January). You can use the following constants as a value:  * JANUARY * FEBRUARY * MARCH * APRIL * MAY * JUNE * JULY * AUGUST * SEPTEMBER * OCTOBER * NOVEMBER * DECEMBER |
    | day | int | The day of the month. |
    | hourOfDay | int | The hour of day (using 24-hour clock). |
    | minute | int | The minute. |
    | second | int | The second. |

Result
:   | Type | Description |
    | --- | --- |
    | long | The number of milliseconds since January 1, 1970, 00:00:00 GMT up to the date in the default time zone, constructed from the given components (year, month, day, etc.). |
