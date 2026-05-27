*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/PathMovement.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class PathMovement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.PathMovement

All Implemented Interfaces:
:   `IMovement`, `Serializable`

---

```
public class PathMovement
extends Object
implements IMovement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.PathMovement)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PathMovement(INetworkMarkupElement networkElement, IPath<?> path, double sourceOffset, double targetOffset, LengthUnits units)` |  |
| `PathMovement(INetworkMarkupElement networkElement, IPath<?> path, double sourceOffset, double targetOffset, PathMovementDirection direction, LengthUnits units)` |  |
| `PathMovement(IPath<?> path, double sourceOffset, double targetOffset, LengthUnits units)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(IRouteLocation location)` |  |
| `double` | `distance(LengthUnits units)` |  |
| `boolean` | `equals(Object obj)` |  |
| `PathMovementDirection` | `getDirection()` |  |
| `Level` | `getLevel()` |  |
| `IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units, IRouteLocation out)` |  |
| `INetwork<?,?>` | `getNetwork()` |  |
| `INetworkMarkupElement` | `getNetworkElement()` |  |
| `IPath<?>` | `getPath()` |  |
| `double` | `getSourceOffset(LengthUnits units)` |  |
| `Agent` | `getSpace()` |  |
| `double` | `getTargetOffset(LengthUnits units)` |  |
| `MovementType` | `getType()` |  |
| `int` | `hashCode()` |  |
| `boolean` | `isMovingForward()` |  |
| `String` | `toString()` |  |
