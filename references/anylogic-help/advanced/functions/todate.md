*来源 (Source): <https://anylogic.help/advanced/functions/todate.html>*

---

# toDate

* [toDate(year, month, day, hourOfDay, minute, second)](#todateyear-month-day-hourofday-minute-second)
* [toDate(year, month, day)](#todateyear-month-day)
* [toDate(dateFormat, text)](#todatedateformat-text)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### toDate(year, month, day, hourOfDay, minute, second)

Description
:   Returns the date in the default time zone, constructed from the given components (year, month, day, etc.).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | year | int | The year. |
    | month | int | The number of month (0-based. e.g., 0 for January)  You can use the following constants as a value:  JANUARY  FEBRUARY  MARCH  APRIL  MAY  JUNE  JULY  AUGUST  SEPTEMBER  OCTOBER  NOVEMBER  DECEMBER |
    | day | int | The day of the month. |
    | hourOfDay | int | The hour of day (using 24-hour clock). |
    | minute | int | The minute. |
    | second | int | The second. |

Result
:   | Type | Description |
    | --- | --- |
    | java.util.Date | The date in the default time zone, constructed from the given components (year, month, day, etc.). |

### toDate(year, month, day)

Description
:   Returns the date in the default time zone with the given field values and the time set to midnight.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | year | int | The year. |
    | month | int | The number of month (0-based. e.g., 0 for January).  You can use the following constants as a value:  JANUARY  FEBRUARY  MARCH  APRIL  MAY  JUNE  JULY  AUGUST  SEPTEMBER  OCTOBER  NOVEMBER  DECEMBER |
    | day | int | The day of the month. |

Result
:   | Type | Description |
    | --- | --- |
    | java.util.Date | The date in the default time zone, constructed from the given components (year, month, day). |

### toDate(dateFormat, text)

Description
:   Parses the date from the given string using the date format pattern. Throws an error if the format is wrong or the text cannot be parsed.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | dateFormat | String | The date format pattern, e.g. MM/dd/yyyy HH:ss. |
    | text | String | The text to be parsed as date. |

Result
:   | Type | Description |
    | --- | --- |
    | java.util.Date | The successfully parsed date. |
