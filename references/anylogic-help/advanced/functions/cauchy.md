*来源 (Source): <https://anylogic.help/advanced/functions/cauchy.html>*

---

# cauchy

* [cauchy(double lambda, double theta)](#cauchydouble-lambda-double-theta)
* [cauchy(double lambda)](#cauchydouble-lambda)
* [cauchy(double lambda, double theta, java.util.Random r)](#cauchydouble-lambda-double-theta-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/cauchy.png)

The Cauchy distribution is an unbounded continuous distribution that has a sharp central peak but significantly broad tails. The tails are much heavier than the tails of the [normal](normal.md) distribution.

The Cauchy distribution can be used to represent the ratio of two equally distributed parameters in certain cases, such as the ratio of two normal parameters. This distribution has no finite moments, due to its extensive tails. Therefore, it can also be used to highly skewed data as long as the data has a central tendency.

###### Example

lambda = 1; theta = 0

![](https://anylogic.help/advanced/functions/images/cauchy01.png)

## cauchy(double lambda, double theta)

Description
:   Generates a sample of the Cauchy distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | lambda | double | The scale parameter > 0. |
    | theta | double | The mode or central peak position. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## cauchy(double lambda)

Description
:   Generates a sample of the Cauchy distribution with theta set to 0. Is equivalent to cauchy(lambda, 0).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | lambda | double | The scale parameter > 0. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## cauchy(double lambda, double theta, java.util.Random r)

Description
:   Generates a sample of the Cauchy distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | lambda | double | The scale parameter > 0. |
    | theta | double | The mode or central peak position. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
