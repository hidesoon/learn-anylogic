*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/MarkupPort.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface MarkupPort

All Known Subinterfaces:
:   `NetworkPort`

All Known Implementing Classes:
:   `ConveyorPortImpl`, `ConveyorSpur`, `LevelGate`, `LiftPortImpl`, `NetworkPortImpl`

---

```
public interface MarkupPort
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getFullName()` |  |
| `Level` | `getLevel()` |  |
| `String` | `getName()` |  |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this markup port. |
| `Point` | `getXYZ()` |  |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this markup port. |
