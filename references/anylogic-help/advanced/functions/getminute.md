*来源 (Source): <https://anylogic.help/advanced/functions/getminute.html>*

---

# getMinute

* [getMinute()](#getminute-2)
  + [Description](#description)
  + [Result](#result)
* [getMinute(Date date)](#getminutedate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getMinute()

### Description

Returns the minute within the hour of the current model date with respect to the start time/date and the model time unit.

For example, at 10:04:15.250 PM the result is 4.

### Result

| Type | Description |
| --- | --- |
| int | The minute within the hour of the current model date with respect to the start time/date and the model time unit. |

## getMinute(Date date)

### Description

Returns the minute component of the specified date value.

For example, at 10:04:15.250 PM the result is 4.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The minute component of the specified date value. |
