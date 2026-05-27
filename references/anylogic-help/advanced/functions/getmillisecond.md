*来源 (Source): <https://anylogic.help/advanced/functions/getmillisecond.html>*

---

# getMillisecond

* [getMillisecond()](#getmillisecond-2)
  + [Description](#description)
  + [Result](#result)
* [getMillisecond(Date date)](#getmilliseconddate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getMillisecond()

### Description

Returns the millisecond within the second of the current model date with respect to the start time/date and the model time unit.

E.g., at 10:04:15.250 PM the result is 250.

### Result

| Type | Description |
| --- | --- |
| int | The millisecond within the second of the current model date with respect to the start time/date and the model time unit. |

## getMillisecond(Date date)

### Description

Returns the millisecond component of the specified date value.

For example, at 10:04:15.250 PM the result is 250.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The millisecond component of the specified date value. |
