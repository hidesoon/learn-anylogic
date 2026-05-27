*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/SVGUtils.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class SVGUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.SVGUtils

---

```
@AnyLogicInternalAPI
public class SVGUtils
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `SVGUtils.SVGCadDescriptor` |  |
| `static class` | `SVGUtils.SVGCadLayerDescriptor` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static final double` | `adjustArcAngle(double x, double y, double offx, double offy, boolean cw, double alimit, double cx, double cy)` | Moves an end point of the arc (namely, its angle) to get a certain offset from the initial point |
| `static final double` | `angleBetween(double astart, double aend, boolean clockwise)` | returns a positive angle between the start and end angles |
| `static String` | `dxfLayerNameToFileName(String layername)` |  |
| `static String` | `dxfLayerNameToSVGId(String layername)` |  |
| `static final String` | `svgColor(Color c)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static final String` | `svgNumberFormat(double value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static final String` | `svgNumberFormatPrecise(double value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static final String` | `svgNumberFormatWithOptions(double value, boolean precise)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
