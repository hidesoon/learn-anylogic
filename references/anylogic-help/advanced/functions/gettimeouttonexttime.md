*来源 (Source): <https://anylogic.help/advanced/functions/gettimeouttonexttime.html>*

---

# getTimeoutToNextTime

* [getTimeoutToNextTime(hourOfDay, minute, second)](#gettimeouttonexttimehourofday-minute-second)
  + [Description](#description)
  + [Parameters](#parameters)
  + [Result](#result)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getTimeoutToNextTime(hourOfDay, minute, second)

### Description

Returns the timeout (in model time units) that is needed to reach the nearest date that will have the specified time. You can use the resulting value for various purposes, for example, scheduling events.

### Parameters

| Name | Type of value | Description |
| --- | --- | --- |
| hourOfDay | int | The hour component of the time value, in the 24-hour format. |
| minute | int | The minute component of the time value. |
|
| second | int | The second component of the time value. |

### Result

| Type | Description |
| --- | --- |
| double | The timeout value in model time units. |
