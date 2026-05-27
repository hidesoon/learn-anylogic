*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/CustomDistributionDiscrete.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class CustomDistributionDiscrete

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.CustomDistributionAbstract](CustomDistributionAbstract.md "class in com.anylogic.engine")<E>

com.anylogic.engine.CustomDistributionDiscrete

All Implemented Interfaces:
:   `Serializable`

---

```
public class CustomDistributionDiscrete
extends CustomDistributionAbstract<E>
implements Serializable
```

This class is used to generate random numbers from a probability density
function (PDF) defined as a set of values of any type with corresponding rates.
You can supply the values and rates directly as a Map, as two lists with unique values and rates
or as a list with non-unique values.

For more information how to use get() function and set the random number generator see .

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.CustomDistributionDiscrete)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CustomDistributionDiscrete(double[] samples)` | Constructs a custom empirical distribution from array with occurrences. |
| `CustomDistributionDiscrete(double[] values, double[] weights)` | Constructs a custom empirical distribution from arrays of values and weights. |
| `CustomDistributionDiscrete(double[] values, double[] weights, Random random)` | Constructs a custom empirical distribution from arrays of values and weights. |
| `CustomDistributionDiscrete(double[] samples, Random random)` | Constructs a custom empirical distribution from array with occurrences. |
| `CustomDistributionDiscrete(Map<Double,Double> valuesWeightsMap, Random random)` | Constructs a custom empirical distribution from the given map with values and weights. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Double` | `get(Random r)` | Returns a random value according to distribution parameters and given random number generator. |
| `int` | `getInt(Random r)` | Returns a random integer according to distribution parameters, if possible. |
