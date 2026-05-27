*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Point.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Point

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Point

All Implemented Interfaces:
:   `Locatable2D`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Position`

---

```
public class Point
extends Object
implements Serializable, Cloneable, Locatable2D
```

Class representing Point structure: three coordinates (x, y, z).
Used in various utility methods in the AnyLogic Engine and in some AnyLogic libraries.
For those utilities which operate in 2D space (x, y), the third (z) coordinate is simply ignored

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Point)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `double` | `x` | The x coordinate of this Point. |
| `double` | `y` | The y coordinate of this Point. |
| `double` | `z` | The z coordinate of this Point. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Point()` | Creates new point with zero (0, 0, 0) coordinates |
| `Point(double x, double y)` | Creates new point with the given (x, y) coordinates. |
| `Point(double x, double y, double z)` | Creates new point with the given coordinates. |
| `Point(Point p)` | Creates a copy of the given point |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Point` | `add(Point p)` | Adds `p` to this point: moves this point by the offset specified by the given point `p`. |
| `Point` | `clone()` |  |
| `Point` | `clone(Point out)` | Fills the given `output` instance (if it is not `null`) or otherwise creates a copy of this object and returns it |
| `double` | `distance(double px, double py)` | Returns the distance from this Point to the specified point. |
| `double` | `distance(double px, double py, double pz)` | Returns the distance from this Point to the specified point. |
| `double` | `distance(Point p)` | Returns the distance from this Point to the specified Point. |
| `double` | `distance2D(Point p)` | Returns the distance from this Point to the specified Point. |
| `double` | `distanceGIS(double lat, double lon)` | Returns the distance from this Point to the specified (lat, lon) on GIS surface. |
| `double` | `distanceGIS(double lat, double lon, LengthUnits units)` | Returns the distance from this Point to the specified (lat, lon) on GIS surface. |
| `double` | `distanceGIS(Point p)` | Returns the distance from this Point to the specified Point on GIS surface. |
| `double` | `distanceGIS(Point p, LengthUnits units)` | Returns the distance from this Point to the specified Point on GIS surface. |
| `double` | `distanceSq(double px, double py)` | Returns the square of the distance from this Point to the specified point. |
| `double` | `distanceSq(double px, double py, double pz)` | Returns the square of the distance from this Point to the specified point.  This method is useful for comparing different distances, finding nearest point etc. |
| `double` | `distanceSq(Point p)` | Returns the square of the distance from this Point to the specified Point.  This method is useful for comparing different distances, finding nearest point etc. |
| `double` | `distanceSq2D(Point p)` | Returns the square of the distance from this Point to the specified Point. |
| `boolean` | `equals(Point p, double relativeError)` | Returns `true` if this point has the same coordinates as in the given point, within the given relative error. |
| `boolean` | `equals(Object obj)` | Returns `true` if the given object is [`Point`](Point.md "class in com.anylogic.engine") and it has exactly the same coordinates as in this Point. |
| `boolean` | `equals2D(Point p, double relativeError)` | Returns `true` if this point has the same (x, y) coordinates (z is ignored) as in the given point, within the given relative error. |
| `double` | `getLatitude()` | Returns the latitude of this Point |
| `double` | `getLongitude()` | Returns the longitude if this Point |
| `double` | `getX()` | Returns the x coordinate of this Point |
| `double` | `getY()` | Returns the y coordinate of this Point |
| `double` | `getZ()` | Returns the z coordinate of this Point |
| `int` | `hashCode()` |  |
| `Point` | `setLatLon(double lat, double lon)` | Set latitude and longitude of this Point |
| `Point` | `setLocation(double x, double y)` | Sets the location of this Point to the given coordinates. |
| `Point` | `setLocation(double x, double y, double z)` | Sets the location of this Point to the given coordinates. |
| `Point` | `setLocation(Point p)` | Sets the location of this Point to the same coordinates as in the given Point object. |
| `Point` | `sub(Point p)` | Subtracts `p` from this point: moves this point by the negative offset specified by the given point `p`. |
| `String` | `toString()` |  |
