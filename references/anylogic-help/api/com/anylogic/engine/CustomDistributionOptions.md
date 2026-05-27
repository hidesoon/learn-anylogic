*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/CustomDistributionOptions.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class CustomDistributionOptions<E extends Enum<?>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.CustomDistributionAbstract](CustomDistributionAbstract.md "class in com.anylogic.engine")<E>

com.anylogic.engine.CustomDistributionOptions<E>

All Implemented Interfaces:
:   `Serializable`

---

```
public class CustomDistributionOptions<E extends Enum<?>>
extends CustomDistributionAbstract<E>
implements Serializable
```

This class is used to generate random enum values from a probability density
function (PDF) defined as a set of values of any type with corresponding
rates. You can supply the values and rates directly as a Map, as two lists
with unique values and rates or as a list with non-unique values.
For more information how to use get() function and set the random number
generator see .

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.CustomDistributionOptions)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CustomDistributionOptions(E[] values)` | Constructs a custom empirical distribution from array with occurrences. |
| `CustomDistributionOptions(E[] values, double[] weights)` | Constructs a custom empirical distribution from arrays of values and weights. |
| `CustomDistributionOptions(E[] values, double[] weights, Random random)` | Constructs a custom empirical distribution from arrays of values and weights. |
| `CustomDistributionOptions(E[] values, Random random)` | Constructs a custom empirical distribution from array with occurrences. |
| `CustomDistributionOptions(Map<E,Double> valuesWeightsMap)` | Constructs a custom empirical distribution from the given map with values and weights. |
| `CustomDistributionOptions(Map<E,Double> valuesWeightsMap, Random random)` | Constructs a custom empirical distribution from the given map with values and weights. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `E` | `get(Random r)` | Returns a random value according to distribution parameters and given random number generator. |
| `int` | `getInt(Random r)` | Returns a random integer, representing enum ordinal, according to distribution, if it is possible. |
