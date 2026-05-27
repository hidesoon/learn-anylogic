*来源 (Source): <https://anylogic.help/advanced/functions/time.html>*

---

# time

* [time()](#time-2)
* [time(units)](#timeunits)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

There are two notations: the simple one, time() returns the current model time as number of model time units simulated since the model start. Another, time(TIME\_UNIT) returns the number of specified time units simulated so far.

The function returns not the integer number, but a real value, e.g. 7.65.

### time()

Description
:   Returns the current model (logical) time. Time stays constant during an event execution and is only advanced between events.

Result
:   | Type | Description |
    | --- | --- |
    | double | Current model time. |

### time(units)

Description
:   Returns the current time as the number of specified time units simulated so far. You specify time units using the function argument. For example, time(MINUTE) returns the number of minutes simulated so far, the function time(DAY) - the number of simulated days, etc.

Parameter
:   | Name | Value | Description |
    | --- | --- | --- |
    | units | One of the following constants:  * MILLISECOND * SECOND * MINUTE * HOUR * DAY * WEEK * MONTH * YEAR | Defines the time units. |

Result
:   | Type | Description |
    | --- | --- |
    | double | Current model time, as the number of specified time units. |
