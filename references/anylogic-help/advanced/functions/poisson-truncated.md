*来源 (Source): <https://anylogic.help/advanced/functions/poisson-truncated.html>*

---

# poisson (truncated)

* [poisson(double min, double max, double mean, double shift, double stretch)](#poissondouble-min-double-max-double-mean-double-shift-double-stretch)
* [poisson(double min, double max, double mean, double shift, double stretch, java.util.Random r)](#poissondouble-min-double-max-double-mean-double-shift-double-stretch-javautilrandom-r)

[poisson](poisson.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The distribution poisson(mean) is stretched by the stretch coefficient, then shifted to the right by shift. After that it is truncated to fit into the [min, max] interval. Truncation is performed by discarding any sample outside this interval and taking the next try.

For more details, see [poisson()](poisson.md).

## poisson(double min, double max, double mean, double shift, double stretch)

Description
:   Generates a sample of the truncated Poisson distribution.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum value that this function will return. The distribution is truncated to return values above this. If the sample (stretched and shifted) is below this value, it will be discarded and another sample will be drawn. Use -infinity for “No limit”. |
    | max | double | The maximum value that this function will return. The distribution is truncated to return values below this. If the sample (stretched and shifted) is bigger than this value, it will be discarded and another sample will be drawn. Use infinity for “No limit”. |
    | mean | double | The mean value for the distribution = rate of event occurrence. |
    | shift | double | The shift parameter that indicates how much the (stretched) distribution will be shifted to the right. |
    | stretch | double | The stretch parameter that indicates how much the distribution will be stretched. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## poisson(double min, double max, double mean, double shift, double stretch, java.util.Random r)

Description
:   Generates a sample of the truncated Poisson distribution using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | mean | double | The mean value for the distribution = rate of event occurrence. |
    | shift | double | The shift parameter. |
    | stretch | double | The stretch parameter. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the *Stat::Fit User's Manual*. Copyright 2016 Geer Mountain Software Corp.
