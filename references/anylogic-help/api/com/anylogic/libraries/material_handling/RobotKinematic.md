*来源 (Source): <https://anylogic.help/api/com/anylogic/libraries/material_handling/RobotKinematic.html>*

---

Package [com.anylogic.libraries.material\_handling](package-summary.md)

# Class RobotKinematic

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.libraries.material\_handling.RobotKinematic

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class RobotKinematic
extends Object
implements Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.libraries.material_handling.RobotKinematic)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RobotKinematic(double... linkLengths)` |  |
| `RobotKinematic(RobotKinematic kinematic)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getEndEffectorLength()` |  |
| `double[]` | `getRotations(int linkIndex)` | Returns rotations of linkIndex link in absolute coordinates. |
| `double[]` | `getXYZ(int linkIndex)` | Returns coordinates of linkIndex link in absolute coordinates. |
| `void` | `setEndEffectorLength(double length)` |  |
| `void` | `setToPoint(Point target, Point direction)` | Sets end point of the kinematic to provided point with direction along the direction vector If provided target/direction is unreachable, kinematic will enter invalid state (isIncalid() will return true) |
