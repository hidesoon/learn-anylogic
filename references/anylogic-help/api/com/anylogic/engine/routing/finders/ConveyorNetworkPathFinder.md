*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/ConveyorNetworkPathFinder.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class ConveyorNetworkPathFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.routing.finders.AbstractNetworkPathFinder](AbstractNetworkPathFinder.md "class in com.anylogic.engine.routing.finders")<[ConveyorNode](../../markup/ConveyorNode.md "class in com.anylogic.engine.markup")<?>,[ConveyorPath](../../markup/ConveyorPath.md "class in com.anylogic.engine.markup")<?>>

com.anylogic.engine.routing.finders.ConveyorNetworkPathFinder

---

```
public class ConveyorNetworkPathFinder
extends AbstractNetworkPathFinder<ConveyorNode<?>,ConveyorPath<?>>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorNetworkPathFinder()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorNode<?> source, ConveyorNode<?> target, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorNode<?> source, ConveyorNode<?> target, LengthUnits units, Predicate<ConveyorNode<?>> nodeFilter, Predicate<ConveyorPath<?>> pathFilter, ConveyorPath<?>... conveyorsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorNode<?> sourceNode, ConveyorPath<?> targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorNode<?> sourceNode, ConveyorPath<?> targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units, Predicate<ConveyorNode<?>> nodeFilter, Predicate<ConveyorPath<?>> pathFilter, ConveyorPath<?>... conveyorsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorPath<?> sourcePath, double sourceOffset, PathMovementDirection sourceDirection, ConveyorNode<?> targetNode, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorPath<?> sourcePath, double sourceOffset, PathMovementDirection sourceDirection, ConveyorNode<?> targetNode, LengthUnits units, Predicate<ConveyorNode<?>> nodeFilter, Predicate<ConveyorPath<?>> pathFilter, ConveyorPath<?>... conveyorsToInclude)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorPath<?> sourcePath, double sourceOffset, PathMovementDirection sourceDirection, ConveyorPath<?> targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units)` |  |
| `RouteData` | `find(IPathFinderProviderFactory factory, ConveyorPath<?> sourcePath, double sourceOffset, PathMovementDirection sourceDirection, ConveyorPath<?> targetPath, double targetOffset, PathMovementDirection targetDirection, LengthUnits units, Predicate<ConveyorNode<?>> nodeFilter, Predicate<ConveyorPath<?>> pathFilter, ConveyorPath<?>... conveyorsToInclude)` |  |
