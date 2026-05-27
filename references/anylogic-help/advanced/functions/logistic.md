*来源 (Source): <https://anylogic.help/advanced/functions/logistic.html>*

---

# logistic

* [logistic(double beta, double alpha)](#logisticdouble-beta-double-alpha)
* [logistic(double beta, double alpha, java.util.Random r)](#logisticdouble-beta-double-alpha-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/logistic.png)

The logistic distribution is an unbounded continuous distribution which is symmetrical about its mean [and shift parameter], alpha. The shape of the logistic distribution is very much like the [normal](normal.md) distribution, except that the logistic distribution has broader tails.

The logistic function is most often used a growth model: for populations, for weight gain, for business failure, and so on. The logistic distribution can be can be used to test for the suitability of such a model, with transformation to get back to the minimum and maximum values for the logistic function. Occasionally, the logistic function is used in place of the normal function where exceptional cases play a larger role.(see Johnson et. al.1)

###### Example

beta = 1; alpha = 0

![](https://anylogic.help/advanced/functions/images/logistic01.png)

## logistic(double beta, double alpha)

Description
:   Generates a sample of the logistic distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | beta | double | The scale parameter > 0. |
    | alpha | double | The shift parameter. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## logistic(double beta, double alpha, java.util.Random r)

Description
:   Generates a sample of the logistic distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | beta | double | The scale parameter > 0. |
    | alpha | double | The shift parameter. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
