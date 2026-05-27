*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/BaseNetworkAStarProvider.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class BaseNetworkAStarProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.finders.BaseNetworkAStarProvider

All Implemented Interfaces:
:   `IAStarProvider`

Direct Known Subclasses:
:   `ConveyorNetworkAStarProvider`, `NetworkAStarProvider`

---

```
public abstract class BaseNetworkAStarProvider
extends Object
implements IAStarProvider
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getEdgeScore(Object edge, Object fromVertex, Object toVertex)` |  |
| `double` | `getHeuristicScore(Object sourceVertex, Object targetVertex)` |  |
| `List<Object>` | `getOppositeVertices(Object vertex, Object edge)` |  |
| `List<Object>` | `getOutgoingEdges(Object vertex, Object fromEdge)` |  |
| `double` | `getVertexScore(Object vertex, Object fromEdge, Object toEdge)` |  |
| `boolean` | `skipEdge(Object edge, Predicate<Object> filter)` |  |
| `boolean` | `skipVertex(Object vertex, Predicate<Object> filter)` |  |
