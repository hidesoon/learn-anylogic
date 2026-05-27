*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/RouteData.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class RouteData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.RouteData

All Implemented Interfaces:
:   `Serializable`, `Iterable<IMovement>`

---

```
public class RouteData
extends Object
implements Serializable, Iterable<IMovement>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.RouteData)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RouteData(IMovement... movements)` |  |
| `RouteData(RouteData routeData)` |  |
| `RouteData(Collection<? extends IMovement> movements)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(RouteData routeData)` |  |
| `void` | `addMovement(int index, IMovement movement)` |  |
| `void` | `addMovement(IMovement movement)` |  |
| `void` | `addMovements(IMovement... movements)` |  |
| `void` | `addMovements(Collection<? extends IMovement> movements)` |  |
| `void` | `addNodeTransferMovement(INode<?,?> node, IPath<?> sourcePath, IPath<?> targetPath)` |  |
| `void` | `addPathMovement(IPath<?> path, boolean forward)` |  |
| `void` | `addPathMovement(IPath<?> path, double sourceOffset, double targetOffset, LengthUnits units)` |  |
| `void` | `addPlainMovement(Agent space, Point source, Point target)` |  |
| `void` | `addPlainMovement(INetworkMarkupElement networkElement, Point source, Point target)` |  |
| `void` | `addPortMovement(MarkupPort source, MarkupPort target)` |  |
| `boolean` | `contains(INode<?,?> node)` |  |
| `boolean` | `contains(IPath<?> path)` |  |
| `static IMovement` | `createNodeTransferMovement(INode<?,?> node, IPath<?> sourcePath, IPath<?> targetPath)` |  |
| `static IMovement` | `createPathMovement(IPath<?> path, boolean forward)` |  |
| `static IMovement` | `createPathMovement(IPath<?> path, double sourceOffset, double targetOffset, LengthUnits units)` |  |
| `static IMovement` | `createPlainMovement(Agent space, Point source, Point target)` |  |
| `static IMovement` | `createPlainMovement(INetworkMarkupElement networkElement, Point source, Point target)` |  |
| `static IMovement` | `createPortMovement(MarkupPort source, MarkupPort target)` |  |
| `double` | `distance(LengthUnits units)` |  |
| `static RouteData` | `findShortestRoute(Collection<RouteData> collection, LengthUnits units)` |  |
| `IMovement` | `getFirstMovement()` |  |
| `IMovement` | `getLastMovement()` |  |
| `IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units)` |  |
| `IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units, IRouteLocation out)` |  |
| `IMovement` | `getMovement(int index)` |  |
| `List<IMovement>` | `getMovements()` |  |
| `IRouteLocation` | `getSourceLocation()` |  |
| `IRouteLocation` | `getTargetLocation()` |  |
| `boolean` | `isEmpty()` |  |
| `Iterator<IMovement>` | `iterator()` |  |
| `double` | `recalculateDistance()` |  |
| `void` | `removeFirstMovement()` |  |
| `void` | `removeLastMovement()` |  |
| `void` | `removeMovement(int index)` |  |
| `boolean` | `removeMovement(IMovement movement)` |  |
| `int` | `size()` |  |
| `String` | `toString()` |  |
