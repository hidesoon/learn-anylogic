*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/QueueArea.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class QueueArea<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AreaNode](AreaNode.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.PolygonalNode](PolygonalNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.QueueArea<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `IAreaNodeDescriptor<T>`, `IDescriptor`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `QueueUnit`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<T>`

---

```
public class QueueArea<T extends Agent>
extends PolygonalNode<T>
implements QueueUnit
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.QueueArea)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `QueueArea()` |  |
| `QueueArea(Agent owner)` |  |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |
| `QueueArea(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `capacity()` | Returns the capacity of the queue |
| `List<Agent>` | `getPeds()` | Returns the list of agents (pedestrians) staying in this queue area |
| `boolean` | `isCapacityLimited()` | Returns `true` if this queue has limited capacity |
| `int` | `size()` | Returns the number of agents (pedestrians) staying in this queue area |
