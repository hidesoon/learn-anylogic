*来源 (Source): <https://anylogic.help/advanced/functions/poisson.html>*

---

# poisson

* [poisson(double lambda)](#poissondouble-lambda)
* [poisson(double lambda, java.util.Random r)](#poissondouble-lambda-javautilrandom-r)

[poisson (truncated)](poisson-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

|  |  |
| --- | --- |
| Probability mass function |  |
| Distribution |  |
| Mean |  |
| Variance |  |

The Poisson distribution is a discrete distribution bounded at 0 on the low side and unbounded on the high side. The Poisson distribution is a limiting form of the [Hypergeometric](hypergeometric.md) distribution. The Poisson distribution finds frequent use, because it represents the infrequent occurrence of events whose rate is constant. This includes many types of events in time or space such as arrivals of telephone calls, defects in semiconductor manufacturing, defects in all aspects of quality control, molecular distributions, stellar distributions, geographical distributions of plants, shot noise, and so on. It is an important starting point in queuing theory and reliability theory.

The time between arrivals (defects) is exponentially distributed, which makes this distribution a particularly convenient starting point even when the process is more complex. The Poisson distribution peaks near lambda and falls off rapidly on either side.

###### Samples

![](https://anylogic.help/advanced/functions/images/poisson_samples.png)

## poisson(double lambda)

Description
:   Generates a sample of the Poisson distribution.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | lambda | double | The rate of occurrence. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## poisson(double lambda, java.util.Random r)

Description
:   Generates a sample of the Poisson distribution using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | lambda | double | The rate of occurrence. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

This document includes content from the *Stat::Fit User's Manual*. Copyright 2016 Geer Mountain Software Corp.
