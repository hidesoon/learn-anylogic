*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ShortestPathData.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ShortestPathData<N extends INode<N,P>,P extends IPath<N>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.ShortestPathData<N,P>

Type Parameters:
:   `N` - network node, an instance of `INode`
:   `P` - network path, an instance of `IPath`

All Implemented Interfaces:
:   `IPathData`, `Serializable`

Direct Known Subclasses:
:   `ContinuousShortestPathData`, `GISShortestPathData`

---

```
public abstract class ShortestPathData<N extends INode<N,P>,P extends IPath<N>>
extends Object
implements IPathData
```

This class keeps data to move an agent through a network.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ShortestPathData)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `double` | `distance` |  |
| `SimpleDirection` | `fromDirection` | Tells, where to go from ([`fromPath`](#fromPath), [`fromOffset`](#fromOffset)) |
| `N` | `fromNode` |  |
| `double` | `fromOffset` |  |
| `P` | `fromPath` |  |
| `double` | `fromX` |  |
| `double` | `fromY` |  |
| `double` | `fromZ` |  |
| `INetwork<N,P>` | `network` |  |
| `Point` | `source` |  |
| `double` | `sourceRotation` |  |
| `double` | `sourceSegmentDistance` |  |
| `double` | `sourceVerticalRotation` |  |
| `Point` | `target` |  |
| `double` | `targetRotation` |  |
| `double` | `targetSegmentDistance` |  |
| `double` | `targetVerticalRotation` |  |
| `SimpleDirection` | `toDirectionReverse` | Tells from which side we come to ([`toPath`](#toPath), [`toOffset`](#toOffset)), in terms of target POV (the 'reverse' word stands for it) |
| `P` | `toHubIncomingPath` |  |
| `N` | `toNode` |  |
| `double` | `toOffset` |  |
| `P` | `toPath` |  |
| `double` | `toX` |  |
| `double` | `toY` |  |
| `double` | `toZ` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShortestPathData()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract Position` | `getFromTargetPosition(double offset, Position out)` | Returns the Position object that corresponds to the point that lies at a certain distance from target point in the direction to the end point |
| `INetwork<N,P>` | `getNetwork()` | Returns the network for this path data |
| `abstract Position` | `getToSourcePosition(double offset, Position out)` | Returns the Position object that corresponds to the point that lies at a certain distance from start point in the direction to source point |
| `boolean` | `isPlainMovement()` | Checks if this shortest path data corresponds to plain movement |
| `void` | `reset()` |  |
| `abstract void` | `resetFromTargetDirection()` | Resets the direction from target to the stored toPoint |
| `abstract void` | `resetToSourceDirection()` | Resets the direction from the stored fromPoint to the source |
| `abstract void` | `setFromTargetDirection(Point toPoint)` | Sets the direction and rotations from the target point to the specified argument point |
| `abstract void` | `setToSourceDirection(Point fromPoint)` | Sets the direction and rotations from the specified argument point to the source point |
