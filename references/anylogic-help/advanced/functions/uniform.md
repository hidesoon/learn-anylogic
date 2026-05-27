*来源 (Source): <https://anylogic.help/advanced/functions/uniform.html>*

---

# uniform

* [uniform()](#uniform-2)
* [uniform(java.util.Random r)](#uniformjavautilrandom-r)
* [uniform(double max)](#uniformdouble-max)
* [uniform(double min, double max)](#uniformdouble-min-double-max)
* [uniform(double min, double max, java.util.Random r)](#uniformdouble-min-double-max-javautilrandom-r)

[uniform\_discr](uniform-discr.md)[uniform-pos](uniform-pos.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/uniform.png)

The uniform distribution is a continuous distribution bounded on both sides, that is, the sample lays in the interval [min, max]. The probability density does not depend on the value of x. It is a special case of the [Beta](beta.md) distribution. It is frequently called rectangular distribution (see Johnson et al).

The uniform distribution is used to represent a random variable with constant likelihood of being in any small interval between min and max. Note that the probability of the maximum value is 0; the maximum point never occurs.

###### Sample

![](https://anylogic.help/advanced/functions/images/uniform01.png)

## uniform()

Description
:   Generates a random value uniformly distributed on the interval [0,1], the upper bound is not included.

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform(java.util.Random r)

Description
:   Generates a random value uniformly distributed on the interval [0,1], using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform(double max)

Description
:   Generates a sample of the uniform distribution on the interval [0, max]. Is equivalent to uniform(0, max). For more details, see uniform(double,double).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | max | double | The maximum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform(double min, double max)

Description
:   Generates a sample of the uniform distribution on the interval [min, max].

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform(double min, double max, java.util.Random r)

Description
:   Generates a sample of the uniform distribution on the interval [min, max] using the specified random number generator. For more details, see uniform(double,double).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | double | The minimum x value. |
    | max | double | The maximum x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | the generated sample. |

This document includes content from the *Stat::Fit User's Manual*. Copyright 2016 Geer Mountain Software Corp.
