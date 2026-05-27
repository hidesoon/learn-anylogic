*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ParkingLotDataSource.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface ParkingLotDataSource

All Superinterfaces:
:   `RoadBasicDataSource`, `Serializable`

---

```
public interface ParkingLotDataSource
extends RoadBasicDataSource
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Agent` | `getCarOnSpace(int spaceIndex)` | Returns car located in the parking space with the given index, or `null` if this space is free |
| `int[]` | `getFreeSpaceIndexes()` | Returns array of indexes of free spaces |
| `int` | `getParkingSpaceIndex(Agent car)` | Returns the index of specified car in the parking lot. |
| `int` | `nFree()` | Returns the number of free spaces in this parking lot |
| `int` | `randomFreeSpaceIndex()` | Returns the index of randomly chosen free parking space |
