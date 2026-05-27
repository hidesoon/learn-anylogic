*来源 (Source): <https://anylogic.help/advanced/functions/gethour.html>*

---

# getHour

* [getHour()](#gethour-2)
  + [Description](#description)
  + [Result](#result)
* [getHour(Date date)](#gethourdate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getHour()

### Description

Returns the hour of the morning or afternoon of the current model date with respect to the start time/date and the model time unit.

This function is used for the 12-hour clock.

Noon and midnight are represented by 0, not by 12.

For example, at 10:04:15.250 PM the result is 10.

### Result

| Type | Description |
| --- | --- |
| int | The hour of the morning or afternoon of the current model date with respect to the start time/date and the model time unit. |

## getHour(Date date)

### Description

Returns the hour of the morning or afternoon of the specified date.

This function is used for the 12-hour clock.

Noon and midnight are represented by 0, not by 12.

For example, at 10:04:15.250 PM the result is 10.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The hour component of the specified date value, in the 12-hour format. |
