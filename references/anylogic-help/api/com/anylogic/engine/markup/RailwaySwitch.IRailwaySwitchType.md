*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RailwaySwitch.IRailwaySwitchType.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface RailwaySwitch.IRailwaySwitchType

All Known Implementing Classes:
:   `RailwaySwitch.IRailwaySwitchType.BaseType`, `RailwaySwitch.IRailwaySwitchType.SingleSlipType`

Enclosing class:
:   [RailwaySwitch](RailwaySwitch.md "class in com.anylogic.engine.markup")

---

```
@AnyLogicInternalAPI
public static interface RailwaySwitch.IRailwaySwitchType
```

## Nested Class Summary

| Modifier and Type | Interface | Description |
| --- | --- | --- |
| `static class` | `RailwaySwitch.IRailwaySwitchType.BaseType` |  |
| `static class` | `RailwaySwitch.IRailwaySwitchType.SingleSlipType` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static RailwaySwitch.IRailwaySwitchType` | `createAllToAll()` |  |
| `static RailwaySwitch.IRailwaySwitchType` | `createDoubleSlip()` |  |
| `static RailwaySwitch.IRailwaySwitchType` | `createSingleSlip(RailwayTrack track)` |  |
| `RailwaySwitchType` | `getType()` |  |
