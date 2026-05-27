*来源 (Source): <https://anylogic.help/advanced/functions/getsecond.html>*

---

# getSecond

* [getSecond()](#getsecond-2)
  + [Description](#description)
  + [Result](#result)
* [getSecond(Date date)](#getseconddate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getSecond()

### Description

Returns the second within the minute of the current model date with respect to the start time/date and the model time unit.

For example, at 10:04:15.250 PM the result is 15.

### Result

| Type | Description |
| --- | --- |
| int | The second within the minute of the current model date with respect to the start time/date and the model time unit. |

## getSecond(Date date)

### Description

Returns the second component of the specified date value.

For example, at 10:04:15.250 PM the result is 4.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The second component of the specified date value. |
