*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/CustomDistributionAbstract.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class CustomDistributionAbstract<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.CustomDistributionAbstract<E>

Type Parameters:
:   `E` - type of stored variables

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `CustomDistributionContinuous`, `CustomDistributionDiscrete`, `CustomDistributionOptions`

---

```
public abstract class CustomDistributionAbstract<E>
extends Object
implements Serializable
```

This abstract class is used to generate random numbers from a probability
density function (PDF) that is defined by the user. Each draw requires a
random number generator, so there are two different modes the
CustomDistributionAbstract can work:
1. You do not provide the RNG in the constructor, but supply it each time you
call get( Random ). In this case the CustomDistribution can safely be made
static and shared across multiple models and objects.
2. You provide the RNG with calling method setRandom(...) after the
constructor, the RNG is then remembered in the CustomDistributionAbstract and
you can use get() method without any parameters. This is simpler syntax, but
such CustomDistribution cannot be shared between models with different RNGs
used. The get( Random ) method can still be used in that case.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.CustomDistributionAbstract)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CustomDistributionAbstract()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `briefInfo()` |  |
| `E` | `get()` | Returns a random value according to distribution parameters. |
| `double` | `get(double min, double max, double shift, double stretch)` | Generates a sample of truncated custom distribution.  This method uses the random number generator set during construction and throws exception if no RNG was set.  This distribution is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `double` | `get(double min, double max, double shift, double stretch, Random rng)` | Generates a sample of truncated custom distribution.  This method requires a random number generator. |
| `abstract E` | `get(Random r)` | Returns a random value according to distribution parameters and given random number generator. |
| `int` | `getInt()` | Returns a random integer according to distribution parameters, if possible. |
| `abstract int` | `getInt(Random r)` | Returns a random integer according to distribution parameters, if possible. |
| `CustomDistributionAbstract<E>` | `setRandom(Random newRandom)` | Sets random number generator for distribution. |
| `String` | `toString()` | Returns the textual representation of the custom distribution. |
