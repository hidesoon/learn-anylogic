*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/EscalatorGroup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class EscalatorGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.EscalatorGroup

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class EscalatorGroup
extends AbstractLevelMarkup
implements HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.EscalatorGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `EscalatorGroup()` |  |
| `EscalatorGroup(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Level upperLevel, double x, double y, double z, double width, double length, double speedInMPS, double stepWidthInMeter, double angle, double rotation, double lowerLandingLength, double upperLandingLength, double rightBalustradeWidth, double leftBalustradeWidth, double internalBalustradeWidth, Color balustradecolor, boolean solidBalustrade, EscalatorPedestrianBehavior pedestrianBehaviorUp, EscalatorPedestrianBehavior pedestrianBehaviorDown, Escalator... escalators)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addEscalator(Escalator escalator)` | Adds an Escalator element to this escalator group. |
| `void` | `block()` | Blocks all escalators in this group. |
| `void` | `block(int index)` | Blocks the escalator with the specified index. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getAngle()` | Returns the angle of inclination of an escalator to the horizontal floor level (typically is 30 degrees). |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `List<Escalator>` | `getEscalators()` | Returns the list of escalators in this group. |
| `double` | `getInternalBalustradeWidth()` | Returns the width of the internal balustrade (in pixels) |
| `double` | `getLeftBalustradeWidth()` | Returns the width of the left balustrade (in pixels) |
| `double` | `getLength()` | Returns escalator length in pixels |
| `double` | `getLowerLandingLength()` | Returns the length of the lower landing |
| `Level` | `getLowerLevel()` | Returns the lower level. |
| `EscalatorMovementDirection` | `getMovementDirection(int index)` | Returns the current movement direction for the escalator specified by index. |
| `EscalatorPedestrianBehavior` | `getPedestrianBehaviorDown()` | Returns the behavior for pedestrians moving down in this escalator group. |
| `EscalatorPedestrianBehavior` | `getPedestrianBehaviorUp()` | Returns the behavior for pedestrians moving up in this escalator group. |
| `double` | `getRightBalustradeWidth()` | Returns the width of the right balustrade (in pixels) |
| `double` | `getRotation()` | Returns the current rotation angle (in radians) |
| `double` | `getSpeed(int index)` | Returns the speed of the specified escalator (in meters per second). |
| `double` | `getSpeed(int index, SpeedUnits units)` | Returns the speed of the escalator (in the units passed via the units argument) with the specified index. |
| `double` | `getStepWidth()` | Returns the step width (a.k.a. |
| `double` | `getStepWidth(LengthUnits units)` | Returns the step width (a.k.a. |
| `double` | `getUpperLandingLength()` | Returns the length of the upper landing |
| `Level` | `getUpperLevel()` | Returns the upper level. |
| `double` | `getWidth()` | Returns escalator width in pixels |
| `double` | `getX()` | Returns the X coordinate of this element |
| `double` | `getY()` | Returns the Y coordinate of this element |
| `double` | `getZ()` | Returns the Z coordinate of this element |
| `boolean` | `isBlocked(int index)` | Checks whether the escalator with the specified index is blocked, or not. |
| `boolean` | `isRunning(int index)` | Checks whether the escalator with the specified index is running, or not. |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setAngle(double angle)` | Sets the angle of inclination of an escalator to the horizontal floor level. |
| `void` | `setInternalBalustradeLength(double internalBalustradeWidth)` | Sets the width of the internal balustrade (in pixels). |
| `void` | `setLeftBalustradeWidth(double leftBalustradeWidth)` | Sets the width of the left balustrade (in pixels). |
| `void` | `setLength(double length)` | Sets the escalator length (in pixels). |
| `void` | `setLowerLandingLength(double lowerLandingLength)` | Sets the length of the lower landing. |
| `void` | `setLowerLevel(Level level)` | Sets the lower level. |
| `void` | `setMovementDirection(int index, EscalatorMovementDirection movementDirection)` | Sets new movement direction for the specified escalator. |
| `void` | `setMovementDirection(EscalatorMovementDirection movementDirection)` | Sets new movement direction for all the escalators in this group. |
| `void` | `setPedestrianBehaviorDown(EscalatorPedestrianBehavior pedestrianBehaviorDown)` | Sets the behavior for pedestrians moving down in this escalator group. |
| `void` | `setPedestrianBehaviorUp(EscalatorPedestrianBehavior pedestrianBehaviorUp)` | Sets the behavior for pedestrians moving up in this escalator group. |
| `void` | `setRightBalustradeLength(double rightBalustradeWidth)` | Sets the width of the right balustrade (in pixels). |
| `void` | `setRotation(double rotation)` | Sets the current rotation |
| `void` | `setSpeed(double speedInMPS)` | Sets the speed (in meters per second) of all the escalators in this group. |
| `void` | `setSpeed(double speed, SpeedUnits units)` | Sets the speed (in meters per second) of the escalator with the specified index. |
| `void` | `setSpeed(int index, double speedInMPS)` | Sets the speed (in meters per second) of the escalator with the specified index. |
| `void` | `setSpeed(int index, double speed, SpeedUnits units)` | Sets the speed (in the units passed via the units argument) of the escalator with the specified index. |
| `void` | `setStepWidth(double stepWidthInMeter)` | Sets the step width (a.k.a. |
| `void` | `setStepWidth(double stepWidth, LengthUnits units)` | Sets the step width (a.k.a. |
| `void` | `setUpperLandingLength(double upperLandingLength)` | Sets the length of the upper landing. |
| `void` | `setUpperLevel(Level level)` | Sets upper level. |
| `void` | `setUpperNewelLength(double upperLandingLength)` | Deprecated. will be removed in future releases |
| `void` | `setWidth(double width)` | Sets the escalator width (in pixels). |
| `void` | `setX(double x)` | Sets the X coordinate of this element. |
| `void` | `setY(double y)` | Sets the Y coordinate of this element. |
| `void` | `setZ(double z)` | Sets the Z coordinate of this element. |
| `void` | `turnOff()` | Turns off all escalators in this group. |
| `void` | `turnOff(int index)` | Turns off the escalator with the specified index. |
| `void` | `turnOn()` | Turns on all escalators in this group. |
| `void` | `turnOn(int index)` | Turns on the escalator with the specified index. |
| `void` | `unblock()` | Unblocks all escalators in this group, allowing pedestrians to enter the escalators. |
| `void` | `unblock(int index)` | Unblocks the escalator with the specified index. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `double` | `walkingPercentageDown()` | Override this function to return probability of choice to walk or stay. |
| `double` | `walkingPercentageUp()` | Override this function to return probability of choice to walk or stay. |
