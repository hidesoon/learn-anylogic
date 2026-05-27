*来源 (Source): <https://anylogic.help/advanced/functions/triangular-truncated.html>*

---

# triangular (truncated)

* [triangular(double min, double max, double left, double mode, double right)](#triangulardouble-min-double-max-double-left-double-mode-double-right)
* [triangular(double min, double max, double left, double mode, double right, java.util.Random r)](#triangulardouble-min-double-max-double-left-double-mode-double-right-javautilrandom-r)

[triangular](triangular.md)[triangularAV](triangularav.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

The distribution triangular(left, right, mode) is stretched by the stretch coefficient, then shifted to the right by shift. After that, it is truncated to fit into the [min, max] interval. Truncation is performed by discarding any sample outside this interval and taking the next try.

For more details, see [triangular()](triangular.md).

## triangular(double min, double max, double left, double mode, double right)

Description
:   Generates a sample of the truncated triangular distribution.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum value that this function will return. The distribution is truncated to return values above this. If the sample (stretched and shifted) is below this value it will be discarded and another sample will be drawn. Use -infinity for “No limit”. |
    | max | double | The maximum value that this function will return. The distribution is truncated to return values below this. If the sample (stretched and shifted) is bigger than this value it will be discarded and another sample will be drawn. Use infinity for “No limit”. |
    | left | double | The minimum x value for triangular distribution. |
    | mode | double | The most likely x value for triangular distribution. |
    | right | double | The maximum x value for triangular distribution. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## triangular(double min, double max, double left, double mode, double right, java.util.Random r)

Description
:   Generates a sample of the truncated triangular distribution using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | left | double | The minimum x value for triangular distribution. |
    | mode | double | The most likely x value for triangular distribution. |
    | right | double | The maximum x value for triangular distribution. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

This document includes content from the *Stat::Fit User's Manual*. Copyright 2016 Geer Mountain Software Corp.
