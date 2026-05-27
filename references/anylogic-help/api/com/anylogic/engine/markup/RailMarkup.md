*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RailMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface RailMarkup

All Superinterfaces:
:   `Serializable`

All Known Implementing Classes:
:   `AbstractRailwayMarkup`, `PositionOnTrack`, `RailwaySwitch`, `RailwayTrack`

---

```
public interface RailMarkup
extends Serializable
```

Interface for all space markup elements which may be contained in a 'rail yard',
e.g. tracks, switches

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `RailwayNetwork` | `getRailYard()` | Returns rail yard associated with this space markup element or `null` if this element has no rail yard |
