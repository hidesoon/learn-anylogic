*来源 (Source): <https://anylogic.help/advanced/functions/getmonth.html>*

---

# getMonth

* [getMonth()](#getmonth-2)
  + [Description](#description)
  + [Result](#result)
* [getMonth(Date date)](#getmonthdate-date)
  + [Description](#description-2)
  + [Parameter](#parameter)
  + [Result](#result-2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

## getMonth()

### Description

Returns the month of the current model date with respect to the start time/date and the model time unit.

This is a calendar-specific value.

The first month of the year in the Gregorian and Julian calendars is JANUARY which is 0. The last depends on the number of months in a year.

Valid values:

> 0 — JANUARY
> 1 — FEBRUARY
> 2 — MARCH
> 3 — APRIL
> 4 — MAY
> 5 — JUNE
> 6 — JULY
> 7 — AUGUST
> 8 — SEPTEMBER
> 9 — OCTOBER
> 10 — NOVEMBER
> 11 — DECEMBER
> 12 — UNDECIMBER (indicates the thirteenth month of the year. Although Gregorian calendar does not use this value, lunar calendars do).

### Result

| Type | Description |
| --- | --- |
| int | The month of the current model date with respect to the start time/date and the model time unit. |

## getMonth(Date date)

### Description

Returns the month component of the specified date.

This is a calendar-specific value.

The first month of the year in the Gregorian and Julian calendars is JANUARY which is 0. The last depends on the number of months in a year.

Valid values:

> 0 — JANUARY
> 1 — FEBRUARY
> 2 — MARCH
> 3 — APRIL
> 4 — MAY
> 5 — JUNE
> 6 — JULY
> 7 — AUGUST
> 8 — SEPTEMBER
> 9 — OCTOBER
> 10 — NOVEMBER
> 11 — DECEMBER
> 12 — UNDECIMBER (indicates the thirteenth month of the year. Although Gregorian calendar does not use this value, lunar calendars do).

### Parameter

| Name | Type of value | Description |
| --- | --- | --- |
| date | java.util.Date | A date, presented in the form of the Date Java class. |

### Result

| Type | Description |
| --- | --- |
| int | The month component of the specified date value. |
