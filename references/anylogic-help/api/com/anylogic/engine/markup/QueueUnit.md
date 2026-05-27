*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/QueueUnit.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface QueueUnit

All Known Implementing Classes:
:   `QueueArea`, `QueuePath`, `QueueSerpentine`

---

```
public interface QueueUnit
```

Interface for queues which are used in Service space markup elements

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `capacity()` | Returns the capacity of the queue |
| `String` | `getName()` |  |
| `List<Agent>` | `getPeds()` | Returns the collection of agents in this queue.  The first one is the queue head, the last one is the queue tail |
| `boolean` | `isCapacityLimited()` | Returns `true` if this queue has limited capacity |
| `int` | `size()` | Returns the current size of the queue |
