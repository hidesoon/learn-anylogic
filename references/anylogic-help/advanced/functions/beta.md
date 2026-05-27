*来源 (Source): <https://anylogic.help/advanced/functions/beta.html>*

---

# beta

* [beta(double p, double q, double min, double max)](#betadouble-p-double-q-double-min-double-max)
* [beta(double p, double q)](#betadouble-p-double-q)
* [beta(double p, double q, double min, double max, java.util.Random r)](#betadouble-p-double-q-double-min-double-max-javautilrandom-r)

[beta (truncated)](beta-truncated.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/beta.png)

The Beta distribution is a continuous distribution that has both upper and lower finite bounds. Because many real-world situations can be bounded in this way, the beta distribution can be used empirically to estimate the true distribution before much data is available. Even when data are available, the beta distribution should fit most data reasonably well, although it may not be the best fit. The uniform distribution is a special case of the beta distribution with p, q = 1.

The beta distribution can approach zero or infinity at either of its bounds, with p controlling the lower bound and q controlling the upper bound. Values of p, q < 1 cause the beta distribution to approach infinity at that bound. Values of p, q > 1 cause the beta distribution to be finite at that bound.

Beta distributions have many, many applications. As summarized in Johnson et al., beta distributions have been used to model distributions of hydrological variables, the logarithm of aerosol sizes, activity time in PERT analysis, insulation data in photovoltaic system analysis, porosity or void ratio of soil, phase derivatives in communication theory, size of offspring in Escherchia coli, dissipation rate in fracture models, proportions in gas mixtures, steady-state reflectivity, clutter, and power of radar signals, construction time, particle size, tool wear, and others. Many of these application arise because of the doubly bounded nature of the beta distribution.

![](https://anylogic.help/advanced/functions/images/beta_s.png)

## beta(double p, double q, double min, double max)

Description
:   Generates a sample of the beta distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The lower shape parameter > 0. |
    | q | double | The upper shape parameter > 0. |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## beta(double p, double q)

Description
:   Generates a sample of the beta distribution with min set to 0 and max set to 1. Is equivalent to beta(p, q, 0, 1).

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The lower shape parameter > 0. |
    | q | double | The upper shape parameter > 0. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## beta(double p, double q, double min, double max, java.util.Random r)

Description
:   Generates a sample of the beta distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | p | double | The lower shape parameter > 0. |
    | q | double | The shape factor (positive integer). |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
