*来源 (Source): <https://anylogic.help/advanced/functions/gumbel2.html>*

---

# gumbel2

* [gumbel2(double a, double b)](#gumbel2double-a-double-b)
* [gumbel2(double a, double b, java.util.Random r)](#gumbel2double-a-double-b-javautilrandom-r)

[gumbel1](gumbel1.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

In probability theory, the Type-2 Gumbel probability density function is:

![](https://anylogic.help/advanced/functions/images/gumbel2.png)

This implies that it is similar to the [Weibull](weibull.md) distributions, substituting ![](https://anylogic.help/advanced/functions/images/bjk.png) and a = -k. Note however that a positive k (as in the Weibull distribution) would yield a negative a, which is not allowed here as it would yield a negative probability density.

## gumbel2(double a, double b)

Description
:   Generates a sample of the Type-2 Gumbel distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | a | double |  |
    | b | double |  |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## gumbel2(double a, double b, java.util.Random r)

Description
:   Generates a sample of the Type-2 Gumbel distribution using the specified random number generator.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | a | double |  |
    | b | double |  |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |
