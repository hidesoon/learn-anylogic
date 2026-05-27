*来源 (Source): <https://anylogic.help/advanced/functions/hypergeometric.html>*

---

# hypergeometric

* [hypergeometric(int ss, int dn, int ps)](#hypergeometricint-ss-int-dn-int-ps)
* [hypergeometric(int ss, int dn, int ps, java.util.Random r)](#hypergeometricint-ss-int-dn-int-ps-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The hypergeometric distribution is a discrete distribution bounded by [0,s]. It describes the number of defects, x, in a sample of size s from a population of size N which has m total defects. The ratio of m/N = p is sometimes used rather than m to describe the probability of a defect.

Defects may be interpreted as successes, in which case x is the number of failures until (s-x) successes. The sample is taken without replacement.

The hypergeometric distribution is used to describe sampling from a population where an estimate of the total number of defects is desired. It has also been used to estimate the total population of species from a tagged subset. However, estimates of all three parameters from a data set are notoriously fickle and error prone, so use of these parameters to estimate a physical quantity without specifying at least one of the parameters is not recommended.

## hypergeometric(int ss, int dn, int ps)

Description
:   Generates a sample of the hypergeometric distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | ss | int | The sample size. |
    | dn | int | The number of defects in the population. |
    | ps | int | The size of the population. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## hypergeometric(int ss, int dn, int ps, java.util.Random r)

Description
:   Generates a sample of the hypergeometric distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | ss | int | The sample size. |
    | dn | int | The number of defects in the population. |
    | ps | int | The size of the population. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
