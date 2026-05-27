*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AreaNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AreaNode<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AreaNode<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `IAreaNodeDescriptor<T>`, `IDescriptor`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<T>`

Direct Known Subclasses:
:   `PolygonalNode`, `RectangularNode`

---

```
@AnyLogicInternalAPI
public abstract class AreaNode<T extends Agent>
extends Node
implements IAreaNodeDescriptor<T>, Iterable<T>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AreaNode)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AreaNode()` |  |
| `AreaNode(Agent owner)` |  |
| `AreaNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, boolean speedRestriction, double maxSpeedInMPS, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. |
| `AreaNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> areaNodeDescriptor, double x, double y, double z, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `accessRestrictionCondition(T agent)` | Evaluates the area access condition for the specified agent |
| `void` | `addAgent(T agent)` |  |
| `void` | `addAreaDataSource(IAreaDataSource areaDataSource)` |  |
| `void` | `addAttractor(double x, double y, double orientation)` | Sets the position choice mode to PositionChoiceMode.POSITION\_CHOICE\_BY\_ATTRACTORS and adds the specified attractor to this area. |
| `void` | `addAttractor(Attractor attractor)` | Deprecated. |
| `List<T>` | `agents()` | Returns the list of agents currently present in this area. |
| `abstract double` | `area(AreaUnits units)` | Returns the area of this area, measured in area units |
| `void` | `close()` | Closes the area. |
| `boolean` | `contains(Agent agent)` | Returns true, if the area contains the specified agent, otherwise returns false. |
| `double` | `density(AreaUnits units)` | Returns the average value of density inside the area, measured in agents per area units. |
| `AreaAccessRestrictionType` | `getAccessRestrictionType()` | Returns access restriction type. |
| `List<Agent>` | `getAdmittedTransporters()` | Returns the list of transporters admitted to the area. |
| `List<T>` | `getAgentsWaitingToEnter()` | Returns a list of agents waiting in the queue to enter the area. |
| `List<Attractor>` | `getAttractors()` | Returns the list of this area attractors |
| `int` | `getCapacity()` | Returns capacity for access restriction |
| `Color` | `getFillColor()` | Returns the fill color of the markup element, or `null` if markup element has no fill color or has textured fill (in this case [`getFillTexture()`](#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the markup element, if the markup element has fill texture |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `LineStyle` | `getLineStyle()` | Returns the line style of the markup element: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getLineWidth()` | Returns the line width of the markup element. |
| `double` | `getMaxSpeed(SpeedUnits units)` | Returns the maximum speed in the specified speed units |
| `int` | `getNumberOfAdmittedAgents()` | Returns the number of agents admitted to the area. |
| `int` | `getNumberOfAdmittedTransporters()` | Returns the number of transporters admitted to the area. |
| `List<Agent>` | `getPeds()` | Returns the list of pedestrians currently present in this area. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `PositionChoiceMode` | `getPositionChoiceMode()` | Returns the position choice mode for this area. |
| `Class<? extends Agent>` | `getRestrictedAgentClass()` | Returns the restricted agent class |
| `Schedule<Boolean>` | `getSchedule()` | Returns the schedule of area access restriction |
| `Slope` | `getSlope()` | Returns the slope for current area |
| `double` | `getThroughput(RateUnits units)` | Returns the maximum number of agents that can enter the area per rate unit. |
| `double` | `getX()` | Returns the x coordinate of the markup element. |
| `double` | `getY()` | Returns the y coordinate of the markup element. |
| `double` | `getZ()` | Returns the z coordinate of the markup element, relative to level/network, if any is defined. |
| `double` | `getZ(double x, double y)` | Returns the z coordinate of the given point |
| `boolean` | `isAccessRestricted()` | Returns `true` if the access to the area is restricted and `false` otherwise |
| `boolean` | `isAllowedToEnter(T agent)` |  |
| `boolean` | `isApplied(T agent)` |  |
| `boolean` | `isAvoidedIfClosed()` | Returns the value of *avoided if closed* parameter |
| `boolean` | `isLimitSpeed()` | Return true if speed is limited in this node, false otherwise |
| `boolean` | `isOpen()` | Returns true if the area is open and false if the area is closed. |
| `boolean` | `isReadyToEnter(T agent)` |  |
| `boolean` | `isSpeedRestricted()` | Checks whether the area has speed restriction enabled. |
| `Iterator<T>` | `iterator()` | Returns the iterator for all agents inside the area. |
| `void` | `notifyCancelReadyToEnter(T agent)` |  |
| `boolean` | `notifyReadyToEnter(T agent)` |  |
| `void` | `notifyReadyToEnter2(T agent)` |  |
| `void` | `notifyReadyToExit(T agent)` |  |
| `void` | `onClose()` | Code executed when the area closes. |
| `void` | `onEnter(T agent)` | Code executed when the agent enters the area. |
| `void` | `onEnterDenied(T agent)` | Code that will be executed when the agent attempts to enter the node but is not allowed to. |
| `void` | `onExit(T agent)` | Code executed when the agent exits the area. |
| `void` | `onOpen()` | Code executed when the area opens. |
| `void` | `open()` | Opens the area. |
| `void` | `recalculateAccessibility()` | The method recalculates the accessibility of the area node. |
| `void` | `removeAgent(T agent)` |  |
| `void` | `removeAreaDataSource(IAreaDataSource areaDataSource)` |  |
| `void` | `removeFromQueue(T agent)` |  |
| `void` | `restrictAccessByCapacity(int number)` | Enables restriction of access to the node by capacity. |
| `void` | `restrictAccessBySchedule(Schedule<Boolean> schedule)` | Enables restriction of access to the node by schedule. |
| `void` | `restrictAccessByThroughput(double throughput, RateUnits units)` | Enables restriction of access to the node by throughput. |
| `void` | `restrictAccessManually(boolean initiallyClosed)` | Enables restriction of access to the node manually. |
| `void` | `restrictSpeed(double maxSpeed, SpeedUnits units)` | Enables speed restriction for the node. |
| `void` | `setAccessRestricted(boolean restricted)` | Sets restriction of access. |
| `void` | `setAccessRestrictionType(AreaAccessRestrictionType accessRestrictionType)` | Sets access restriction type. |
| `void` | `setAvoidedIfClosed(boolean avoided)` | Sets the value of *avoided if closed* parameter |
| `void` | `setCapacity(int number)` | Sets capacity for access restriction |
| `void` | `setLimitSpeed(boolean restriction)` | Deprecated. use [`restrictSpeed(double, SpeedUnits)`](#restrictSpeed(double,com.anylogic.engine.SpeedUnits)) instead |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setLineStyle(LineStyle lineStyle)` | Sets the line style of the markup element: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `void` | `setLineWidth(double width)` | Sets the line width of the markup element, 0 means thinnest possible |
| `void` | `setMaxSpeed(double maxSpeed, SpeedUnits units)` | Deprecated. use [`restrictSpeed(double, SpeedUnits)`](#restrictSpeed(double,com.anylogic.engine.SpeedUnits)) instead |
| `void` | `setOpen(boolean open)` | Makes the area either open or closed to the incoming agents. |
| `void` | `setPos(double x, double y, double z)` | Sets coordinates of the markup element |
| `void` | `setPositionChoiceMode(PositionChoiceMode positionChoiceMode)` | Sets the position choice mode for this area. |
| `void` | `setRestrictedAgentClass(Class<? extends Agent> restrictedClass)` | Sets the restricted agent class |
| `void` | `setSchedule(Schedule<Boolean> schedule)` | Sets the schedule of area access restriction |
| `void` | `setSlope(Slope slope)` | Sets the slope for current area |
| `void` | `setSpeedRestricted(boolean restriction)` | Sets the speed restriction in the area. |
| `void` | `setThroughput(double throughput, RateUnits units)` | Sets the maximum number of agents that can enter the area per rate unit. |
