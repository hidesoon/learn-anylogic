*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Position.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Position

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Point](Point.md "class in com.anylogic.engine")

com.anylogic.engine.Position

All Implemented Interfaces:
:   `Locatable2D`, `Serializable`, `Cloneable`

---

```
public class Position
extends Point
```

Class representing Point structure three coordinates (x, y, z) with two
angles for orientation. Used in various utility methods in the AnyLogic
Engine and in some AnyLogic libraries.
For those utilities which operate in 2D space (x, y), the third (z)
coordinate and vertical rotation are simply ignored

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Position)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `double` | `rotation` | The (horizontal) orientation, measured CW from right (east) |
| `double` | `verticalRotation` | The vertical orientation, measured from horizontal-oriented (0) to the ground: "-Z" direction (ground) is positive, "+Z" direction (sky) is negative |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Position()` | Creates new position with zero (0, 0, 0) coordinates and zero rotation angles (default orientation: horizontally to the right/east) |
| `Position(double x, double y, double rotation)` | Creates new point with the given (x, y) coordinates and rotation. |
| `Position(double x, double y, double z, double rotation, double verticalRotation)` | Creates new position with the given coordinates and rotations. |
| `Position(Point p)` | Creates a position with the given coordinates. |
| `Position(Point p, double rotation, double verticalRotation)` |  |
| `Position(Position p)` | Creates a copy of the given position |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `clone()` |  |
| `Position` | `clone(Position out)` | Fills the given `output` instance (if it is not `null`) or otherwise creates a copy of this object and returns it |
| `double` | `getRotation()` | Returns the horizontal orientation |
| `double` | `getVerticalRotation()` | Returns the vertical orientation |
| `Position` | `setLocation(Position p)` | Sets the location and rotations of this Position to the same values as in the given Position object. |
| `Position` | `setPosition(double x, double y, double z, double rotation, double verticalRotation)` | Sets the location and rotations of this Position to the given coordinates and rotations. |
| `void` | `setRotation(double rotation)` | Sets the horizontal orientation |
| `void` | `setVerticalRotation(double verticalRotation)` | Sets the vertical orientation |
| `String` | `toString()` |  |
