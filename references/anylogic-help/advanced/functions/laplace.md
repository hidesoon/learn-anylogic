*来源 (Source): <https://anylogic.help/advanced/functions/laplace.html>*

---

# laplace

* [laplace(double phi, double theta)](#laplacedouble-phi-double-theta)
* [laplace(double phi, double theta, java.util.Random r)](#laplacedouble-phi-double-theta-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/laplace.png)

The Laplace distribution, sometimes called the double exponential distribution, is an unbounded continuous distribution that has a very sharp central peak, located at theta. The distribution scales with phi.

The Laplace distribution can be used to describe the difference between two independent, and equally distributed, exponents. It is also used in error analysis.

###### Example

phi = 1; theta = 0

![](https://anylogic.help/advanced/functions/images/laplace01.png)

## laplace(double phi, double theta)

Description
:   Generates a sample of the Laplace distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | phi | double | The scaling parameter. |
    | theta | double | The mode or central peak position. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## laplace(double phi, double theta, java.util.Random r)

Description
:   Generates a sample of the Laplace distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | phi | double | The scaling parameter. |
    | theta | double | The mode or central peak position. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
