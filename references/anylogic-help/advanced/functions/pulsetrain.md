*来源 (Source): <https://anylogic.help/advanced/functions/pulsetrain.html>*

---

# pulseTrain

[pulse](pulse.md)[step](step.md)

pulseTrain(double startTime, double pulseWidth, double timeBetweenPulses, double endTime) function returns 1, starting at startTime, and lasting for interval pulseWidth and then repeats this pattern every timeBetweenPulses time until endTime; 0 is returned at all other times.

If the value of timeBetweenPulses is smaller than pulseWidth then 1 will be returned between startTime and endTime.

The plot below illustrates how the function works:

![](https://anylogic.help/advanced/functions/images/pulseTrain.png)

#### Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | startTime | double | The first pulse start time. |
    | pulseWidth | double | The length of pulse time interval. |
    | timeBetweenPulses | double | The length of time interval between starts pulses. |
    | endTime | double | The end time of pulses, since this time the function returns 0. |

#### Result
:   | Type | Description |
    | --- | --- |
    | double | 1 for pulses, 0 otherwise. |

#### Units

startTime — time

pulseWidth — time

timeBetweenPulses — time

endTime — time

pulse() — dimensionless
