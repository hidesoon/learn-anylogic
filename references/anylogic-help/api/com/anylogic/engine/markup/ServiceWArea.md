*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceWArea.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServiceWArea

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ServiceBase](ServiceBase.md "class in com.anylogic.engine.markup")<[ServicePoint](ServicePoint.md "class in com.anylogic.engine.markup")<[QueueArea](QueueArea.md "class in com.anylogic.engine.markup")>,[QueueArea](QueueArea.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.ServiceWArea

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ServiceWArea
extends ServiceBase<ServicePoint<QueueArea>,QueueArea>
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServiceWArea)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServiceWArea()` |  |
| `ServiceWArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, QueueArea queueArea, ServicePoint<QueueArea>[] services, Color serviceColor)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `QueueArea` | `getQueueArea()` | Returns the area belonging to the current service with area. |
| `List<QueueArea>` | `getQueues()` | Returns the list containing one element corresponding to the queue area of this service with area |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setQueueArea(QueueArea area)` | Sets the queue area of this service element. |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
