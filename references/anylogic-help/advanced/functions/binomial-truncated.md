*来源 (Source): <https://anylogic.help/advanced/functions/binomial-truncated.html>*

---

# binomial (truncated)

* [binomial(double min, double max, double p, int n, double shift, double stretch)](#binomialdouble-min-double-max-double-p-int-n-double-shift-double-stretch)
* [binomial(double min, double max, double p, int n, double shift, double stretch, java.util.Random r)](#binomialdouble-min-double-max-double-p-int-n-double-shift-double-stretch-javautilrandom-r)

[binomial](binomial.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The distribution binomial(p, n) is stretched by the stretch coefficient, then shifted to the right by shift, after that it is truncated to fit into the [min, max] interval. Truncation is performed by discarding any sample outside this interval and taking the next try.

For more details, see [binomial()](binomial.md).

## binomial(double min, double max, double p, int n, double shift, double stretch)

Description
:   Generates a sample of the truncated binomial distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | min | double | The minimum value that this function will return. The distribution is truncated to return values above this. If the sample (stretched and shifted) is below this value, it will be discarded and another sample will be drawn. Use -infinity for “No limit”. |
    | max | double | The maximum value that this function will return. The distribution is truncated to return values below this. If the sample (stretched and shifted) is bigger than this value it will be discarded and another sample will be drawn. Use  infinity for “No limit”. |
    | p | double | The probability of the event occurrence. |
    | n | int | The number of trials. |
    | shift | double | The shift parameter that indicates how much the (stretched) distribution will be shifted to the right. |
    | stretch | double | The stretch parameter that indicates how much the distribution will be stretched. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

## binomial(double min, double max, double p, int n, double shift, double stretch, java.util.Random r)

Description
:   Generates a sample of the truncated binomial distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | p | double | The probability of the event occurrence. |
    | n | int | The number of trials. |
    | shift | double | The shift parameter. |
    | stretch | double | The stretch parameter. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | int | The generated sample. |

This document includes content from the “Stat::Fit User's Manual”. Copyright 2016 Geer Mountain Software Corp.
