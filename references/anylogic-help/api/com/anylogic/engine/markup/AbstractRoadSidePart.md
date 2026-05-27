*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractRoadSidePart.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractRoadSidePart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadPart](AbstractRoadPart.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractRoadSidePart

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `BusStop`, `ParkingLot`, `StopLine`

---

```
@AnyLogicInternalAPI
public abstract class AbstractRoadSidePart
extends AbstractRoadPart
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractRoadSidePart)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractRoadSidePart()` |  |
| `AbstractRoadSidePart(Road road, ShapeDrawMode drawMode, boolean isPublic, boolean isOnForwardSide, double offset)` | Creates abstract road part. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract double` | `getLength()` |  |
| `boolean` | `isOnForwardSide()` | Returns true if the road part is located on forward side of road segment, false otherwise. |
| `void` | `setOnForwardSide(boolean isOnForwardSide)` |  |
