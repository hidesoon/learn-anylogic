*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/BusStop.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class BusStop

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadPart](AbstractRoadPart.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadSidePart](AbstractRoadSidePart.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.BusStop

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasCenterPoint`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class BusStop
extends AbstractRoadSidePart
implements HasCenterPoint
```

Class representing a bus stop located along border of a road segment.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.BusStop)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BusStop()` |  |
| `BusStop(Road road, ShapeDrawMode drawMode, boolean isPublic, boolean isOnForwardSide, double offset, double lengthInMeters)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<Agent>` | `getCars()` | Returns ordered list of cars located on this bus stop. |
| `final Position` | `getCenter(Position out)` |  |
| `double` | `getLength()` | Returns length of bus stop along border with lane adjacent to bus stop, measured in pixels. |
| `double` | `getLength(LengthUnits units)` | Returns length of bus stop measured in the given units along border with lane adjacent to bus stop. |
| `int` | `nCars()` | Returns number of cars located on this bus stop |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setDataSource(RoadBasicDataSource dataSource)` |  |
| `void` | `setLength(double lengthInPixels)` | Deprecated. this method is deprecated and may be removed in the next release. |
| `void` | `setLength(double length, LengthUnits units)` | Sets length of bus stop measured in the given units along border with lane adjacent to bus stop |
