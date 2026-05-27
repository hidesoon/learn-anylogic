*来源 (Source): <https://anylogic.help/advanced/functions/pulse.html>*

---

# pulse

[pulseTrain](pulsetrain.md)[step](step.md)

pulse(double startTime, double pulseWidth) function returns 1, starting at startTime, and lasting for interval pulseWidth; 0 is returned at all other times.

The plot below illustrates how the function works:

![](https://anylogic.help/advanced/functions/images/pulse.png)

#### Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | startTime | double | The pulse start time. |
    | pulseWidth | double | The length of pulse time interval. |

#### Result
:   | Type | Description |
    | --- | --- |
    | double | 1 for pulse (when time is within **[start, start width)**), otherwise 0. |

#### Units

startTime — time

pulseWidth — time

pulse() — dimensionless
