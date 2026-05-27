*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceWLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServiceWLine<S extends ServiceUnit<QueuePath>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ServiceBase](ServiceBase.md "class in com.anylogic.engine.markup")<S,[QueuePath](QueuePath.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.ServiceWLine<S>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ServiceWLine<S extends ServiceUnit<QueuePath>>
extends ServiceBase<S,QueuePath>
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServiceWLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServiceWLine()` |  |
| `ServiceWLine(Agent owner, ShapeDrawMode drawMode, boolean isPublic, ServiceWLineType type, boolean bidirectional, S[] services, QueuePath[] queues, QueuePath[] reverseQueues, ServiceQueueChoicePolicy queueChoicePolicy, boolean waitForExit, Color serviceColor, Color queueColor, Color reverseQueueColor)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ServiceWLine(Agent owner, ShapeDrawMode drawMode, boolean isPublic, ServiceWLineType type, boolean bidirectional, S[] services, QueuePath[] queues, QueuePath[] reverseQueues, ServiceQueueChoicePolicy queueChoicePolicy, boolean waitForExit, Color serviceColor, Color queueColor, Color reverseQueueColor, ServiceGroupBehaviorMode groupBehaviorMode, ServiceGroupBehavior groupBehavior, AreaNode groupWaitingArea)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addQueue(QueuePath queue)` | Adds a queue to this service. |
| `void` | `addReverseQueue(QueuePath queue)` | Adds a reverse queue to this service. |
| `QueuePath` | `customSelectQueue(S serviceUnit)` | This method should be overridden to return queue in `CUSTOM` queue choice policy |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `ServiceGroupBehavior` | `getGroupBehavior()` | Returns the currently set group behavior for this service with lines |
| `ServiceGroupBehaviorMode` | `getGroupBehaviorMode()` | Returns currently set group behavior mode for this service with lines |
| `AreaNode` | `getGroupWaitingArea()` | Returns the area markup element (if any) associated with the current service with lines. |
| `ServiceQueueChoicePolicy` | `getQueueChoicePolicy()` | Returns the queue choice policy for this service with lines |
| `Color` | `getQueueColor()` | Returns the color of the queue elements. |
| `List<QueuePath>` | `getQueues()` | Returns the list of all queues of this service |
| `Color` | `getReverseQueueColor()` | Returns the color of the reverse queue elements. |
| `List<QueuePath>` | `getReverseQueues()` | Returns the list of all reverse queues of this service |
| `QueuePath` | `getShortestQueue(Agent agent, boolean reverse)` | Returns the queue containing the least number of pedestrians. |
| `ServiceWLineType` | `getType()` | Returns the type of this service |
| `boolean` | `isBidirectional()` | Returns true if the service with lines is bidirectional, i.e. |
| `boolean` | `isWaitForExit()` | Returns true if the service with lines is set to wait for exit, i.e. |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `queuePriority(QueuePath queue)` | This method should be overridden to return queue in `PRIORITY` queue choice policy |
| `void` | `setBidirectional(boolean bidirectional)` | Sets this service to be bidirectional allowing pedestrians to pass services in both directions if the argument is true. |
| `void` | `setGroupBehavior(ServiceGroupBehavior groupBehavior)` | Sets the group behavior for this service with lines |
| `void` | `setGroupBehaviorMode(ServiceGroupBehaviorMode groupBehaviorMode)` | Sets the behavior mode for groups in this service with lines |
| `void` | `setGroupWaitingArea(AreaNode groupWaitingArea)` | Sets the area markup element for the group members to wait in. |
| `void` | `setQueueChoicePolicy(ServiceQueueChoicePolicy queueChoicePolicy)` | Sets the policy for choosing a queue to enter by a pedestrian. |
| `void` | `setQueueColor(Color queueColor)` | Sets the color of the queue elements. |
| `void` | `setReverseQueueColor(Color reverseQueueColor)` | Sets the color of the reverse queue elements. |
| `void` | `setType(ServiceWLineType type)` | Sets the type of this service. |
| `void` | `setWaitForExit(boolean waitForExit)` | If the argument is true, the service with lines will be set to make pedestrians wait for exit, i.e. |
