*来源 (Source): <https://anylogic.help/advanced/functions/getdayofmonth.html>*

---

# getDayOfMonth

* [getDayOfMonth()](#getdayofmonth-2)
  + [Description](#description)
  + [Result](#result)
* [getDayOfMonth(Date date)](#getdayofmonthdate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getDayOfMonth()

### Description

Returns the day of the month of the current model date with respect to the start time/date and the model time unit.

The first day of the month has 1 as the value.

### Result

| Type | Description |
| --- | --- |
| int | The day of the month of the current model date with respect to the start time/date and the model time unit. |

## getDayOfMonth(Date date)

### Description

Returns the serial number of the day of the month of the specified date.

The first day of the month has 1 as the value.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The serial number of the day of the month of the specified date value. |
