*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorPointNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorPointNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.ConveyorPointNode

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorPointNode
extends ConveyorNode<Agent>
implements AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorPointNode)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorPointNode()` |  |
| `ConveyorPointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorPointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, PathEnd<ConveyorPath<?>>... pathEnds)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(ConveyorPath<?> path, PathEndType type)` |  |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `double` | `getTransferDistance(ConveyorPath<?> path1, ConveyorPath<?> path2)` |  |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
