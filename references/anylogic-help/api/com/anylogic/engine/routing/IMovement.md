*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/IMovement.html>*

---

Package [com.anylogic.engine.routing](package-summary.md)

# Interface IMovement

All Superinterfaces:
:   `Serializable`

All Known Implementing Classes:
:   `PathMovement`, `PlainMovement`, `PortMovement`

---

```
public interface IMovement
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(IRouteLocation location)` |  |
| `double` | `distance(LengthUnits units)` |  |
| `Level` | `getLevel()` |  |
| `default IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units)` |  |
| `IRouteLocation` | `getLocationAtOffset(double offset, LengthUnits units, IRouteLocation out)` |  |
| `INetwork<?,?>` | `getNetwork()` |  |
| `INetworkMarkupElement` | `getNetworkElement()` |  |
| `Agent` | `getSpace()` |  |
| `MovementType` | `getType()` |  |
| `default boolean` | `isMovingForward()` |  |
