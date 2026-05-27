*来源 (Source): <https://anylogic.help/advanced/functions/uniform-discr.html>*

---

# uniform\_discr

* [uniform\_discr(int max)](#uniformdiscrint-max)
* [uniform\_discr(int min, int max)](#uniformdiscrint-min-int-max)
* [uniform\_discr(int min, int max, java.util.Random r)](#uniformdiscrint-min-int-max-javautilrandom-r)

[uniform](uniform.md)[uniform\_pos](uniform-pos.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

![](https://anylogic.help/advanced/functions/images/uniform_discr.png)

The discrete uniform distribution is a discrete distribution bounded on [min, max] with constant probability at every value on or between the bounds. Sometimes called the discrete rectangular distribution, it arises when an event can have a finite and equally probable number of outcomes.

###### Sample

![](https://anylogic.help/advanced/functions/images/uniform_discr_s.png)

## uniform\_discr(int max)

Description
:   Generates a sample of the discrete uniform distribution in the interval [0, max], both 0 and max included! Is equivalent to uniform\_discr(0, max). For more details, see uniform\_discr(int, int).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | max | int | The maximum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform\_discr(int min, int max)

Description
:   Generates a sample of the discrete uniform distribution on the interval [min, max], both min and max included!

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | int | The minimum x value. |
    | max | int | The maximum x value. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |

## uniform\_discr(int min, int max, java.util.Random r)

Description
:   Generates a sample of the Discrete Uniform distribution on the interval [min, max] using the specified random number generator, both min and max included! For more details, see uniform\_discr(int, int).

Parameters

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | min | int | The minimum x value. |
    | max | int | The maximum x value. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | double | The generated sample. |
