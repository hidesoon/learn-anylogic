*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceUnit.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServiceUnit<Q extends QueueUnit>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[ServiceBase](ServiceBase.md "class in com.anylogic.engine.markup")<?,Q>>

com.anylogic.engine.markup.ServiceUnit<Q>

All Implemented Interfaces:
:   `HasBoundingRectangle`, `Serializable`

Direct Known Subclasses:
:   `ServiceLine`, `ServicePoint`

---

```
public abstract class ServiceUnit<Q extends QueueUnit>
extends AbstractMarkupSubunit<ServiceBase<?,Q>>
implements HasBoundingRectangle
```

Base class for service units which are used in Service space markup elements

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServiceUnit)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Q` | `customSelectQueue()` | This method should be overridden to return queue in `CUSTOM` queue choice policy |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Q` | `getClosestQueue()` | Returns the queue that is the closest to the service, no matter whether it is empty or not. |
| `Q` | `getClosestQueueNotEmpty()` | Returns the non-empty queue that is the closest to the service element. |
| `Color` | `getColor()` | Returns the color of the markup shape. |
| `ServiceQueueChoicePolicy` | `getCustomQueueChoicePolicy()` | Returns custom queue choice policy. |
| `Q` | `getLongestQueue()` | Returns the queue containing the maximum number of pedestrians. |
| `boolean` | `isSuspended()` | Returns true if the service element is in suspended state; returns false otherwise. |
| `int` | `queuePriority(Q queue)` | This method should be overridden to return queue in `PRIORITY` queue choice policy |
| `void` | `setColor(Color color)` | Sets the color of the markup shape. |
| `void` | `setSuspended(boolean suspended)` | Sets the service element to suspended state if the suspended value is true; sets the service element to active state otherwise. |
