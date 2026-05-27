*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractRoadPart.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractRoadPart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractRoadPart

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AbstractRoadSidePart`

---

```
@AnyLogicInternalAPI
public abstract class AbstractRoadPart
extends AbstractRoadMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractRoadPart)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractRoadPart()` |  |
| `AbstractRoadPart(Road road, ShapeDrawMode drawMode, boolean isPublic, double offset)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getOffset()` | Returns offset (measured by guideline of lane adjacent to road part) from beginning of lane guideline to beginning of road part in XY-projection, **in pixels**. |
| `double` | `getOffset(LengthUnits units)` | Returns offset (measured by guideline of lane adjacent to road part) from beginning of lane guideline to beginning of road part in XY-projection, measured in the given units. |
| `Road` | `getRoad()` | Returns road segment on which the road part is located. |
| `void` | `setOffset(double offset)` | Sets offset (measured by guideline of lane adjacent to road part) from beginning of lane guideline to beginning of road part in XY-projection, **in pixels**. |
| `void` | `setOffset(double offset, LengthUnits units)` | Sets offset (measured by guideline of lane adjacent to road part) from beginning of lane guideline to beginning of road part in XY-projection, measured in the given units. |
| `void` | `setRoad(Road road)` | Sets road segment on which the road part is located. |
