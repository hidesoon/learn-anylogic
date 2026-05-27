*来源 (Source): <https://anylogic.help/advanced/functions/gumbel1.html>*

---

# gumbel1

* [gumbel1(double a, double b)](#gumbel1double-a-double-b)
* [gumbel1(double a, double b, java.util.Random r)](#gumbel1double-a-double-b-javautilrandom-r)

[gumbel2](gumbel2.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

In probability theory, the Type-1 Gumbel distribution function is:

![](https://anylogic.help/advanced/functions/images/gumbel1.png)

The distribution is mainly used in the analysis of extreme values and in survival analysis (also known as duration analysis or event-history modelling).

###### Example

CDF is shown with a red line.

![](https://anylogic.help/advanced/functions/images/gumbel1_pdf.png)

## gumbel1(double a, double b)

Description
:   Generates a sample of the Type I Gumbel distribution.

Parameters
:   | Name | Type of value | Description |
    | --- | --- | --- |
    | a | double |  |
    | b | double |  |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## gumbel1(double a, double b, java.util.Random r)

Description
:   Generates a sample of the Type I Gumbel distribution using the specified random number generator.

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
