*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/ElevatorUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class ElevatorUsdRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<[Elevator](../markup/Elevator.md "class in com.anylogic.engine.markup")<?>>

com.anylogic.engine.omniverse\_connector.ElevatorUsdRepresentation

All Implemented Interfaces:
:   `UsdRepresentation<Elevator<?>>`

---

```
public class ElevatorUsdRepresentation
extends AbstractUsdRepresentation<Elevator<?>>
```

Associates a pedestrian elevator with a prim

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ElevatorUsdRepresentation(UsdContext context, Elevator<?> elevator, String cabinPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `void` | `setCabinFrontDoorVariantProvider(Function<Elevator<?>,Object> cabinFrontDoorVariantProvider)` |  |
| `void` | `setCabinFrontDoorVarset(String cabinFrontDoorVarset)` |  |
| `void` | `setCabinRearDoorVariantProvider(Function<Elevator<?>,Object> cabinRearDoorVariantProvider)` |  |
| `void` | `setCabinRearDoorVarset(String cabinRearDoorVarset)` |  |
| `void` | `setGateFrontVariantProvider(Function<ElevatorShaft,String> gateFrontVariantProvider)` |  |
| `void` | `setGateFrontVarsetProvider(Function<ElevatorShaft,String> gateFrontVarsetProvider)` |  |
| `void` | `setGatePathProvider(Function<Integer,String> gatePathProvider)` |  |
| `void` | `setGateRearVariantProvider(Function<ElevatorShaft,String> gateRearVariantProvider)` |  |
| `void` | `setGateRearVarsetProvider(Function<ElevatorShaft,String> gateRearVarsetProvider)` |  |
