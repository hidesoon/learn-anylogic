*来源 (Source): <https://anylogic.help/advanced/functions/getdayofweek.html>*

---

# getDayOfWeek

* [getDayOfWeek()](#getdayofweek-2)
  + [Description](#description)
  + [Result](#result)
* [getDayOfWeek(Date date)](#getdayofweekdate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getDayOfWeek()

### Description

Returns an integer constant indicating the day of the week for the current model date. Possible return values are:

SUNDAY
MONDAY
TUESDAY
WEDNESDAY
THURSDAY
FRIDAY
SATURDAY

Days of the week are numbered from SUNDAY (1) to SATURDAY (7).

### Result

| Type | Description |
| --- | --- |
| int | An integer constant representing the day of the week for the current model date. |

## getDayOfWeek(Date date)

### Description

Returns an integer constant indicating the day of the week for the specified date. Possible return values are:

SUNDAY
MONDAY
TUESDAY
WEDNESDAY
THURSDAY
FRIDAY
SATURDAY

Days of the week are numbered from SUNDAY (1) to SATURDAY (7).

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | An integer constant representing the day of the week for the specified date. |
