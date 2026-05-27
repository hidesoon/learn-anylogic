*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/rail/IRailStopLineDescriptor.html>*

---

Package [com.anylogic.engine.markup.rail](package-summary.md)

# Interface IRailStopLineDescriptor<T extends Agent>

All Superinterfaces:
:   `IDescriptor`, `IMarkupLibraryDescriptor`

All Known Implementing Classes:
:   `PositionOnTrack`

---

```
public interface IRailStopLineDescriptor<T extends Agent>
extends IDescriptor
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `onTrainEnter(T train)` |  |
| `void` | `onTrainExit(T train)` |  |
