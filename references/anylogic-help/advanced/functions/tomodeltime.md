*来源 (Source): <https://anylogic.help/advanced/functions/tomodeltime.html>*

---

# toModelTime

* [toModelTime(value, units)](#tomodeltimevalue-units)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### toModelTime(value, units)

Description
:   Converts the timeout (given as the number of specified time units) to the model time units. You define the timeout using the function arguments: first, you pass the value as the value argument, and then specify the time units using the second argument, units. For example, the model time units in your model are minutes. In this case the function call toModelTime(195, SECOND) will return 195/60 = 3.25.

Parameters
:   | Name | Description |
    | --- | --- |
    | value | The time value in the given time units (you specify the time units using the second argument, units). |
    | units | Defines the time units.   Valid values:  MILLISECOND  SECOND  MINUTE  HOUR  DAY  WEEK  MONTH  YEAR |

Result
:   | Type | Description |
    | --- | --- |
    | double | The converted value in model time units. |
