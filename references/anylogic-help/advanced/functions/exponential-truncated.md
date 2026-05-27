*来源 (Source): <https://anylogic.help/advanced/functions/exponential-truncated.html>*

---

# exponential (truncated)

* [exponential(double min, double max, double shift, double stretch)](#exponentialdouble-min-double-max-double-shift-double-stretch)
* [exponential(double min, double max, double shift, double stretch, java.util.Random r)](#exponentialdouble-min-double-max-double-shift-double-stretch-javautilrandom-r)

[exponential](exponential.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The distribution exponential(1, 0) is stretched by the stretch coefficient, then shifted to the right by shift. After that, it is truncated to fit into the [min, max] interval. Truncation is performed by discarding any sample outside this interval and taking the next try.

For more details, see [exponential()](exponential.md).

## exponential(double min, double max, double shift, double stretch)

Description
:   Generates a sample of the truncated exponential distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | min | double | The minimum value that this function will return. The distribution is truncated to return values above this. If the sample (stretched and shifted) is below this value, it will be discarded and another sample will be drawn. Use -infinity for “No limit”. |
    | max | double | The maximum value that this function will return. The distribution is truncated to return values below this. If the sample (stretched and shifted) is bigger than this value, it will be discarded and another sample will be drawn. Use infinity for “No limit”. |
    | shift | double | The shift parameter that indicates how much the (stretched) distribution will be shifted to the right. |
    | stretch | double | The stretch parameter that indicates how much the distribution will be stretched. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## exponential(double min, double max, double shift, double stretch, java.util.Random r)

Description
:   Generates a sample of the truncated exponential distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | shift | double | The shift parameter. |
    | stretch | double | The stretch parameter. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the “Stat::Fit User’s Manual”. Copyright 2016 Geer Mountain Software Corp.
