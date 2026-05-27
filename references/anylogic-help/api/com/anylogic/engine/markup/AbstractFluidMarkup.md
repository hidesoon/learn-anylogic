*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractFluidMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractFluidMarkup<DS>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractFluidMarkup<DS>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `BulkConveyorBelt`, `Pipe`, `StorageTank`

---

```
public abstract class AbstractFluidMarkup<DS>
extends AbstractLevelMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractFluidMarkup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractFluidMarkup()` |  |
| `AbstractFluidMarkup(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Paint color)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Color` | `getColor()` | Returns the color of the markup element, or `null` if markup element has no color or has textured (in this case [`getTexture()`](#getTexture()) should be used instead) |
| `DS` | `getDataSource()` |  |
| `Texture` | `getTexture()` | Returns the texture of the markup element, if it has texture |
| `void` | `setColor(Color color)` | Sets the color of the markup element. |
| `void` | `setColor(Paint color)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setDataSource(DS dataSource)` |  |
