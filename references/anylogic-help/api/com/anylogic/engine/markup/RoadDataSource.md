*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RoadDataSource.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface RoadDataSource

All Superinterfaces:
:   `Serializable`

---

```
public interface RoadDataSource
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `averageSpeed(boolean isOnForwardSide, double offset, SpeedUnits units)` | Returns the average speed on the given road direction near the specified offset |
| `List<Agent>` | `getCars(boolean isOnForwardSide)` | Returns ordered list of cars located on the given direction. |
| `int` | `nCars(boolean isOnForwardSide)` | Returns number of cars located on the given direction. |
| `int` | `nCars(boolean isOnForwardSide, int laneIndex)` | Returns number of cars located on the given direction. |
| `default int` | `queueSize(boolean isForwardSide, int laneIndexFrom, int laneIndexTo, double offset)` |  |
