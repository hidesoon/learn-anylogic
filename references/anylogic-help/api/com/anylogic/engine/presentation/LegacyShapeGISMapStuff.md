*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/LegacyShapeGISMapStuff.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class LegacyShapeGISMapStuff

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.LegacyShapeGISMapStuff

---

```
@Deprecated
@AnyLogicInternalAPI
public class LegacyShapeGISMapStuff
extends Object
```

Deprecated.

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `LegacyShapeGISMapStuff.ALListenerList<T>` | Deprecated. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LegacyShapeGISMapStuff(ShapeGISMap owner, ILegacyTileFactory tileFactory)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addImageChangedListener(ImageChangedListener listener)` | Deprecated. |
| `static BufferedImage` | `createBufferedImage(int width, int height, boolean transparent)` | Deprecated. |
| `void` | `dispose()` | Deprecated. |
| `void` | `draw(Graphics2D g, AffineTransform xform, boolean publicOnly)` | Deprecated. this function is deprecated and will be removed in the next release |
| `static void` | `drawGISRuler(Graphics2D g, com.bbn.openmap.proj.Projection projection, int width, int height)` | Deprecated.  *This method is not designed to be called by user*  Draws ruler for given GIS projection |
| `void` | `removeImageChangedListener(ImageChangedListener listener)` | Deprecated. |
| `void` | `setHeight(double height)` | Deprecated. |
| `void` | `setMapScale(double mapScale)` | Deprecated. |
| `void` | `setProjectionCenter(double centerLatitude, double centerLongitude)` | Deprecated. |
| `void` | `setWidth(double width)` | Deprecated. |
| `void` | `setX(double x)` | Deprecated. |
| `void` | `setY(double y)` | Deprecated. |
