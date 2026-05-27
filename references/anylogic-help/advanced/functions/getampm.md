*来源 (Source): <https://anylogic.help/advanced/functions/getampm.html>*

---

# getAmPm

* [getAmPm()](#getampm-2)
  + [Description](#description)
  + [Result](#result)
* [getAmPm(Date date)](#getampmdate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getAmPm()

### Description

Indicates whether the hour of the current model date with respect to the start time/date and the model time unit is before (AM) or after (PM) noon.

This function is used for the 12-hour clock.

Valid values:

> 0 — AM
> 1 — PM

For example, at 10:04:15.250 PM the result is 1.

### Result

| Type | Description |
| --- | --- |
| int | 0 or 1 depending on the hour of the current model date with respect to the start time/date and the model time unit. |

## getAmPm(Date date)

### Description

Indicates whether the hour of the specified date is before (AM) or after (PM) noon.

This function is used for the 12-hour clock.

Valid values:

> 0 — AM
> 1 — PM

For example, at 10:04:15.250 PM the result is 1.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The AM/PM part of the specified date value: 0 for AM, 1 for PM. |
