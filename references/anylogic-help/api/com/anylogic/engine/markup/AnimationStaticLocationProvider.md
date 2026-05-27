*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AnimationStaticLocationProvider.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface AnimationStaticLocationProvider

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `AnimationMovingLocationProvider`, `INode<N,P>`, `IPath<N>`

All Known Implementing Classes:
:   `AreaNode`, `ConveyorCustomStation`, `ConveyorNode`, `ConveyorPath`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `GISNode`, `GISPoint`, `GISRegion`, `GISRoute`, `NetworkPortImpl`, `Node`, `Path`, `PointNode`, `PolygonalNode`, `QueueArea`, `RectangularNode`

---

```
public interface AnimationStaticLocationProvider
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Agent` | `getSpace()` | Returns the space where the animation location is defined |
