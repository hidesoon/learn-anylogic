*来源 (Source): <https://anylogic.help/advanced/functions/totimeoutincalendar.html>*

---

# toTimeoutInCalendar

* [toTimeoutInCalendar(units, amount)](#totimeoutincalendarunits-amount)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### toTimeoutInCalendar(units, amount)

Description
:   Returns timeout, in model time units, which equals to the given amount of specified time units from current model date, e.g. toTimeoutInCalendar(DAY, 1) returns timeout in model time units from [date()](date.md) to the date() 1 day.

    The result of this method also depends on the current model date (because of leap years, different month lengths, daylight saving time tweaks) and therefore this method shouldn't be used for initialization of any constants.

    One of examples where this method should be used: A model scheduling an event occurring each day at fixed time (e.g. 8:00): this method will return correct timeout on each call (even when time is switched to daylight-saving mode) unlike [day()](day.md) which will always return timeout for 24 hours and may result in events scheduled at 7:00 or 9:00.

Parameter
:   | Name | Description |
    | --- | --- |
    | units | Defines the time units. Valid values:  * MILLISECOND * SECOND * MINUTE * HOUR * DAY * WEEK * MONTH * YEAR |
    | amount | The number of time units (may be negative, in this case result will be also negative). The real value of type double. |

Result
:   | Type | Description |
    | --- | --- |
    | double | Timeout, in model time units, which may be used e.g. to schedule an event in the given amount of specified time units. |
