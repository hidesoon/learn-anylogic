*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/IMaintenanceableMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface IMaintenanceableMarkup

All Superinterfaces:
:   `IMaintenanceable`

All Known Implementing Classes:
:   `ConveyorPath`, `ConveyorSimpleStation`, `JibCrane`, `OverheadCraneBridge`

---

```
public interface IMaintenanceableMarkup
extends IMaintenanceable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `RuntimeException` | `error(String message)` |  |
| `void` | `fail()` |  |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `String` | `getName()` |  |
| `Object` | `getPMLProxy()` |  |
| `double` | `getUtilization()` |  |
| `boolean` | `isFailed()` |  |
| `boolean` | `isMaintenanceActive(IDowntime<?> block)` |  |
| `double` | `mtbf()` | Returns mean time before failure in model time units. |
| `double` | `mtbf(IDowntime<?> downtime)` | Returns mean time before failure for specified Downtime block (in model time units). |
| `double` | `mtbf(IDowntime<?> downtime, TimeUnits units)` | Returns mean time before failure for specified Downtime block (in specified time units). |
| `double` | `mtbf(TimeUnits units)` | Returns mean time before failure in specified time units. |
| `double` | `mttr()` | Returns mean time to repair in model time units. |
| `double` | `mttr(IDowntime<?> downtime)` | Returns mean time to repair for specified Downtime block (in model time units). |
| `double` | `mttr(IDowntime<?> downtime, TimeUnits units)` | Returns mean time to repair for specified Downtime block (in specified time units). |
| `double` | `mttr(TimeUnits units)` | Returns mean time to repair in specified time units. |
| `void` | `repair()` |  |
| `void` | `resetStats()` |  |
| `void` | `restartMaintenanceTriggers(IDowntime<?> block)` |  |
| `void` | `startMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stopMaintenanceManually(IDowntime<?> block)` |  |
