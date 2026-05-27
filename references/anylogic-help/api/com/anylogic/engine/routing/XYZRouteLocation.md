*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/XYZRouteLocation.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class XYZRouteLocation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.XYZRouteLocation

All Implemented Interfaces:
:   `IRouteLocation`, `Serializable`

---

```
@AnyLogicInternalAPI
public class XYZRouteLocation
extends Object
implements IRouteLocation
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.XYZRouteLocation)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `XYZRouteLocation(Agent space, Level level, INetwork<?,?> network, INetworkMarkupElement networkElement, Position position)` |  |
| `XYZRouteLocation(Agent space, Position position)` |  |
| `XYZRouteLocation(INetwork<?,?> network, Position position)` |  |
| `XYZRouteLocation(INetworkMarkupElement networkElement, Position position)` |  |
| `XYZRouteLocation(Level level, Position position)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `equals(Object obj)` |  |
| `Level` | `getLevel()` |  |
| `INetwork<?,?>` | `getNetwork()` |  |
| `INetworkMarkupElement` | `getNetworkElement()` |  |
| `Position` | `getPosition()` |  |
| `Agent` | `getSpace()` |  |
| `int` | `hashCode()` |  |
| `String` | `toString()` |  |
