*来源 (Source): <https://anylogic.help/advanced/functions/triangularav.html>*

---

# triangularAV

* [triangularAV(double average, double variability)](#triangularavdouble-average-double-variability)
* [triangularAV(double average, double variability, Random r)](#triangularavdouble-average-double-variability-random-r)

[triangular](triangular.md)[triangular (truncated)](triangular-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/triangularAV.png)

This function is used for specifying distribution in the form like “roughly this, +/- 20%”.

Is equivalent to triangular( average \* (1 - variability), average \* (1 variability) ).

## triangularAV(double average, double variability)

Description
:   Generates a sample of the triangular distribution with mode set to average.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | average | double | The most likely x value. |
    | variability | double | The percent [0...1] of average representing the half of distribution range, where the generated sample falls. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## triangularAV(double average, double variability, Random r)

Description
:   Generates a sample of the triangular distribution with mode set to average, and also uses the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | average | double | The most likely x value. |
    | variability | double | The percent [0...1] of average representing the half of the distribution range, where the generated sample falls. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |
