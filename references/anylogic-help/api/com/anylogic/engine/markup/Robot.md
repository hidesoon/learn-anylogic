*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Robot.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Robot<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Robot<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `IMarkupLibraryDescriptor`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IRobotDescriptor<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Robot<T extends Agent>
extends AbstractLevelMarkup
implements com.anylogic.engine.markup.material_handling.IRobotDescriptor<T>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Robot)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Robot()` |  |
| `Robot(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, com.anylogic.engine.markup.material_handling.IRobotDescriptor<T> descriptor, double x, double y, double z, double[] linksLength, Color linksColor, Color endEffectorColor, double initialEndEffectorX, double initialEndEffectorY, double initialEndEffectorZ, double maxArmReach, boolean blockedZoneEnabled, double blockedZoneStartAngleRadians, double blockedZoneAngleRadians)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `attachAgentAnimation(T agent)` | Attaches agent animation to the robot end effector to perform agent transporting by the robot with `move()` command. |
| `double` | `averageCycleTime()` | Returns average time that takes the robot to transport or process an agent, in model time units |
| `double` | `averageCycleTime(TimeUnits timeUnits)` | Returns average time that takes the robot to transport or process an agent, in time units |
| `boolean` | `canReach(double x, double y, double z, RobotApproachType approachType)` | Returns `true` if the robot can reach specified point in space with specified approach type, `false` otherwise |
| `boolean` | `canReach(Agent agent, RobotApproachType direction)` | Returns `true` if the robot can reach the agent with specified approach type, `false` otherwise |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `detachAgentAnimation()` | Detaches previously attached agent animation from the robot end effector. |
| `void` | `fail()` | Sets the robot to `failed` state |
| `T` | `getAgent()` | Returns the agent, currently operated by robot, including the case when robot is moving to the agent. |
| `List<T>` | `getAgentsInQueue()` | Returns list of agents, waiting for the robot. |
| `double` | `getBlockedZoneAngle()` | Returns the delta angle of the robot's blocked zone in radians. |
| `double` | `getBlockedZoneAngle(AngleUnits units)` | Returns the delta angle of the robot's blocked zone. |
| `double` | `getBlockedZoneStartAngle()` | Returns the initial angle of the robot's blocked zone in radians. |
| `double` | `getBlockedZoneStartAngle(AngleUnits units)` | Returns the initial angle of the robot's blocked zone. |
| `RobotEndEffector` | `getEndEffector()` | Returns the end effector equipped by the robot. |
| `Color` | `getEndEffectorColor()` | Returns the color of robot's end effector |
| `double` | `getEndEffectorHorizontalRotation()` | Returns the horizontal (along Z axis) rotation of the end effector, in radians |
| `Position` | `getEndEffectorPosition()` | Returns the position of the robot's end effector |
| `double` | `getEndEffectorVerticalRotation()` | Returns the vertical (along y axis) rotation of the end effector, in radians |
| `double` | `getGripperLength()` | Returns the robot's gripper length in pixels. |
| `double` | `getGripperLength(LengthUnits units)` | Returns the robot's gripper length in the specified length units. |
| `double` | `getInitialEndEffectorX()` | Returns the initial X coordinate of the robot's end effector |
| `double` | `getInitialEndEffectorY()` | Returns the initial Y coordinate of the robot's end effector |
| `double` | `getInitialEndEffectorZ()` | Returns the initial Z coordinate of the robot's end effector |
| `com.anylogic.engine.markup.material_handling.IRobotDescriptor<T>` | `getLibraryDescriptor()` |  |
| `double[]` | `getLinkEnd(int i)` |  |
| `double[]` | `getLinkRotations(int i)` |  |
| `Color` | `getLinksColor()` | Returns the color of robot's links |
| `double[]` | `getLinksLength()` | Returns array of robot's links length, in pixels |
| `double[]` | `getLinksLength(LengthUnits units)` | Returns array of the robot's links length, in the specified length units |
| `double` | `getMaxArmReach()` | Returns maximum arm reach of the robot in pixels |
| `double` | `getMaxArmReach(LengthUnits lengthUnits)` | Returns the robot's maximum arm reach in the specified length units. |
| `RobotState` | `getState()` | Returns current robot state |
| `double` | `getStatisticsStartTime()` |  |
| `double` | `getUtilization()` | Returns the robot utilization: the fraction of time the robot was operating. |
| `double` | `getVacuumGripperHeightInPixels()` |  |
| `double` | `getVacuumGripperLength()` | Returns the robot's vacuum gripper length in pixels. |
| `double` | `getVacuumGripperLength(LengthUnits units)` | Returns the robot's vacuum gripper length in the specified length units. |
| `double` | `getVacuumGripperWidth()` | Returns the robot's vacuum gripper width in pixels. |
| `double` | `getVacuumGripperWidth(LengthUnits units)` | Returns the robot's vacuum gripper width in the specified length units. |
| `double` | `getWeldingGunLength()` | Returns the robot's welding gun length in pixels. |
| `double` | `getWeldingGunLength(LengthUnits units)` | Returns the robot's welding gun length in the specified length units. |
| `double` | `getX()` | Returns the X coordinate of the robot |
| `Point` | `getXYZ()` | Returns the point location of the robot |
| `double` | `getY()` | Returns the Y coordinate of the robot |
| `double` | `getZ()` | Returns Z coordinate of the robot relative to robot's level |
| `boolean` | `isBlockedZoneEnabled()` | Returns `true` if the robot has enabled blocked zone and `false` otherwise. |
| `boolean` | `isFailed()` | Returns `true` if the robot is failed and `false` otherwise. |
| `boolean` | `isObstacle()` | Returns `true` if this robot is considered an obstacle by transporters moving in free space mode. |
| `void` | `move(PointNode node, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits)` | Starts movement to place attached agent (if exists) or robot end effector in the target node. |
| `void` | `move(PointNode node, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, double safeHeight)` | Starts movement to place attached agent (if exists) or robot end effector in the target node. |
| `void` | `move(PointNode node, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state)` | Starts movement to place attached agent (if exists) or robot end effector in the target node. |
| `void` | `move(PointNode node, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state, double safeHeight)` | Starts movement to place attached agent (if exists) or robot end effector in the target node. |
| `void` | `move(Point point, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits)` | Starts movement to place attached agent (if exists) or robot end effector in the target point. |
| `void` | `move(Point point, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, double safeHeight)` | Starts movement to place attached agent (if exists) or robot end effector in the target point. |
| `void` | `move(Point point, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state)` | Starts movement to place attached agent (if exists) or robot end effector in the target point. |
| `void` | `move(Point point, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state, double safeHeight)` | Starts movement to place attached agent (if exists) or robot end effector in the target point. |
| `void` | `move(T agent, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits)` | Starts movement to place robot end effector at the target agent in position for pickup. |
| `void` | `move(T agent, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, double safeHeight)` | Starts movement to place robot end effector at the target agent in position for pickup. |
| `void` | `move(T agent, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state)` | Starts movement to place robot end effector at the target agent in position for pickup. |
| `void` | `move(T agent, RobotApproachType endEffectorApproaches, double time, TimeUnits timeUnits, RobotState state, double safeHeight)` | Starts movement to place robot end effector at the target agent in position for pickup. |
| `int` | `numberOfItemsProcessed()` | Returns the number of items, transported or processed by the robot since model start or since last `resetStats()` call |
| `void` | `onAgentProcessingEnd(T agent)` | Calls the robot's `onProcessEnd()` callback code |
| `void` | `onAgentProcessingStart(T agent)` | Calls the robot's `onProcessStart()` callback code |
| `void` | `onFailed()` | Calls the robot's `onFailed()` callback code |
| `void` | `onRelease(T agent)` | Calls the robot's `onRelease()` callback code |
| `void` | `onRepaired()` | Calls the robot's `onRepaired()` callback code |
| `void` | `onRobotMovementEnd()` | Calls the robot's `onMovementFinished()` callback code |
| `void` | `onRobotMovementStart()` | Calls the robot's `onMovementStart()` callback code |
| `void` | `onRobotStateChanged(T agent, RobotState newState)` | Calls the robot's `onRobotStateChanged()` callback code |
| `void` | `onSeize(T agent)` | Calls the robot's `onSeize()` callback code |
| `void` | `repair()` | Repairs the robot from `failed` state |
| `void` | `resetStats()` | Resets the robot utilization statistics. |
| `void` | `setBlockedZone(double startAngle, double deltaAngle, AngleUnits units)` | Sets the specified blocked zone of the robot in the specified angle units. |
| `void` | `setBlockedZoneAngle(double blockedZoneAngle)` | Sets the delta angle of the robot's blocked zone in radians. |
| `void` | `setBlockedZoneAngle(double angle, AngleUnits units)` | Sets the delta angle of the robot's blocked zone in the specified angle units. |
| `void` | `setBlockedZoneEnabled(boolean blockedZoneEnabled)` | Enables the robot's blocked zone if the parameter is `true` and disables if `false` |
| `void` | `setBlockedZoneStartAngle(double blockedZoneStartAngle)` | Sets the initial angle of the robot's blocked zone in raidans. |
| `void` | `setBlockedZoneStartAngle(double angle, AngleUnits units)` | Sets the initial angle of the robot's blocked zone in the specified units. |
| `void` | `setEndEffector(RobotEndEffector robotEndEffector)` | Sets the robot's end effector. |
| `void` | `setEndEffectorColor(Color color)` | Sets the specified color of robot's end effector |
| `void` | `setGripperLength(double gripperLength)` | Sets the robot's gripper length in pixels. |
| `void` | `setGripperLength(double gripperLength, LengthUnits units)` | Sets the robot's gripper length in the specified length units. |
| `void` | `setGripperWidth(double gripperWidth)` |  |
| `void` | `setInitialEndEffectorX(double initialEndEffectorX)` | Sets the initial X coordinate of the robot's end effector |
| `void` | `setInitialEndEffectorY(double initialEndEffectorY)` | Sets the initial Y coordinate of the robot's end effector |
| `void` | `setInitialEndEffectorZ(double initialEndEffectorZ)` | Sets the initial Z coordinate of the robot's end effector |
| `void` | `setLinksColor(Color color)` | Sets the specified color of robot's links |
| `void` | `setLinksLength(double[] linksLength)` | Sets the links length to the robot in pixels |
| `void` | `setLinksLength(double[] linksLength, LengthUnits units)` | Sets the links length to the robot in the specified units |
| `void` | `setMaxArmReach(double maxArmReach)` | Sets the robot's maximum arm reach in pixels. |
| `void` | `setMaxArmReach(double maxArmReach, LengthUnits units)` | Sets the robot's maximum arm reach in the specified length units. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this robot as an obstacle for transporters moving in free space mode. |
| `void` | `setVacuumGripperLength(double gripperLength)` | Sets the robot's vacuum gripper length in pixels. |
| `void` | `setVacuumGripperLength(double gripperLength, LengthUnits units)` | Sets the robot's vacuum gripper length in the specified length units. |
| `void` | `setVacuumGripperWidth(double gripperWidth)` | Sets the robot's vacuum gripper width in pixels. |
| `void` | `setVacuumGripperWidth(double gripperWidth, LengthUnits units)` | Sets the robot's vacuum gripper width in the specified length units. |
| `void` | `setWeldingGunLength(double weldingGunLength)` | Sets the robot's welding gun length in pixels. |
| `void` | `setWeldingGunLength(double weldingGunLength, LengthUnits units)` | Sets the robot's welding gun length in the specified length units. |
| `void` | `setX(double x)` | Sets the X coordinate of the robot |
| `void` | `setXYZ(Point point)` | Places the robot into the argument point location |
| `void` | `setY(double y)` | Sets the Y coordinate of the robot |
| `void` | `setZ(double z)` | Sets the Z coordinate of the robot |
| `double` | `timeInState(RobotState robotState)` | Returns time (in model time units) the robot spent in specified state since model start or since last `resetStats()` call |
| `double` | `timeInState(RobotState robotState, TimeUnits timeUnits)` | Returns time (in units) the robot spent in specified state since model start or since last `resetStats()` call |
| `void` | `uninstallEndEffector()` |  |
