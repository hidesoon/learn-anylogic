*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractRoadMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractRoadMarkup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractRoadMarkup

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AbstractRoadConnectableElement`, `AbstractRoadPart`

---

```
@AnyLogicInternalAPI
public abstract class AbstractRoadMarkup
extends MarkupShape
```

Abstract class for all Transport Library space markup elements.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractRoadMarkup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractRoadMarkup()` | Creates a new instance of abstract road markup. |
| `AbstractRoadMarkup(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Creates a new instance of abstract road markup. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `RoadNetwork` | `getRoadNetwork()` | Return roadNetwork specified for this AbstractRoadMarkup |
| `void` | `setDebugInfoVisible(boolean debugInfoVisible)` | Deprecated. TODO remove in release |
| `void` | `setRoadNetwork(RoadNetwork roadNetwork)` | Sets a roadNetwork for this AbstractRoadMarkup. |
