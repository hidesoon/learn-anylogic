*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorPath.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorPath<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorPath<T>

All Implemented Interfaces:
:   `IMaintenanceable`, `AggregatableAnimationElement`, `AnimationMovingLocationProvider`, `AnimationStaticLocationProvider`, `HasBoundingRectangle`, `HasCenterPoint`, `HasLevel`, `IMaintenanceableMarkup`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `IPath<ConveyorNode<?>>`, `com.anylogic.engine.markup.material_handling.IConveyorPathDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialAreaLocation<T>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IMaterialPointLocation<T>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<MarkupSegment>`

---

```
public class ConveyorPath<T extends Agent>
extends ConveyorMarkupElement<T>
implements IPath<ConveyorNode<?>>, Iterable<MarkupSegment>, HasBoundingRectangle, HasCenterPoint, IMaintenanceableMarkup, com.anylogic.engine.markup.material_handling.IConveyorPathDescriptor<T>
```

Conveyor is the space markup shape that graphically defines a conveyor.
You simulate how material items are transported by conveyors using the AnyLogic Material Handling Library blocks Convey, ConveyorEnter and ConveyorExit.

Several conveyors can be connected together.
Altogether they compose a conveyor network.
In the conveyor network, movement is always performed along the shortest conveyor between the origin and the destination nodes.

Conveyor starts with the defined initial speed and accelerates to the defined maximum speed, keeping it until stops.

Unlike many other space markup elements that just define the element's location and size graphically,
the conveyor element also provides users with a set of actions, which are used to define additional agent behavior.

**Conveyor types**
By default the roller conveyor is used, but if required you can set it to be of any available type:

* **Roller** - It is an accumulating type of a conveyor.
  If an agent is stopped on it, the rollers will keep on rolling,
  bringing all the preceding material items to the stopped one, thus forming a line of agents.
  The Gap parameter defines how close the material items can be pushed to each other.
  If the Gap is set to 0, collisions are inevitable.
* **Belt** - It is not an accumulating type of a conveyor.
  If an agent is stopped, the whole conveyor stops to prevent collision of material items.
  The distance between the items is defined by the Gap parameter.
* **Fixed cell** - It is not an accumulating type of a conveyor.
  The conveyor is a succession of cells of specified size.
  Agents are placed in the center of the conveyor cell.
  One conveyor cell can contain only one material item.
  The Gap parameter defines the distance between the conveyor cells.
  If an agent is stopped, the whole conveyor stops.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorPath)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorPath()` |  |
| `ConveyorPath(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorPath(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double widthInMeters, Paint color, boolean drawStands, double standsLevel, com.anylogic.engine.markup.material_handling.IConveyorPathDescriptor<T> descriptor, ConveyorNode<?> source, ConveyorNode<?> target, MarkupSegment... segments)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `ConveyorPath(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double widthInMeters, Paint color, boolean drawStands, double standsLevel, com.anylogic.engine.markup.material_handling.IConveyorPathDescriptor<T> descriptor, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `void` | `changeDirection()` | Changes current direction of this conveyor to the opposite |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(Agent agent)` |  |
| `boolean` | `containsSq(double px, double py, double squareDistance)` |  |
| `default NetworkPort` | `createPort(IPath<?> path, PathEndType endType)` |  |
| `default NetworkPort` | `createPort(IPath<?> path, PathEndType endType, NetworkPort pairedPort)` |  |
| `NetworkPort` | `createPort(PathEndType endType)` | Creates and returns a Network Port located on specified conveyor's end |
| `NetworkPort` | `createPort(PathEndType endType, NetworkPort pairedPort)` | Creates and returns a Network Port located on specified conveyor's end and pairs created port with specified one |
| `NetworkPort` | `createPortInternal(PathEndType endType)` |  |
| `void` | `fail()` | Initiates conveyor failure. |
| `double` | `getAcceleration(AccelerationUnits units)` | Returns the acceleration of the conveyor in the specified acceleration units. |
| `T` | `getAgent(double offset, LengthUnits units)` |  |
| `T` | `getAgent(int index)` | Returns the agent at a given position (counted from 0, from the exit). |
| `List<T>` | `getAgents()` | Returns the list of agents (material items) that are currently conveyed |
| `List<T>` | `getAgents(double offset, double length, LengthUnits units)` |  |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getCellSize(LengthUnits units)` |  |
| `Position` | `getCenter(Position out)` |  |
| `double` | `getCurrentAcceleration(AccelerationUnits units)` |  |
| `double` | `getCurrentSpeed(SpeedUnits units)` | Returns the current speed of the conveyor in the specified speed units. |
| `double` | `getDeceleration(AccelerationUnits units)` | Returns the deceleration of the conveyor in the specified acceleration units. |
| `ConveyorDirection` | `getDirection()` | Returns the direction of this conveyor |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition()` | Returns the end position |
| `Position` | `getEndPosition(Position out)` | Returns the end position |
| `double` | `getGap(LengthUnits units)` | Returns the minimum required gap between material items of this conveyor (in the specified length units). |
| `double` | `getInitialSpeed(SpeedUnits units)` | Returns the initial speed of the conveyor in the specified speed units. |
| `com.anylogic.engine.markup.material_handling.IConveyorPathDescriptor<T>` | `getLibraryDescriptor()` |  |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`IPath.getLineTexture()`](IPath.md#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getLineWidth()` | **This method is internal and shouldn't be called by user.**  *it may be removed in future.* |
| `double` | `getMaxSpeed(SpeedUnits units)` | Returns the maximum speed of the conveyor in the specified speed units. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `double` | `getOffset3D(double offset2D)` |  |
| `ConveyorNode<?>` | `getOtherNode(ConveyorNode<?> n)` | Returns the second (other) node of the conveyor. |
| `Object` | `getPMLProxy()` |  |
| `Position` | `getPosition(double value, double maxValue, Position out)` | Returns position with offset corresponding to the given `value`, assuming that `0` is start and `maxValue` is end |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Position` | `getPositionAt2DOffset(double offset, Position out)` |  |
| `Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](IPath.md#getStartPoint(com.anylogic.engine.Point)). |
| `Position` | `getPositionAtOffset(double offset, Position out)` | Returns the position at specified offset |
| `List<PositionOnConveyor<T>>` | `getPositionsOnConveyor()` | Returns the list of all PositionOnConveyor elements on this conveyor |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `ConveyorNode<?>` | `getSource()` | Returns the source node of the conveyor. |
| `List<ConveyorSpur<T>>` | `getSplitMerges()` | Deprecated. will be removed in the next release. |
| `List<ConveyorSpur<T>>` | `getSpurs()` | Returns the list of conveyor spur elements of this conveyor. |
| `double` | `getStandsLevel()` | Returns the base level Z-level to draw conveyor stands from. |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition()` | Returns the start position |
| `Position` | `getStartPosition(Position out)` | Returns the start position |
| `ConveyorState` | `getState()` |  |
| `List<ConveyorStation<T>>` | `getStations()` | Returns the list of all stations of this conveyor. |
| `double` | `getStatisticsStartTime()` |  |
| `ConveyorNode<?>` | `getTarget()` | Returns the target node of the conveyor. |
| `ConveyorType` | `getType()` | Returns the type of this conveyor. |
| `double` | `getUtilization()` | Returns the conveyor utilization: the fraction of time the conveyor was busy. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of this conveyor |
| `boolean` | `isAccumulating()` | Returns true if the conveyor can accumulate objects, false otherwise. |
| `boolean` | `isBidirectional()` | Returns the 'bidirectional' property (`true` by default). |
| `boolean` | `isChangingDirection()` | Returns true if this conveyor is in the process of changing direction, returns false otherwise |
| `boolean` | `isDrawStands()` | Returns `true` if this conveyor is drawn with stands |
| `boolean` | `isFailed()` | Returns true if the conveyor is currently failed, returns false otherwise. |
| `boolean` | `isMaintenanceActive(IDowntime<?> block)` |  |
| `boolean` | `isMaximumPriority()` | Returns true if the conveyor has the greatest priority. |
| `boolean` | `isObstacle()` | Returns true if this conveyor is considered an obstacle by transporters moving in free space mode. |
| `boolean` | `isReversible()` | Returns the 'reversible' property (`false` by default). |
| `boolean` | `isStopped()` | Returns true if the conveyor is currently stopped, false otherwise. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `double` | `length()` | Returns the length of markup element, used e.g. |
| `double` | `length(LengthUnits units)` | Returns the length of markup element, used e.g. |
| `double` | `mtbf()` | Returns mean time between failures in model time units. |
| `double` | `mtbf(IDowntime<?> downtime)` | Returns mean time between failures for specified Downtime block (in model time units). |
| `double` | `mtbf(IDowntime<?> downtime, TimeUnits units)` | Returns mean time between failures for specified Downtime block (in specified time units). |
| `double` | `mtbf(TimeUnits units)` | Returns mean time between failures in specified time units. |
| `double` | `mttr()` | Returns mean time to repair in model time units. |
| `double` | `mttr(IDowntime<?> downtime)` | Returns mean time to repair for specified Downtime block (in model time units). |
| `double` | `mttr(IDowntime<?> downtime, TimeUnits units)` | Returns mean time to repair for specified Downtime block (in specified time units). |
| `double` | `mttr(TimeUnits units)` | Returns mean time to repair in specified time units. |
| `void` | `onDirectionChanged(List<T> agents)` |  |
| `void` | `onLeadingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onLeadingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onMotionChanged()` |  |
| `void` | `onStarted()` |  |
| `void` | `onStopped()` |  |
| `void` | `onTrailingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `double` | `priority(T agent)` |  |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `boolean` | `removeAgent(Agent agent)` | Removes the given agent from the conveyor. |
| `void` | `repair()` | Repairs conveyor, makes it available again. |
| `void` | `resetStats()` |  |
| `void` | `restartMaintenanceTriggers(IDowntime<?> block)` |  |
| `void` | `run()` | Launches the conveyor. |
| `void` | `setAcceleration(double acceleration, AccelerationUnits units)` | Sets the new acceleration for the conveyor in the specified acceleration units. |
| `void` | `setBidirectional(boolean bidirectional)` | Sets the 'bidirectional' property (`true` by default). |
| `void` | `setCellSize(double size, LengthUnits units)` |  |
| `void` | `setDeceleration(double deceleration, AccelerationUnits units)` | Sets the new deceleration for the conveyor in the specified acceleration units. |
| `void` | `setDirection(ConveyorDirection direction)` | Sets the direction of this conveyor. |
| `void` | `setDowntimeBlocks(IDowntime<?>[] downtimeBlocks)` |  |
| `void` | `setDrawStands(boolean drawStands)` | Sets to draw stands for conveyor or not |
| `void` | `setGap(double gapBetweenItems, LengthUnits units)` |  |
| `void` | `setInitialSpeed(double initialSpeed, SpeedUnits units)` |  |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setLineWidth(double widthInPixels)` | **This method is internal and shouldn't be called by user.**  *it may be removed in future.* |
| `void` | `setMaximumPriority(boolean maximumPriority)` |  |
| `void` | `setMaxSpeed(double maxSpeed, SpeedUnits units)` | Sets the new maximum speed of the conveyor in the specified speed units. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this conveyor as an obstacle for transporters moving in free space mode. |
| `void` | `setReversible(boolean reversible)` | Sets the 'reversible' property (`true` by default). |
| `void` | `setSource(ConveyorNode<?> node)` | Sets source node of this path. |
| `void` | `setStandsLevel(double standsLevel)` | Set the base Z-level to draw conveyor stands from. |
| `void` | `setTarget(ConveyorNode<?> node)` | Sets source node of this path. |
| `void` | `setType(ConveyorType type)` | Sets the type of this conveyor. |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of this conveyor |
| `int` | `size()` | Returns the number of agents currently being conveyed. |
| `void` | `startMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stop()` | Stops the conveyor. |
| `void` | `stopMaintenanceManually(IDowntime<?> block)` |  |
| `String` | `toString()` |  |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `void` | `validate()` |  |
