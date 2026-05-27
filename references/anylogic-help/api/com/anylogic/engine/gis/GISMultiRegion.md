*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISMultiRegion.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISMultiRegion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.GISMultiRegion

All Implemented Interfaces:
:   `IGeographicSearchEntry`, `Serializable`, `Iterable<GISRegion>`

---

```
public class GISMultiRegion
extends Object
implements IGeographicSearchEntry, Iterable<GISRegion>, Serializable
```

This markup element contains set of GIS regions.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.GISMultiRegion)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISMultiRegion()` |  |
| `GISMultiRegion(String title, GISRegion... regions)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `add(GISRegion region)` |  |
| `boolean` | `addAll(Collection<GISRegion> regions)` |  |
| `double` | `area()` | Returns the total area (measured in m2) |
| `double` | `area(AreaUnits units)` | Returns the area of this multiregion (measured in @units) |
| `List<GISRegion>` | `getRegions()` |  |
| `String` | `getTitle()` | Returns full geographic name. |
| `Iterator<GISRegion>` | `iterator()` |  |
| `GISRegion` | `randomRegionInside()` |  |
| `GISRegion` | `randomRegionInside(Random rng)` |  |
| `boolean` | `remove(GISRegion region)` |  |
| `boolean` | `removeAll(Collection<GISRegion> regions)` |  |
| `void` | `setFillColor(Paint color)` |  |
| `void` | `setLineColor(Paint color)` |  |
| `void` | `setLineStyle(LineStyle lineStyle)` |  |
| `void` | `setLineWidth(double width)` |  |
| `void` | `setTitle(String title)` |  |
| `void` | `setVisible(boolean visible)` |  |
