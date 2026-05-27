*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Pathway.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Pathway

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Pathway

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Pathway
extends AbstractLevelMarkup
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Pathway)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Pathway()` |  |
| `Pathway(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Color lineColor, MarkupSegmentLine... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegmentLine segment)` | Adds segment to this markup element |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Color` | `getLineColor()` | Returns the color of the markup shape |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index in the path |
| `int` | `getSegmentCount()` | Returns the number of segments in the path |
| `List<MarkupSegmentLine>` | `getSegments()` | Returns the list of segments in this element. |
| `void` | `setLineColor(Color color)` | Sets the color of the markup shape. |
