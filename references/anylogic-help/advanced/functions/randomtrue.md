*来源 (Source): <https://anylogic.help/advanced/functions/randomtrue.html>*

---

# randomTrue

* [randomTrue(double p)](#randomtruedouble-p)
* [randomTrue(double p, java.util.Random r)](#randomtruedouble-p-javautilrandom-r)

[randomFalse](randomfalse.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

Returns true with the given probability p. Is equivalent to uniform() < p. The probability of false is 1 - p correspondingly.

## randomTrue(double p)

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | p | double | The probability of true. |

Result
:   | Type | Description |
    | --- | --- |
    | boolean | true with probability p, false with probability 1 - p. |

## randomTrue(double p, java.util.Random r)

Returns true with the given probability p, using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | p | double | The probability of true. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | boolean | true with probability p, false with probability 1 - p. |
