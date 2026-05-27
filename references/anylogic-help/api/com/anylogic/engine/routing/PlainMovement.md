*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/PlainMovement.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class PlainMovement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.PlainMovement

All Implemented Interfaces:
:   `IMovement`, `Serializable`

---

```
public class PlainMovement
extends Object
implements IMovement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.PlainMovement)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PlainMovement(Agent space, Point source, Point target)` |  |
| `PlainMovement(INetwork<?,?> network, Point source, Point target)` |  |
| `PlainMovement(INetworkMarkupElement networkElement, Point source, Point target)` |  |
| `PlainMovement(Level level, Point source, Point target)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(IRouteLocation location)` |  |
| `double` | `distance(LengthUnits units)` |  |
| `boolean` | `equals(Object obj)` |  |
| `Level` | `getLevel()` |  |
| `IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units, IRouteLocation out)` |  |
| `INetwork<?,?>` | `getNetwork()` |  |
| `INetworkMarkupElement` | `getNetworkElement()` |  |
| `Position` | `getNormal()` |  |
| `Position` | `getSource()` |  |
| `Agent` | `getSpace()` |  |
| `Position` | `getTarget()` |  |
| `MovementType` | `getType()` |  |
| `int` | `hashCode()` |  |
| `String` | `toString()` |  |
