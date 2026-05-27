*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/LegacyShapeGISMapProjection.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class LegacyShapeGISMapProjection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.LegacyShapeGISMapProjection

---

```
@Deprecated
@AnyLogicInternalAPI
public class LegacyShapeGISMapProjection
extends Object
```

Deprecated.

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LegacyShapeGISMapProjection(ShapeGISMap owner)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Point` | `convertForward(double latitude, double longitude)` | Deprecated. this function is deprecated and will be removed in the next release |
| `Point` | `convertForward(double latitude, double longitude, Point out)` | Deprecated. this function is deprecated and will be removed in the next release |
| `Point` | `convertInverse(double x, double y)` | Deprecated. this function is deprecated and will be removed in the next release |
| `Point` | `convertInverse(double x, double y, Point out)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertRotationAngleForward(double latitude, double longitude, double angle)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertRotationAngleInverse(double x, double y, double angle)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertXForward(double latitude, double longitude)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertXInverse(double x, double y)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertYForward(double latitude, double longitude)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `convertYInverse(double x, double y)` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `getAdditionalScale()` | Deprecated. |
| `double` | `getPresentationScaleOnOwnerSpace(Agent agent)` | Deprecated. |
| `com.bbn.openmap.proj.Projection` | `getProjection()` | Deprecated.  Creates projection if it hasn't been created yet |
| `boolean` | `projectionContains(double latitude, double longitude)` | Deprecated. this function is deprecated and will be removed in the next release |
| `void` | `setAdditionalScale(double additionalScale)` | Deprecated. |
