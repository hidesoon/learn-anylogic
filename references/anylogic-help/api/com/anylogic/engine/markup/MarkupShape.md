*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/MarkupShape.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class MarkupShape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.MarkupShape

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AbstractLevelMarkup`, `AbstractRailwayMarkup`, `AbstractRoadMarkup`, `ConveyorMarkupElement`, `LiftPortImpl`, `NetworkMarkupElement`

---

```
public abstract class MarkupShape
extends AbstractMarkup
implements HasLevel
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.MarkupShape)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MarkupShape()` |  |
| `MarkupShape(Agent owner)` |  |
| `MarkupShape(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `final RuntimeException` | `error(String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `String` | `getFullName()` | Returns the name of the markup prefixed by the path from the top-level agent to this one. |
| `abstract Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `double` | `getOutsideLevelZ()` |  |
| `Agent` | `getPresentable()` |  |
| `Agent` | `getSpace()` | Returns the agent where the markup element is defined |
| `final void` | `initialize()` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |
| `boolean` | `isClickHandled()` |  |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isPublic()` | Tests if the markup is public, i.e. |
| `boolean` | `onClick(double clickx, double clicky)` | Should be overridden to define the shape reaction on mouse click. |
| `void` | `remove()` | Removes the markup element from the presentation, if it is not a part of the presentation, does nothing. |
| `void` | `setDrawMode(ShapeDrawMode drawMode)` | Sets the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  This method may be called only for shapes created using no-argument constructor (which have no limitations like 2D-only) and only once. |
| `void` | `setOwner(Agent owner)` | Sets the owner of the markup element |
