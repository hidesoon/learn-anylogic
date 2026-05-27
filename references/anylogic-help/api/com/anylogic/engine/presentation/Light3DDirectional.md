*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3DDirectional.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3DDirectional

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Light3D](Light3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Light3DDirectional

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class Light3DDirectional
extends Light3D
```

3D directional light, may be added to 3D groups for scene lighting
Directional source of light is located in some infinitely distant point.
It shines in the specified direction.
You can think of a directional source of light as the Sun.
Lighting is performed along the given direction which is
specified using 2 angles: orientation around [X](#setAngleX(double))
and [Z](#setAngleZ(double)) axes.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Light3D`](Light3D.md "class in com.anylogic.engine.presentation")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3DDirectional)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Light3DDirectional(boolean ispublic, double angleX, double angleZ, Color diffuseColor, Color specularColor, Color ambientColor, boolean global)` | Creates new 3D directional light |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Light3DDirectional` | `clone()` | Creates and returns a copy of this light (i.e. |
| `float` | `getAngleX()` | Returns the orientation of the light around X axis (CW, from +Y to +Z).  Zero angle value corresponds to horizontal orientation of the light (parallel with XY-plane). |
| `float` | `getAngleZ()` | Returns the orientation of the light around Z axis (CW, from +X to +Y).  Zero angle value corresponds to orientation of the light towards -Y direction (to the North). |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setAngleX(double angleX)` | Sets the orientation of the light around X axis (CW, from +Y to +Z).  Zero angle value corresponds to horizontal orientation of the light (parallel with XY-plane). |
| `void` | `setAngleZ(double angleZ)` | Sets the orientation of the light around Z axis (CW, from +X to +Y).  Zero angle value corresponds to orientation of the light towards -Y direction (to the North). |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
