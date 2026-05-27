*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PedFlowStatisticsDataSource.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface PedFlowStatisticsDataSource

All Superinterfaces:
:   `Serializable`

---

```
public interface PedFlowStatisticsDataSource
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `countPeds()` | Returns total number of pedestrians passed through this line |
| `double` | `intensity()` | Returns the average pedestrian flow intensity on the line, measured in pedestrians per hour per meter |
| `void` | `reset()` | Resets the average traffic and intensity. |
| `double` | `traffic()` | Returns the average of traffic flow statistics through the line, measured in pedestrians per hour |
