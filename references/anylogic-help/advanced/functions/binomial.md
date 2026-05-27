*来源 (Source): <https://anylogic.help/advanced/functions/binomial.html>*

---

# binomial

* [binomial(double p, int n)](#binomialdouble-p-int-n)
* [binomial(double p)](#binomialdouble-p)
* [binomial(double p, int n, java.util.Random r)](#binomialdouble-p-int-n-javautilrandom-r)

[binomial (truncated)](binomial-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

|  |  |
| --- | --- |
| Probability mass function |  |
| Distribution |  |
| Mean |  |
| Variance |  |

The binomial distribution is a discrete distribution bounded by [0,n]. It is typically used when a single trial is repeated over and over, such as flipping a coin. The parameter, p, is the probability of the event, either heads or tails, either occurring or not occurring. Each single trial is assumed to be independent of all others. For large n, the binomial distribution may be approximated by the [normal](normal.md) distribution, for example, when np > 9 and p < 0.5 or when np(1-p) > 9.

As shown in the examples above, low values of p give high probabilities for low values of x and vice versa, so that the peak of the distribution may approach either bound. The binomial distribution has been extensively used in games, but is also useful in genetics, sampling for defective parts in a stable process, and other event sampling tests where the probability of the event is known to be constant or nearly so.

## binomial(double p, int n)

Description
:   Generates a sample of the binomial distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The probability of the event occurrence. |
    | n | int | The number of trials. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## binomial(double p)

Description
:   Generates a sample of the binomial distribution with n set to 1. Is equivalent to binomial(dd, 1).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The probability of the event occurrence. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## binomial(double p, int n, java.util.Random r)

Description
:   Generates a sample of the binomial distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The probability of the event occurrence. |
    | n | int | The number of trials. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
