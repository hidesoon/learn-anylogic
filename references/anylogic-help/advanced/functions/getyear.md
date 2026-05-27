*来源 (Source): <https://anylogic.help/advanced/functions/getyear.html>*

---

# getYear

* [getYear()](#getyear-2)
  + [Description](#description)
  + [Result](#result)
* [getYear(Date date)](#getyeardate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getYear()

### Description

Returns the year of the current model date with respect to the start time/date and the model time unit.

This is a calendar-specific value.

### Result

| Type | Description |
| --- | --- |
| int | The year of the current model date with respect to the start time/date and the model time unit test. |

## getYear(Date date)

### Description

Returns the year component of the specified date.

This is a calendar-specific value.

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The year component of the specified date value. |
