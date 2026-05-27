*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Camera3D.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Camera3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.Camera3D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `Serializable`, `Cloneable`

---

```
public class Camera3D
extends Object
```

3D camera object. Used in [3D windows](ShapeWindow3D.md "class in com.anylogic.engine.presentation").
Has location and view direction.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Camera3D)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Camera3D()` | This constructor calls [`update()`](#update()) and should be used in the cameras changing at a model run-time |
| `Camera3D(double x, double y, double z, double rotationX, double rotationZ)` |  |
| `Camera3D(Camera3D c)` | Creates a copy of the given camera |
| `Camera3D(ShapeGroup group, double x, double y, double z, double rotationX, double rotationZ)` | Creates new camera object |
| `Camera3D(ShapeGroup group, String name, double x, double y, double z, double rotationX, double rotationZ)` | Creates new camera object |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Camera3D` | `clone()` |  |
| `void` | `copyToClipboard()` | Copies camera settings to the system clipboard in the format supported by AnyLogic IDE.  To paste the camera setting in the AnyLogic, please select the camera object, open "General" page of its Property View and press the button with clipboard icon ("Paste") located in the properties page. |
| `boolean` | `equals(Object obj)` | Returns `true` if the given obj is 3D camera with the same location/rotation parameters. |
| `String` | `getCameraPostionAttributeValue()` |  |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `Presentable` | `getPresentable()` |  |
| `double` | `getRotationX()` | Returns the rotation of the camera around X axis (CW, from +Y to +Z).  Zero rotation value corresponds to horizontal orientation of the camera (parallel with XY-plane). |
| `double` | `getRotationZ()` | Returns the rotation of the camera in radians around Z axis (CW from +X to +Y) |
| `long` | `getSVGId()` |  |
| `double` | `getX()` | Returns the x coordinate of the camera location |
| `double` | `getY()` | Returns the y coordinate of the camera location |
| `double` | `getZ()` | Returns the z coordinate of the camera location |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` |  |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setPos(double x, double y, double z)` | Sets the camera location |
| `void` | `setRotationX(double rotationX)` | Sets the rotation of the camera around X axis (CW, from +Y to +Z).  Zero rotation value corresponds to horizontal orientation of the camera (parallel with XY-plane). |
| `void` | `setRotationZ(double rotationZ)` | Sets the rotation of the camera in radians around Z axis (CW from +X to +Y) |
| `void` | `setX(double x)` | Sets the x coordinate of the camera location |
| `void` | `setY(double y)` | Sets the y coordinate of the camera location |
| `void` | `setZ(double z)` | Sets the z coordinate of the camera location |
| `String` | `toString()` |  |
| `void` | `update()` | User extension point for cameras changing at a model run-time  This callback method should be overridden to set up-to-date values of camera properties using methods [`setX(double)`](#setX(double)), [`setY(double)`](#setY(double)) etc.  Default implementation does nothing |
| `void` | `update(double x, double y, double z, double rotationX, double rotationZ)` |  |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind)` |  |
