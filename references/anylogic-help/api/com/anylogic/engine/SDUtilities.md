*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/SDUtilities.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class SDUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.SDUtilities

---

```
public class SDUtilities
extends Object
```

This class contains functions commonly used in System Dynamic modeling.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static double` | `getTableFunctionArea(TableFunction tableFunction, double start, double end)` | Returns the area under a `tableFunction` (with **linear interpolation** and **Nearest** out-of-range action) between `start` and `end`. |
| `static double` | `lookupBackward(TableFunction tableFunction, double x)` | For a `tableFunction` (with **linear interpolation** and **Nearest** out-of-range action) returns the value of the left point of interval for `x` value. |
| `static double` | `lookupExtrapolate(TableFunction tableFunction, double x)` | For a `tableFunction` (with **linear interpolation** and **Nearest** out-of-range action) returns the value for the given `x` using extrapolation if needed.  This function may be replaced with a call of `.get(x)` method for a table function with **Extrapolate** out-of-range action. |
| `static double` | `lookupForward(TableFunction tableFunction, double x)` | For a `tableFunction` (with **linear interpolation** and **Nearest** out-of-range action) returns the next value between arguments. |
| `static double` | `lookupInvert(TableFunction tableFunction, double y)` | Finds the input that, when used in the `tableFunction` (with **linear interpolation** and **Nearest** out-of-range action) would return `y`.  This function will find the first (smallest) value that satisfies this inverse relationship. |
| `static double` | `lookupSlope(TableFunction tableFunction, double x, double mode)` | Finds the slope at `x` in the `tableFunction` according to the given `mode`. |
