*来源 (Source): <https://anylogic.help/advanced/functions/rayleigh.html>*

---

# rayleigh

* [rayleigh(double sigma, double min)](#rayleighdouble-sigma-double-min)
* [rayleigh(double sigma)](#rayleighdouble-sigma)
* [rayleigh(double sigma, double min, java.util.Random r)](#rayleighdouble-sigma-double-min-javautilrandom-r)

[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/rayleigh.png)

The Rayleigh distribution is a continuous distribution bounded on the lower side. It is a special case of the [Weibull](weibull.md) distribution with alpha = 2 and beta/sqrt(2) = sigma. Because of the fixed shape parameter, the Rayleigh distribution does not change shape although it can be scaled. The Rayleigh distribution is frequently used to represent lifetimes because its hazard rate increases linearly with time, for example, the lifetime of vacuum tubes. This distribution also finds application in noise problems in communications.

###### Sample

sigma = 1; min = 0

![](https://anylogic.help/advanced/functions/images/rayleigh01.png)

## rayleigh(double sigma, double min)

Description
:   Generates a sample of the Rayleigh distribution.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | sigma | double | The scale parameter > 0. |
    | min | double | The minimum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## rayleigh(double sigma)

Description
:   Generates a sample of the Rayleigh distribution with min set to 0. Is equivalent to rayleigh(sigma, 0).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | sigma | double | The scale parameter > 0. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## rayleigh(double sigma, double min, java.util.Random r)

Description
:   Generates a sample of the Rayleigh distribution using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | sigma | double | The scale parameter > 0. |
    | min | double | The minimum x value- |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the *Stat::Fit User's Manual*. Copyright 2016 Geer Mountain Software Corp.
