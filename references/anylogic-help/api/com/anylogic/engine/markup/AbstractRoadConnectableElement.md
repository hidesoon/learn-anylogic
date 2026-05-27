*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractRoadConnectableElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractRoadConnectableElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractRoadConnectableElement

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `Intersection`, `Road`

---

```
@AnyLogicInternalAPI
public abstract class AbstractRoadConnectableElement
extends AbstractRoadMarkup
```

Abstract class for any Transport Library space markup elements representing any part of road (road,
road juction, parking lot, etc.)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractRoadConnectableElement)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractRoadConnectableElement()` | Creates a new instance of abstract road element. |
| `AbstractRoadConnectableElement(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Creates a new instance of abstract road element. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract List<RoadConnectionPoint>` | `getConnectionPoints()` | Returns a list of connection points of the road element. |
