*来源 (Source): <https://anylogic.help/advanced/functions/randomfalse.html>*

---

# randomFalse

* [randomFalse(double p)](#randomfalsedouble-p)
* [randomFalse(double p, java.util.Random r)](#randomfalsedouble-p-javautilrandom-r)

[randomTrue](randomtrue.md)[Probability distributions](https://anylogic.help/anylogic/stochastic/probability-distributions.html)[Custom distribution](https://anylogic.help/anylogic/stochastic/custom-distribution.html)[Choose probability distribution wizard](https://anylogic.help/anylogic/stochastic/choose-pdf.html)

Returns false with the given probability p. Is equivalent to uniform() >= p. The probability of true is 1 - p correspondingly.

## randomFalse(double p)

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | p | double | The probability of false. |

Result
:   | Type | Description |
    | --- | --- |
    | boolean | false with probability p, true with probability 1 - p. |

## randomFalse(double p, java.util.Random r)

Returns false with the given probability p, using the specified random number generator.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | p | double | The probability of false. |
    | r | java.util.Random | The random number generator. |

Result
:   | Type | Description |
    | --- | --- |
    | boolean | false with probability p, true with probability 1 - p. |
