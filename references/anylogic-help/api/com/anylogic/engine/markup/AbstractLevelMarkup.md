*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractLevelMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractLevelMarkup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractLevelMarkup

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AbstractFluidMarkup`, `AbstractWall`, `Crane`, `DensityMap`, `Elevator`, `EscalatorGroup`, `LevelGate`, `Lift`, `Pathway`, `PedFlowStatistics`, `Robot`, `ServiceBase`, `Storage`, `TargetLine`

---

```
public abstract class AbstractLevelMarkup
extends MarkupShape
implements LevelMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractLevelMarkup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractLevelMarkup()` |  |
| `AbstractLevelMarkup(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `void` | `setLevel(Level level)` |  |
