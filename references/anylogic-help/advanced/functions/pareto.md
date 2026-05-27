*来源 (Source): <https://anylogic.help/advanced/functions/pareto.html>*

---

# pareto

* [pareto(double alpha, double min)](#paretodouble-alpha-double-min)
* [pareto(double alpha)](#paretodouble-alpha)
* [pareto(double alpha, double min, java.util.Random r)](#paretodouble-alpha-double-min-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

|  |  |
| --- | --- |
| PDF |  |
| CDF |  |
| Mode |  |

The Pareto distribution is a continuous distribution bounded on the lower side. It has a finite value at the minimum x and decreases monotonically for increasing x. A Pareto random variable is the exponential of an exponential random variable, and possesses many of the same characteristics.

The Pareto distribution has, historically, been used to represent the income distribution of a society. It is also used to model many empirical phenomena with very long right tails, such as city population sizes, occurrence of natural resources, stock price fluctuations, size of firms, brightness of comets, and error clustering in communication circuits.

The shape of the Pareto curve changes slowly with alpha, but the tail of the distribution increases dramatically with decreasing alpha.

###### Examples

![](https://anylogic.help/advanced/functions/images/pareto_s.png)

## pareto(double alpha, double min)

Description
:   Generates a sample of the Pareto distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The scale parameter > 0. |
    | min | double | The minimum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## pareto(double alpha)

Description
:   Generates a sample of the Pareto distribution with min set to 1. Is equivalent to pareto(alpha, 1).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The scale parameter > 0. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## pareto(double alpha, double min, java.util.Random r)

Description
:   Generates a sample of the Pareto distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The scale parameter > 0. |
    | min | double | The minimum x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
