*来源 (Source): <https://anylogic.help/advanced/functions/gethourofday.html>*

---

# getHourOfDay

* [getHourOfDay()](#gethourofday-2)
  + [Description](#description)
  + [Result](#result)
* [getHourOfDay(Date date)](#gethourofdaydate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getHourOfDay()

### Description

Returns the hour of day of the current model date with respect to the start time/date and the model time unit.

This function is used for the 24-hour clock. For example, at 10:04:15.250 PM the result is 22.

### Result

| Type | Description |
| --- | --- |
| int | The hour of day of the current model date with respect to the start time/date and the model time unit. |

## getHourOfDay(Date date)

### Description

Returns the hour of the day of the specified date.

This function is used for the 24-hour clock. For example, at 10:04:15.250 PM the result is 22.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The hour component of the specified date value, in the 24-hour format. |
