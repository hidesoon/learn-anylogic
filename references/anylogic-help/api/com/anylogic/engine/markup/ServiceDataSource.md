*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceDataSource.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface ServiceDataSource<Q extends QueueUnit>

All Superinterfaces:
:   `Serializable`

---

```
public interface ServiceDataSource<Q extends QueueUnit>
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Q` | `getClosestQueue(ServiceUnit<Q> serviceUnit)` |  |
| `Q` | `getClosestQueueNotEmpty(ServiceUnit<Q> serviceUnit)` |  |
| `Q` | `getLongestQueue(ServiceUnit<Q> serviceUnit)` |  |
| `List<Agent>` | `getPeds(Q queue)` | Returns the list of agents (pedestrians) staying in the given queue |
| `double` | `getServiceUtilization(ServiceUnit<Q> serviceUnit)` | Returns the service unit utilization. |
| `Q` | `getShortestQueue(Agent agent, boolean reverse)` |  |
| `boolean` | `isServiceSuspended(ServiceUnit<Q> serviceUnit)` |  |
| `void` | `onQueueCapacityChanged(Q queue)` |  |
| `int` | `queueSize(Q queue)` | Returns the number of agents (pedestrians) staying in the given queue |
| `void` | `resetServiceStats(ServiceUnit<Q> serviceUnit)` | Resets all service unit statistics. |
| `void` | `setServiceSuspended(ServiceUnit<Q> serviceUnit, boolean suspended)` |  |
