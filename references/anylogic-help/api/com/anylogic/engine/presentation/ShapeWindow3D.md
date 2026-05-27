*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeWindow3D.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeWindow3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeWindow3D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeWindow3D
extends ShapeControl
```

The window showing 3D world on the model animation.
This is a shape like any control which is located on the model animation
canvas. It draws the 3D scene from the field of view of selected
[camera](Camera3D.md "class in com.anylogic.engine.presentation").
3D window has custom context popup menu with additional items:

* "Copy camera" - copies current view as camera setting to be pasted in the
  AnyLogic (at design-time) in the "General" properties page of any 3D camera
  of the model.
* "Camera" submenu - allows navigation to any camera defined on the current
  agent.

Window may be locked with the camera - in this case the point of window follows
the camera changes.
Window has several navigation modes:

* [`NAVIGATION_FULL`](#NAVIGATION_FULL) - works only when the window isn't linked with
  camera
* [`NAVIGATION_LIMITED_TO_Z_ABOVE_ZERO`](#NAVIGATION_LIMITED_TO_Z_ABOVE_ZERO) - works only when the window
  isn't linked with camera
* [`NAVIGATION_ROTATION_ONLY`](#NAVIGATION_ROTATION_ONLY)
* [`NAVIGATION_NONE`](#NAVIGATION_NONE)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeWindow3D)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Navigation3DType` | `NAVIGATION_FULL` | Navigation is fully allowed |
| `static final Navigation3DType` | `NAVIGATION_LIMITED_TO_Z_ABOVE_ZERO` | Navigation is only allowed above Z=0 plane |
| `static final Navigation3DType` | `NAVIGATION_NONE` | Navigation is prohibited.  Default when window is linked with camera. |
| `static final Navigation3DType` | `NAVIGATION_ROTATION_ONLY` | Navigation mode where user is able to rotate view only.  Can be used when window is linked with camera. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeWindow3D(Presentable p, boolean ispublic, double x, double y, double width, double height, Navigation3DType navigationMode, double farClippingDistance)` | Creates a (persistent) 3d scene window control. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Camera3D` | `createCamera()` | Returns new instance of [`Camera3D`](Camera3D.md "class in com.anylogic.engine.presentation") having the most recent camera parameters set in setCamera functions.  Due to technical reasons, this function doesn't reflect current position of the animation GUI navigation. |
| `void` | `executeAction()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getFarClippingDistance()` | Returns the "far-clipping" distance, which controls how much of the scene is shown (how far in depth is it visible) |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `setCamera(Camera3D camera)` | Sets the 3D Window to the given camera (and doesn't follow the camera) |
| `void` | `setCamera(Camera3D camera, boolean follow)` | Sets the 3D Window to the given camera and optionally starts following it. |
| `void` | `setCamera(Camera3D camera, boolean follow, long transitionTimeout)` | Sets the 3D Window to the given camera and optionally starts following it. |
| `void` | `setNavigationMode(Navigation3DType mode)` | Sets the navigation mode (the freedom level of camera manipulation using mouse). |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
