*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/NetworkPathFinder.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class NetworkPathFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.routing.finders.AbstractNetworkPathFinder](AbstractNetworkPathFinder.md "class in com.anylogic.engine.routing.finders")<[Node](../../markup/Node.md "class in com.anylogic.engine.markup"),[Path](../../markup/Path.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.routing.finders.NetworkPathFinder

---

```
public class NetworkPathFinder
extends AbstractNetworkPathFinder<Node,Path>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `NetworkPathFinder()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `RouteData` | `find(IPathFinderProviderFactory factory, Node source, Node target, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Node sourceNode, Path targetPath, double targetOffset, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Node source, Point sourcePos, Node target, Point targetPos, LengthUnits units, Predicate<Node> nodeFilter, Predicate<Path> pathFilter, Path... pathsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Node sourceNode, Point sourcePos, Path targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units, Predicate<Node> nodeFilter, Predicate<Path> pathFilter, Path... pathsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Path sourcePath, double sourceOffset, Node targetNode, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Path sourcePath, double sourceOffset, Path targetPath, double targetOffset, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Path sourcePath, double sourceOffset, PathMovementDirection sourceDirection, Node targetNode, Point targetPos, LengthUnits units, Predicate<Node> nodeFilter, Predicate<Path> pathFilter, Path... pathsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, Path sourcePath, double sourceOffset, PathMovementDirection sourceDirection, Path targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units, Predicate<Node> nodeFilter, Predicate<Path> pathFilter, Path... pathsToInclude)` |  |
