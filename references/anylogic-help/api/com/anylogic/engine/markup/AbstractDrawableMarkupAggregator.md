*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractDrawableMarkupAggregator.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractDrawableMarkupAggregator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.AbstractDrawableMarkupAggregator

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `Level`, `RailwayNetwork`, `RoadNetwork`

---

```
@AnyLogicInternalAPI
public abstract class AbstractDrawableMarkupAggregator
extends AbstractMarkupAggregator<Agent>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractDrawableMarkupAggregator)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `void` | `setDrawMode(ShapeDrawMode drawMode)` | Sets the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  This method may be called only for shapes created using no-argument constructor (which have no limitations like 2D-only) and only once. |
