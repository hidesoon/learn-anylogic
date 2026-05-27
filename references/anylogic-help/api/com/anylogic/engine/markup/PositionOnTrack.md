*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PositionOnTrack.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PositionOnTrack<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRailwayMarkup](AbstractRailwayMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.PositionOnTrack<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `IDescriptor`, `HasLevel`, `IMarkupLibraryDescriptor`, `IRailStopLineDescriptor<T>`, `RailMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class PositionOnTrack<T extends Agent>
extends AbstractRailwayMarkup
implements IRailStopLineDescriptor<T>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PositionOnTrack)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PositionOnTrack()` |  |
| `PositionOnTrack(Agent owner, IRailStopLineDescriptor<T> d, ShapeDrawMode drawMode, boolean isPublic, Paint color, RailwayTrack track, double offset)` |  |
| `PositionOnTrack(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Paint color, RailwayTrack track, double offset)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Paint` | `getColor()` | Returns the color of this element |
| `double` | `getOffset()` | Returns offset (measured in pixels) |
| `double` | `getOffset(LengthUnits units)` | Returns offset (measured in the given units) |
| `RailwayTrack` | `getTrack()` | Returns the track that this position is located on. |
| `double` | `getX()` | Returns the absolute x coordinate of this element |
| `double` | `getY()` | Returns the absolute y coordinate of this element |
| `double` | `getZ()` |  |
| `void` | `onTrainEnter(T train)` |  |
| `void` | `onTrainExit(T train)` |  |
| `void` | `setColor(Paint color)` | Sets the color of this element |
| `void` | `setPointOnTrack(RailwayTrack track, double offset)` | Sets the PositionOnTrack on the specified track at the specified offset. |
