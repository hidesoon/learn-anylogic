*来源 (Source): <https://anylogic.help/advanced/functions/getdatewithtimenextto.html>*

---

# getDateWithTimeNextTo

* [getDateWithTimeNextTo(date, hourOfDay, minute, second)](#getdatewithtimenexttodate-hourofday-minute-second)
  + [Description](#description)
  + [Parameters](#parameters)
  + [Result](#result)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getDateWithTimeNextTo(date, hourOfDay, minute, second)

### Description

Returns the next date after the given date, with the specified time in the default system time zone.

### Parameters

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | The date. |
| hourOfDay | int | The hour component of the time value, in the 24-hour format. |
| minute | int | The minute component of the time value. |
|
| second | int | The second component of the time value. |

### Result

| Type | Description |
| --- | --- |
| java.util.Date | The Date object defining the next date after the one specified in the parameter, with the given time value. |
