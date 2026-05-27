*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/NetworkAStarProvider.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class NetworkAStarProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.routing.finders.BaseNetworkAStarProvider](BaseNetworkAStarProvider.md "class in com.anylogic.engine.routing.finders")

com.anylogic.engine.routing.finders.NetworkAStarProvider

All Implemented Interfaces:
:   `IAStarProvider`

---

```
public class NetworkAStarProvider
extends BaseNetworkAStarProvider
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `NetworkAStarProvider(Object sourceVertex, Point sourcePos, Object targetVertex, Point targetPos)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<Object>` | `getIngoingEdges(Object vertex, Object fromEdge)` |  |
| `List<Object>` | `getIngoingVertices(Object vertex, Object edge)` |  |
| `List<Object>` | `getOutgoingVertices(Object vertex, Object edge)` |  |
| `boolean` | `isCompatibleEdge(Object element)` |  |
| `boolean` | `isCompatibleVertex(Object element)` |  |
| `boolean` | `skipEdge(Object edge, Predicate<Object> filter)` |  |
| `boolean` | `skipVertex(Object vertex, Predicate<Object> filter)` |  |
