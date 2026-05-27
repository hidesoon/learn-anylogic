*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Slope.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Slope

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.Slope

All Implemented Interfaces:
:   `Serializable`

---

```
public class Slope
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Slope)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Slope(double x, double y, double horizontalAngle, double verticalAngle)` | Constructs a slope with specific attributes. |
| `Slope(double x, double y, double dx, double dy, double dz)` | Constructs a slope with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDx()` | Returns the x-offset of the end line point relative to the start one (the difference of x coordinates of the line end and start points). |
| `double` | `getDy()` | Returns the y-offset of the end line point relative to the start one (the difference of x coordinates of the line end and start points). |
| `double` | `getDz()` | Returns the z-offset of the end line point relative to the start one (the difference of x coordinates of the line end and start points). |
| `double` | `getHorizontalAngle()` | Returns the horizontal angle, it terms of radian |
| `SlopeType` | `getType()` | Returns slope type |
| `double` | `getVerticalAngle()` | Returns the vertical angle, it terms of radian |
| `double` | `getX()` | Returns the x coordinate of the start line point |
| `double` | `getY()` | Returns the y coordinate of the start line point |
