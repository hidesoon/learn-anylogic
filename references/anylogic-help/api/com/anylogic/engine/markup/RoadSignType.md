*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RoadSignType.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface RoadSignType

All Superinterfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public interface RoadSignType
extends Serializable
```

Interface and a factory class for various road signs used in [`StopLine`](StopLine.md "class in com.anylogic.engine.markup")

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   * `StopLine.addRoadSign(RoadSignType)`

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static RoadSignType` | `newEndOfSpeedLimit()` | Creates "end of speed limit" road sign |
| `static RoadSignType` | `newSpeedLimit(double speedLimit, SpeedUnits units)` | Creates "speed limit" road sign |
| `static RoadSignType` | `newYield()` | Creates "yield" road sign |
