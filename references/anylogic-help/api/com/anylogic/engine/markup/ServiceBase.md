*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceBase.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServiceBase<S extends ServiceUnit<Q>,Q extends QueueUnit>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.ServiceBase<S,Q>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ServiceWArea`, `ServiceWLine`

---

```
public abstract class ServiceBase<S extends ServiceUnit<Q>,Q extends QueueUnit>
extends AbstractLevelMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServiceBase)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addService(S s)` | Adds a service point to the service. |
| `boolean` | `contains(double px, double py)` | Always returns `false` |
| `Q` | `getClosestQueue(ServiceUnit<Q> serviceUnit)` | Returns the queue that is the closest to the service, no matter whether it is empty or not. |
| `Q` | `getClosestQueueNotEmpty(ServiceUnit<Q> serviceUnit)` | Returns the non-empty queue that is the closest to the service element. |
| `Q` | `getLongestQueue(ServiceUnit<Q> serviceUnit)` | Returns the queue containing the maximum number of pedestrians. |
| `List<Agent>` | `getPeds(Q queue)` | Returns the list of agents (pedestrians) staying in the given queue |
| `abstract List<Q>` | `getQueues()` | Returns the list of all queues of this service |
| `Color` | `getServiceColor()` | Returns the color of the service |
| `List<S>` | `getServices()` | Returns the list of all service points in this service |
| `Q` | `getShortestQueue(Agent agent)` | Returns the queue containing the least number of pedestrians. |
| `double` | `getUtilization()` | Returns the service utilization: the average utilization of all service units. |
| `boolean` | `isServiceSuspended(ServiceUnit<Q> serviceUnit)` | Returns true if the service unit is in suspended state; returns false otherwise. |
| `void` | `onDestroy()` |  |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `queueSize(Q queue)` | Returns the number of agents (pedestrians) staying in the given queue |
| `void` | `resetStats()` | Resets all statistics of all service units. |
| `void` | `setDataSource(ServiceDataSource<Q> dataSource)` |  |
| `void` | `setServiceColor(Color serviceColor)` | Sets the color of the service |
| `void` | `setServiceSuspended(ServiceUnit<Q> serviceUnit, boolean suspended)` | Sets the service unit to suspended state if the suspended value is true; sets the service unit to active state otherwise. |
