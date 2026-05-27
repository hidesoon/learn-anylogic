*来源 (Source): <https://anylogic.help/advanced/functions/pert.html>*

---

# pert

* [pert(double min, double max, double mode)](#pertdouble-min-double-max-double-mode)
* [pert(double min, double max, double mode, java.util.Random r)](#pertdouble-min-double-max-double-mode-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The PERT distribution is a continuous distribution bounded on both sides. Being an alternative distribution to the triangular, it has the same three inputs (minimum, most likely, and Maximum), but is a smooth curve that puts less emphasis on extreme values. The PERT distribution is often used in risk analysis applications, for example, in Monte Carlo simulations to assess cost and project duration risks.

###### Samples (PDF, CDF)

![](https://anylogic.help/advanced/functions/images/pert_pdf.png)![](https://anylogic.help/advanced/functions/images/pert_pdf2.png)

## pert(double min, double max, double mode)

Description
:   Generates a sample of the PERT distribution.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | mode | double | The most likely x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## pert(double min, double max, double mode, java.util.Random r)

Description
:   Generates a sample of the PERT distribution using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | mode | double | The most likely x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |
