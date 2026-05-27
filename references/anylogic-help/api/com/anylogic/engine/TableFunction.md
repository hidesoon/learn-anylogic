*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TableFunction.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TableFunction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.TableFunction

All Implemented Interfaces:
:   `Serializable`

---

```
public class TableFunction
extends Object
implements Serializable
```

Table function enables the user to define functions by giving a number of
(argument, value) pairs, i.e. a number of base points on a plot. Supports
various interpolation types. A call of get(x) will return a (possibly,
interpolated) value of the function. A number of behaviors are supported
for the case x is out of original argument range.
In case the function only supports discrete values (that were provided as
the argument set), and no interpolation is allowed, a call of get(x) with
x not matching any argument entry would result in exception thrown.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.TableFunction)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `TableFunction.InterpolationType` |  |
| `static enum` | `TableFunction.OutOfRangeAction` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final TableFunction.InterpolationType` | `INTERPOLATION_APPROXIMATION` |  |
| `static final TableFunction.InterpolationType` | `INTERPOLATION_LINEAR` |  |
| `static final TableFunction.InterpolationType` | `INTERPOLATION_NONE` |  |
| `static final TableFunction.InterpolationType` | `INTERPOLATION_SPLINE` |  |
| `static final TableFunction.InterpolationType` | `INTERPOLATION_STEP` |  |
| `static final TableFunction.OutOfRangeAction` | `OUTOFRANGE_CUSTOM` |  |
| `static final TableFunction.OutOfRangeAction` | `OUTOFRANGE_ERROR` |  |
| `static final TableFunction.OutOfRangeAction` | `OUTOFRANGE_EXTRAPOLATE` |  |
| `static final TableFunction.OutOfRangeAction` | `OUTOFRANGE_NEAREST` |  |
| `static final TableFunction.OutOfRangeAction` | `OUTOFRANGE_REPEAT` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TableFunction(double[] arguments, double[] values, TableFunction.InterpolationType interpolationtype, int approximationOrder, TableFunction.OutOfRangeAction outofrangeaction, double outofrangevalue)` | Creates a new table function with the given arguments, values, interpolation type and out of range behavior type. |
| `TableFunction(double[] arguments, double[] values, TableFunction.InterpolationType interpolationtype, TableFunction.OutOfRangeAction outofrangeaction, double outofrangevalue)` | Deprecated. please use [`TableFunction(double[], double[], InterpolationType, int, OutOfRangeAction, double)`](#%3Cinit%3E(double%5B%5D,double%5B%5D,com.anylogic.engine.TableFunction.InterpolationType,int,com.anylogic.engine.TableFunction.OutOfRangeAction,double)) constructor instead |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `CustomDistributionAbstract<Double>` | `createCustomDistribution()` | Constructs a custom distribution from the TableFunction. |
| `CustomDistributionAbstract<Double>` | `createCustomDistribution(Random random)` | Constructs a custom distribution from the TableFunction. |
| `double` | `get(double x)` | Returns the table function value corresponding to the given argument, subject to the currently set interpolation type and out of range handling. |
| `int` | `getApproximationOrder()` | The method returns the currently set order of the approximation polynomial used in the approximation mode. |
| `double[]` | `getArguments()` | Returns the (sorted) array of arguments. |
| `TableFunction.InterpolationType` | `getInterpolationType()` | Returns the current interpolation type of the table function. |
| `int` | `getLength()` | Returns the number of entries (rows) in the table function. |
| `double` | `getNextArgument(double x)` | Returns the value of the nearest argument that is strictly greater than x, respecting the possible table repeating. |
| `TableFunction.OutOfRangeAction` | `getOutOfRangeAction()` | Returns the current type of action performed for out of range arguments. |
| `double` | `getOutOfRangeDefaultValue()` | Returns the value that is returned by get(x) in case x is out of range when out of range action type is OUTOFRANGE\_CUSTOM. |
| `double[]` | `getValues()` | Returns the array of values corresponding to the (sorted) array of arguments. |
| `int` | `indexOf(double x)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Finds the interval between the two points on the argument axis [a,b[ where x belongs to and returns the index of the left point a. |
| `void` | `setApproximationOrder(int order)` | This method sets order of the approximation polynomial for the INTERPOLATION\_APPROXIMATION mode. |
| `void` | `setArgumentsAndValues(double[] arguments, double[] values)` | Sets the new argument and value arrays for the table function. |
| `void` | `setInterpolationType(TableFunction.InterpolationType type)` | Sets the new interpolation type for the table function. |
| `void` | `setOutOfRangeAction(TableFunction.OutOfRangeAction action)` | Sets the new action performed in case the argument provided in get() is out of range. |
| `void` | `setOutOfRangeDefaultValue(double value)` | Sets the value to be returned by get(x) in case x is out of range AND out of range action type is OUTOFRANGE\_CUSTOM. |
| `String` | `toString()` | Returns the textual representation of the table function. |
