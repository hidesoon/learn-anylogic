*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesMath.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface UtilitiesMath

All Known Implementing Classes:
:   `Agent`, `Experiment`, `ExperimentCompareRuns`, `ExperimentMultipleRuns`, `ExperimentOptimization`, `ExperimentParamVariation`, `ExperimentRunFast`, `ExperimentSimulation`, `FlowchartBlock`, `Utilities`

---

```
public interface UtilitiesMath
```

Various math utilities

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final double` | `infinity` | A constant holding the positive infinity of type `double`.  If you want to get negative infinity, please write `-infinity` |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static double` | `atan2fast(double y, double x)` | Returns the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta). |
| `static double` | `difference(BasicDataSet ds1, BasicDataSet ds2)` | Difference function which is always not-negative and reflects difference between 2 given data sets in their common arguments range |
| `static double` | `difference(BasicDataSet ds, TableFunction f)` | Difference function which is always not-negative and reflects difference between given data set and table function in their common arguments range |
| `static double` | `gammaLog(double x)` | Returns the natural logarithm of the gamma function of `x`:  `ln(Γ(x))`.  The gamma function is an extension of the factorial function that works on all positive values of `x`.  If `n` is a positive integer, then: `Γ(n) = (n - 1)!`.    The `gammaLog` function may be useful in System Dynamics models for computing combinatorial factors. |
| `static boolean` | `isFinite(double v)` | Returns `true` if the given value is finite (not +/-infinity or NaN) |
| `static double` | `limit(double min, double x, double max)` | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| `static int` | `limit(int min, int x, int max)` | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| `static double` | `limitMax(double x, double max)` | Returns x if it is less or equal to max, otherwise returns max. |
| `static int` | `limitMax(int x, int max)` | Returns x if it is less or equal to max, otherwise returns max. |
| `static double` | `limitMin(double min, double x)` | Returns x if it is greater or equal to min, otherwise returns min. |
| `static int` | `limitMin(int min, int x)` | Returns x if it is greater or equal to min, otherwise returns min. |
| `static double` | `quantum(double value, double quantizer)` | Returns the number smaller (by absolute value) than or equal to `value` that is an integer multiple of `quantizer`.  If `quantizer` is less than or equal to zero, then `value` is returned unchanged.  For example, `quantum(PI, 0.01)` will return `3.14` |
| `static double` | `roundToDecimal(double v, int nDecimalDigits)` | Rounds the value to the given precision. |
| `static int` | `roundToInt(double v)` | Returns `int` closest to the given value. |
| `static double` | `sqr(double v)` | Returns the square of the given value (`v2`) |
| `static double` | `xidz(double a, double b, double x)` | Tries to divide the first argument by the second. |
| `static double` | `zidz(double a, double b)` | Tries to divide the first argument by the second. |
