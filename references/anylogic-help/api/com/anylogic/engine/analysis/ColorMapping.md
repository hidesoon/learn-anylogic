*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/ColorMapping.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class ColorMapping

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.ColorMapping

All Implemented Interfaces:
:   `Serializable`

---

```
public class ColorMapping
extends Object
implements Serializable
```

Conditional expression which determines the color of the value in [`TimeColorChart`](TimeColorChart.md "class in com.anylogic.engine.analysis")

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.ColorMapping)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ColorMapping(String title, ColorMappingOperator comparisonOperator, double rightHandSide, Color color)` | Creates the mapping from the value to the color |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Color` | `getColor()` | Returns the resulting color of this mapping |
| `ColorMappingOperator` | `getComparisonOperator()` | Returns the operator of this mapping |
| `double` | `getRightHandSide()` | Returns the value of the rightHandSide |
| `String` | `getTitle()` |  |
