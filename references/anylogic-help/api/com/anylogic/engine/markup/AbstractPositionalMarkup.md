*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractPositionalMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface AbstractPositionalMarkup

All Superinterfaces:
:   `SVGElement`, `UsdElement`

All Known Implementing Classes:
:   `AbstractShapedWall`, `AreaNode`, `CircularWall`, `ConveyorCustomStation`, `ConveyorNode`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSpur`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `Crane`, `Elevator`, `EscalatorGroup`, `JibCrane`, `LevelGate`, `Lift`, `LiftPortImpl`, `NetworkPortImpl`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `PositionOnTrack`, `QueueArea`, `RailwaySwitch`, `RectangularNode`, `RectangularWall`, `Robot`, `Storage`, `StorageTank`

---

```
@AnyLogicInternalAPI
public interface AbstractPositionalMarkup
extends UsdElement, SVGElement
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default double` | `getRotation()` |  |
| `Agent` | `getSpace()` |  |
| `double` | `getX()` |  |
| `double` | `getY()` |  |
| `double` | `getZ()` |  |
| `boolean` | `isVisible()` |  |
