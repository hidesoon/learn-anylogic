*来源 (Source): <https://anylogic.help/advanced/functions/geometric.html>*

---

# geometric

* [geometric(double p)](#geometricdouble-p)
* [geometric(double p, java.util.Random r)](#geometricdouble-p-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

|  |  |
| --- | --- |
| Probability mass function |  |
| Distribution |  |
| Mean |  |
| Variance |  |
| Mode | 0 |

The geometric distribution is a discrete distribution bounded at 0 and unbounded on the high side. It is a special case of the [negative binomial](negativebinomial.md) distribution. In particular, it is the direct discrete analog for the continuous [exponential](exponential.md) distribution. The geometric distribution has no history dependence, its probability at any value being independent of a shift along the axis.

The geometric distribution has been used for inventory demand, marketing survey returns, a ticket control problem, and meteorological models.

###### Examples

![](https://anylogic.help/advanced/functions/images/geometric_s.png)

## geometric(double p)

Description
:   Generates a sample of the geometric distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The probability of occurrence. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## geometric(double p, java.util.Random r)

Description
:   Generates a sample of the geometric distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The probability of occurrence. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
