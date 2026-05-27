*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/PathRouteLocation.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class PathRouteLocation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.PathRouteLocation

All Implemented Interfaces:
:   `IRouteLocation`, `Serializable`

---

```
@AnyLogicInternalAPI
public class PathRouteLocation
extends Object
implements IRouteLocation
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.PathRouteLocation)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PathRouteLocation(INetworkMarkupElement element, IPath<?> path, double offset, LengthUnits units)` |  |
| `PathRouteLocation(INetworkMarkupElement element, IPath<?> path, double offset, LengthUnits units, PathMovementDirection direction)` |  |
| `PathRouteLocation(IPath<?> path, double offset, LengthUnits units)` |  |
| `PathRouteLocation(IPath<?> path, double offset, LengthUnits units, PathMovementDirection direction)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `equals(Object obj)` |  |
| `PathMovementDirection` | `getDirection()` |  |
| `Level` | `getLevel()` |  |
| `INetwork<?,?>` | `getNetwork()` |  |
| `INetworkMarkupElement` | `getNetworkElement()` |  |
| `double` | `getOffset(LengthUnits units)` |  |
| `IPath<?>` | `getPath()` |  |
| `Position` | `getPosition()` |  |
| `Agent` | `getSpace()` |  |
| `int` | `hashCode()` |  |
| `String` | `toString()` |  |
