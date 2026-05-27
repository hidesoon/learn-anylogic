*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/CustomDistributionContinuous.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class CustomDistributionContinuous

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.CustomDistributionAbstract](CustomDistributionAbstract.md "class in com.anylogic.engine")<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang")>

com.anylogic.engine.CustomDistributionContinuous

All Implemented Interfaces:
:   `Serializable`

---

```
public class CustomDistributionContinuous
extends CustomDistributionAbstract<Double>
implements Serializable
```

This class is used to generate random numbers from a probability density
function (PDF) defined as:
- piecewise linear function. Piecewise linear function is defined by values and corresponding weights.
- set of ranges with corresponding weights
- set of samples
Despite that this function defined with discrete number of values, it has continuous nature.

For more information how to use get() function and set the random number generator see .

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.CustomDistributionContinuous)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CustomDistributionContinuous(double[] samples)` | Constructs a custom empirical distribution from array with occurrences. |
| `CustomDistributionContinuous(double[] values, double[] weights)` | Constructs a custom distribution from the given arrays of values and weights. |
| `CustomDistributionContinuous(double[] starts, double[] ends, double[] weights)` | Constructs a custom distribution from the given arrays of starts, ends and weights.  The distribution for the intersect ranges has no sense, thus each range shouldn't intersect with other ranges. |
| `CustomDistributionContinuous(double[] starts, double[] ends, double[] weights, Random random)` | Constructs a custom distribution from the given arrays of starts, ends and weights.  The distribution for the intersect ranges has no sense, thus each range shouldn't intersect with other ranges. |
| `CustomDistributionContinuous(double[] values, double[] weights, Random random)` | Constructs a custom distribution from the given arrays of points and rates. |
| `CustomDistributionContinuous(double[] samples, Random random)` | Constructs a custom empirical distribution from array with occurrences. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Double` | `get(Random r)` | Returns a random value according to distribution parameters and given random number generator. |
| `int` | `getInt(Random r)` | Returns a random integer according to distribution parameters, if possible. |
