*来源 (Source): <https://anylogic.help/advanced/functions/gamma.html>*

---

# gamma

* [gamma(double alpha, double beta, double min)](#gammadouble-alpha-double-beta-double-min)
* [gamma(double alpha, double beta)](#gammadouble-alpha-double-beta)
* [gamma(double alpha, double beta, double min, java.util.Random r)](#gammadouble-alpha-double-beta-double-min-javautilrandom-r)

[gamma (truncated)](gamma-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/gamma.png)

The Gamma distribution is a continuous distribution bounded at the lower side. It has three distinct regions. For alpha = 1, beta = 1/lambda the Gamma distribution reduces to the [exponential(lambda)](exponential.md) distribution, starting at a finite value at minimum x and decreasing monotonically thereafter. For alpha < 1, the Gamma distribution tends to infinity at minimum x and decreases monotonically as x increases. For alpha > 1, the Gamma distribution is 0 at minimum x, peaks at a value that depends on both alpha and beta, decreasing monotonically thereafter. If alpha is restricted to positive integers, the Gamma distribution is reduced to the [Erlang](erlang.md) distribution.

The Gamma distribution also reduces to the [chi-squared](chi2.md) distribution for min = 0, beta = 2, and alpha = nμ/2. It can then be viewed as the distribution of the sum of squares of independent unit normal variables, with nµ degrees of freedom and is used in many statistical tests.

The Gamma distribution can also be used to approximate the [Normal](normal.md) distribution, for large alpha, while maintaining its strictly positive values of  (actually, (x - min)).

The Gamma distribution has been used to represent lifetimes, lead times, personal income data, a population about a stable equilibrium, interarrival times, and service times. In particular, it can represent lifetime with redundancy.

Examples of each of the regions of the Gamma distribution are shown above. Note the peak of the distribution moving away from the minimum value for increasing alpha, but with a much broader distribution.

* [Gamma distribution in Wikipedia](https://en.wikipedia.org/wiki/Gamma_distribution)

###### Examples

![](https://anylogic.help/advanced/functions/images/gamma_pdf.png)

![](https://anylogic.help/advanced/functions/images/gamma_pdf2.png)

## gamma(double alpha, double beta, double min)

Description
:   Generates a sample of the Gamma distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The shape parameter > 0. |
    | beta | double | The scale parameter > 0. |
    | min | double | The minimum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## gamma(double alpha, double beta)

Description
:   Generates a sample of the Gamma distribution with min set to 0. Is equivalent to gamma(alpha, beta, 0).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The shape parameter > 0 |
    | beta | double | The scale parameter > 0. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## gamma(double alpha, double beta, double min, java.util.Random r)

Description
:   Generates a sample of the Gamma distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | alpha | double | The shape parameter > 0. |
    | beta | double | The scale parameter > 0. |
    | min | double | The minimum x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
