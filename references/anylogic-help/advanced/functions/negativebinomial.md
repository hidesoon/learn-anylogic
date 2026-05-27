*来源 (Source): <https://anylogic.help/advanced/functions/negativebinomial.html>*

---

# negativeBinomial

* [negativeBinomial(double p, double n)](#negativebinomialdouble-p-double-n)
* [negativeBinomial(double p, double n, java.util.Random r)](#negativebinomialdouble-p-double-n-javautilrandom-r)

[negativeBinomial (truncated)](negativebinomial-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

|  |  |
| --- | --- |
| Probability mass function |  |
| Distribution |  |
| Mean |  |
| Variance |  |

The negative binomial distribution is a discrete distribution bounded on the low side at 0 and unbounded on the high side. The negative binomial distribution gives the number of failures before the n-th success in a sequence of independent Bernoulli trials with probability p of success on each trial.

The negative binomial distribution has many uses; some occur because it provides a good approximation for the sum or mixing of other discrete distributions. By itself, it is used to model accident statistics, birth-and-death processes, market research and consumer expenditure, lending library data, biometric data, and many others.

###### Examples

![](https://anylogic.help/advanced/functions/images/negativeBinomial_s.png)

## negativeBinomial(double p, double n)

Description
:   Generates a sample of the negative binomial distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | Probability of success on each trial. |
    | n | double | Number of desired successes. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## negativeBinomial(double p, double n, java.util.Random r)

Description
:   Generates a sample of the negative binomial distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | Probability of success on each trial. |
    | n | double | Number of desired successes. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
