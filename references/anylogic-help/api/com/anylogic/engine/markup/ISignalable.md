*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ISignalable.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface ISignalable

All Known Implementing Classes:
:   `RoadLanesConnector`, `StopLine`

---

```
public interface ISignalable
```

Road element which may have traffic light signal. Either stop line or lane connector

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `TrafficLightSignal` | `getSignal()` |  |
| `void` | `registerListener(SignalChangeListener listener)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setSignal(TrafficLightSignal signal)` |  |
