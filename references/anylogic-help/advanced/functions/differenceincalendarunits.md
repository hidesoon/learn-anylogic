*来源 (Source): <https://anylogic.help/advanced/functions/differenceincalendarunits.html>*

---

# differenceInCalendarUnits

* [differenceInCalendarUnits(timeUnit, time1, time2)](#differenceincalendarunitstimeunit-time1-time2)
* [differenceInCalendarUnits(timeUnit, date1, date2)](#differenceincalendarunitstimeunit-date1-date2)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### differenceInCalendarUnits(timeUnit, time1, time2)

Description
:   Returns the difference (time2 - time1) between two model dates (corresponding to the given model times) in the given time units. Result is the number of time units that should be added to the model time time1 to obtain time2. The result may be negative and may have fractional part depending on the given.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | timeUnit | One of the following constants:  MILLISECOND  SECOND  MINUTE  HOUR  DAY  WEEK  MONTH  YEAR | Defines the time units. |
    | time1 | double | The first model time. |
    | time2 | double | The second model time. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The difference (time2 - time1) in the given time units. |

### differenceInCalendarUnits(timeUnit, date1, date2)

Description
:   Returns the difference (date2 - date1) between two given model dates in the given time units. Result is the number of time units that should be added to the model date date1 to obtain date2. The result may be negative and may have fractional part depending on the given dates.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | timeUnit | One of the following constants:  MILLISECOND  SECOND  MINUTE  HOUR  DAY  WEEK  MONTH  YEAR | Defines the time units. |
    | date1 | double | The first model date. |
    | date2 | double | The second model date. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The difference (time2 - time1) in the given time units. |
