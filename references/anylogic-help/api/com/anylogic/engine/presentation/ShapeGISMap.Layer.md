*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGISMap.Layer.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeGISMap.Layer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.ShapeGISMap.Layer

All Implemented Interfaces:
:   `Serializable`

Enclosing class:
:   [ShapeGISMap](ShapeGISMap.md "class in com.anylogic.engine.presentation")

---

```
public static class ShapeGISMap.Layer
extends Object
implements Serializable
```

Class which stores GIS map layer information

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeGISMap.Layer)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Layer(String shapeFileName, Color lineColor, Color fillColor, boolean visible)` | Creates new Layer descriptor |
| `Layer(String shapeFileName, String dbfFileName, Color lineColor, Color fillColor, int objectNameColumnIndex, boolean visible)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `forAllObjects(BiConsumer<org.locationtech.jts.geom.Geometry,org.geotools.api.feature.simple.SimpleFeature> action)` | Reads the shapefile (with optional filtering, e.g. |
| `void` | `forAllObjects(BiFunction<org.geotools.api.filter.FilterFactory,org.geotools.api.feature.type.FeatureType,org.geotools.api.filter.Filter> filterProvider, BiConsumer<org.locationtech.jts.geom.Geometry,org.geotools.api.feature.simple.SimpleFeature> action)` | Same as `#forAllObjects(Consumer)` but applies the given filtering when reading shapefile. |
| `boolean` | `isVisible()` |  |
| `void` | `setFillColor(List<Integer> shapes, Color color)` | Sets the new fill color for the given shapes in the shape file. |
| `void` | `setLineColor(List<Integer> shapes, Color color)` | Sets the new line color for the given shapes in the shape file. |
| `void` | `setVisible(boolean visible)` |  |
