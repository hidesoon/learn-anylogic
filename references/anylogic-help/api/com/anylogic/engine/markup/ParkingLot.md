*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ParkingLot.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ParkingLot

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadPart](AbstractRoadPart.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadSidePart](AbstractRoadSidePart.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.ParkingLot

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasCenterPoint`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ParkingLot
extends AbstractRoadSidePart
implements HasCenterPoint
```

Class representing a set of parking spaces along border of a road segment. Parallel and perpendicular parking types are supported.
Parking lot belongs to some road segment. One road segment can contain several parking lots.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ParkingLot)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ParkingLot()` |  |
| `ParkingLot(Road road, ShapeDrawMode drawMode, boolean isPublic, boolean isOnForwardSide, double offset, ParkingLotType type, int parkingSpacesCount, double parkingSpaceWidthInMeters, double parkingSpaceLengthInMeters, int parkingAngle, boolean forceLeavingEnabled, double forceLeavingTimeoutInSeconds)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Agent` | `getCarOnSpace(int spaceIndex)` | Returns car located in the parking space with the given index, or `null` if this space is free |
| `List<Agent>` | `getCars()` | Returns ordered list of cars located on this parking lot. |
| `final Position` | `getCenter(Position out)` |  |
| `int` | `getDiagonalParkingAngle()` | Returns parking angle value. |
| `double` | `getForceLeavingTimeout()` | Returns the delay time after which cars leaving will be forced (i.e. |
| `double` | `getForceLeavingTimeout(TimeUnits units)` | Returns the delay time after which cars leaving will be forced (i.e. |
| `int[]` | `getFreeSpaceIndexes()` | Returns array of indexes of free parking spaces |
| `double` | `getLength()` |  |
| `int` | `getParkingSpaceIndex(Agent car)` | Returns the index of the parking space where the given car is located. |
| `double` | `getParkingSpaceLength()` | Returns the length of parking space |
| `double` | `getParkingSpaceLength(LengthUnits units)` | Returns the length of parking space |
| `double` | `getParkingSpaceWidth()` | Returns the width of parking space |
| `double` | `getParkingSpaceWidth(LengthUnits units)` | Returns the width of parking space |
| `ParkingLotType` | `getParkingType()` | Returns parking type of the parking lot, parallel or perpendicular (diagonal) |
| `boolean` | `isForceLeaving()` | Returns true if car will leave the parking lot forcibly after timeout (if specified) (i.e. |
| `int` | `nCars()` | Returns number of cars located on this parking lot |
| `int` | `nFree()` | Returns the number of free parking spaces in this parking lot |
| `int` | `nSpaces()` | Returns the total number of spaces in this parking lot |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `randomFreeSpaceIndex()` | Returns the index of randomly chosen free parking space |
| `void` | `setDataSource(ParkingLotDataSource dataSource)` |  |
| `void` | `setDiagonalParkingAngle(int diagonalParkingAngle)` | Sets diagonal angle of the parking lot spaces. |
| `void` | `setForceLeavingEnabled(boolean forceLeavingEnabled)` | Switches the forced parking leaving mode on or off according to the given value. |
| `void` | `setForceLeavingTimeout(double timeout)` | Sets the force parking leaving timeout value in model time units. |
| `void` | `setForceLeavingTimeout(double timeout, TimeUnits units)` | Sets the force parking leaving timeout value in specified time units. |
| `void` | `setNSpaces(int parkingSpacesCount)` | Sets number of parking spaces in parking lot. |
| `void` | `setParkingSpaceLength(double parkingSpaceLengthInPixels)` | Deprecated. this method is deprecated and may be removed in the next release. |
| `void` | `setParkingSpaceLength(double parkingSpaceLength, LengthUnits units)` | Sets the length of parking space |
| `void` | `setParkingSpaceWidth(double parkingSpaceWidthInPixels)` | Deprecated. this method is deprecated and may be removed in the next release. |
| `void` | `setParkingSpaceWidth(double parkingSpaceWidth, LengthUnits units)` | Sets the width of parking space |
| `void` | `setParkingType(ParkingLotType parkingType)` | Sets parking type of the parking lot. |
