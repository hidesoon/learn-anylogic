*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/BasicGISUtils.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class BasicGISUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.BasicGISUtils

---

```
public class BasicGISUtils
extends Object
```

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static interface` | `BasicGISUtils.DistanceFunction` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static double` | `getDistanceGIS(double latitude1, double longitude1, double latitude2, double longitude2)` | Returns the distance measured in meters between two given points |
| `static double` | `getGISRegionArea(double[] latlondeg)` |  |
| `static double[]` | `getSimplifiedRoute(double[] latLonPoints, double generalizationPrecision, BasicGISUtils.DistanceFunction distanceFunction)` | *Generalizes* the given curve. |
| `static double` | `getSphericalAzimuth(double latitude1, double longitude1, double latitude2, double longitude2)` |  |
| `static double` | `getSphericalDistance(double latitude1, double longitude1, double latitude2, double longitude2)` | Distance from one geographic point to another in radians |
| `static com.bbn.openmap.proj.Projection` | `makeProjection(double centerLatitude, double centerLongitude, double projectionScale, int width, int height)` | Create a Mercator projection. |
| `static void` | `readShapeFile(String shapefilePath, BiFunction<org.geotools.api.filter.FilterFactory,org.geotools.api.feature.type.FeatureType,org.geotools.api.filter.Filter> filterProvider, BiConsumer<org.locationtech.jts.geom.Geometry,org.geotools.api.feature.simple.SimpleFeature> action)` | Reads the given shapefile (with optional filtering, e.g. |
| `static String` | `shapeFileNameToSVGFileName(String shapefilename)` |  |
