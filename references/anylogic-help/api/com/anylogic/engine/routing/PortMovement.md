*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/PortMovement.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Class PortMovement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.PortMovement

All Implemented Interfaces:
:   `IMovement`, `Serializable`

---

```
public class PortMovement
extends Object
implements IMovement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.routing.PortMovement)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PortMovement(MarkupPort source, MarkupPort target)` |  |

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
| `MarkupPort` | `getSource()` |  |
| `Position` | `getSourcePosition()` |  |
| `Agent` | `getSpace()` |  |
| `MarkupPort` | `getTarget()` |  |
| `Position` | `getTargetPosition()` |  |
| `MovementType` | `getType()` |  |
| `int` | `hashCode()` |  |
| `String` | `toString()` |  |
