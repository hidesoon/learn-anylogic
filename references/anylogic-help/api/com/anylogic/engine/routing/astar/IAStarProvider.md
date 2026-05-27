*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/astar/IAStarProvider.html>*

---

Package [com.anylogic.engine.routing.astar](package-summary.md)

# Interface IAStarProvider

All Known Implementing Classes:
:   `BaseNetworkAStarProvider`, `ConveyorNetworkAStarProvider`, `NetworkAStarProvider`

---

```
public interface IAStarProvider
```

Graph provider for AStar algorithm

**Example:**

```
 public class SimpleNetworkProvider implements IAStarProvider {
     public List getOutgoingEdges(Object vertex, Object fromEdge) {
         Node node = (Node)vertex;
         List result = new ArrayList<>(node.getConnectionsCount());
         for (int i = 0; i < node.getConnectionsCount(); i++) {
         Path path = node.getConnection(i);
             if (path.isBidirectional() || path.getSource() == vertex) {
                 result.add(path);
             }
         }
         return result;
     }

     public List getOppositeVertices(Object vertex, Object edge) {
         return Collections.singletonList(((Path)edge).getOtherNode((Node)vertex));
     }

     public double getEdgeScore(Object edge, Object fromVertex, Object toVertex) {
         return ((Path)edge).length();
     }

     public double getVertexScore(Object vertex, Object fromEdge, Object toEdge) {
         return ((Node)vertex).getTransferDistance((Path)fromEdge, (Path)toEdge);
     }

     public double getHeuristicScore(Object sourceVertex, Object targetVertex) {
         Position sourcePos = ((Node)sourceVertex).getPosition(0, 1, null);
         Position targetPos = ((Node)sourceVertex).getPosition(0, 1, null);
         return sourcePos.distance(targetPos);
     }
 }

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| double | getEdgeScore(Object edge,  Object fromVertex,  Object toVertex) |  |
| double | getHeuristicScore(Object sourceVertex,  Object targetVertex) |  |
| List<Object> | getOppositeVertices(Object vertex,  Object edge) |  |
| List<Object> | getOutgoingEdges(Object vertex,  Object fromEdge) |  |
| double | getVertexScore(Object vertex,  Object fromEdge,  Object toEdge) |  |
| default boolean | skipEdge(Object edge,  Predicate<Object> filter) |  |
| default boolean | skipVertex(Object vertex,  Predicate<Object> filter) |  |
```
