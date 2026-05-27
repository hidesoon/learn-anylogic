*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/descriptors/IAreaDataSource.html>*

---

Package [com.anylogic.engine.markup.descriptors](package-summary.md)

# Interface IAreaDataSource

---

```
public interface IAreaDataSource
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(Agent agent)` |  |
| `Collection<Agent>` | `getAllAgents()` |  |
| `default int` | `getNumberOfTransporters()` |  |
| `default Collection<Agent>` | `getPeds()` |  |
| `default Collection<Agent>` | `getTransporters()` |  |
| `default void` | `onCancelReadyToEnter(Agent agent)` |  |
| `default void` | `onClose()` |  |
| `default void` | `onEnter(Agent agent)` |  |
| `default void` | `onExit(Agent agent)` |  |
| `default void` | `onOpen()` |  |
| `default void` | `onReadyToEnter(Agent agent)` |  |
| `default void` | `onUpdateQueue2(Agent agent)` |  |
| `default void` | `recalculateAccessibility()` |  |
| `int` | `size()` |  |
