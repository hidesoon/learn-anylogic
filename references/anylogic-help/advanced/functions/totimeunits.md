*来源 (Source): <https://anylogic.help/advanced/functions/totimeunits.html>*

---

# toTimeUnits

* [toTimeUnits(modelTimeValue, units)](#totimeunitsmodeltimevalue-units)

[Model time](https://anylogic.help/anylogic/experiments/model-time.html)[Time functions](time-functions.md)[API reference - Utilities class](https://anylogic.help/api/com/anylogic/engine/Utilities.html)

### toTimeUnits(modelTimeValue, units)

Description
:   Converts the timeout (specified as the number of model time units) to the specified time units. For example, the model time units are minutes. In this case the function call toTimeUnits(5.5, SECOND) will return 5.5\*60 = 330.

Parameter
:   | Name | Description |
    | --- | --- |
    | modelTimeValue | The time value as the number of model time units (real value of type double). |
    | units | Defines the time units. One of the following constants:  * MILLISECOND * SECOND * MINUTE * HOUR * DAY * WEEK * MONTH * YEAR |

Result
:   | Type | Description |
    | --- | --- |
    | double | The converted value in the given units. |
