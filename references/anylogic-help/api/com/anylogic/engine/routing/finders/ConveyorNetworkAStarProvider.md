*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/ConveyorNetworkAStarProvider.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class ConveyorNetworkAStarProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.routing.finders.BaseNetworkAStarProvider](BaseNetworkAStarProvider.md "class in com.anylogic.engine.routing.finders")

com.anylogic.engine.routing.finders.ConveyorNetworkAStarProvider

All Implemented Interfaces:
:   `IAStarProvider`

---

```
public class ConveyorNetworkAStarProvider
extends BaseNetworkAStarProvider
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorNetworkAStarProvider(Object sourceVertex, Point sourcePos, Object targetVertex, Point targetPos)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getEdgeScore(Object edge, Object fromVertex, Object toVertex)` |  |
| `List<Object>` | `getOppositeVertices(Object vertex, Object edge)` |  |
| `List<Object>` | `getOutgoingEdges(Object vertex, Object fromEdge)` |  |
| `List<Object>` | `getSplitMergeOutgoingEdges(ConveyorSpur<?> csm, Object fromEdge)` |  |
| `double` | `getVertexScore(Object vertex, Object fromEdge, Object toEdge)` |  |
| `boolean` | `isCompatibleEdge(Object element)` |  |
| `boolean` | `isCompatibleVertex(Object element)` |  |
| `boolean` | `skipEdge(Object edge, Predicate<Object> filter)` |  |
| `boolean` | `skipVertex(Object vertex, Predicate<Object> filter)` |  |
