*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3DSpot.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3DSpot

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Light3D](Light3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Light3DSpot

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Light3D.CarHeadlight`

---

```
public class Light3DSpot
extends Light3D
```

3D spot light, may be added to 3D groups for scene lighting
Spot source of light is a particular case of a [`point light`](Light3DPoint.md "class in com.anylogic.engine.presentation").
Spot source creates a beam of light that gradually becomes
wider and makes a cone of light (with [cut-off angle](#setCutOffAngle(double))
and [drop-off rate](#setDropOffRate(double))). You can think of a spot
source of light as a searchlight or a car headlight.
Lighting is performed along the given direction which is
specified using 2 angles: orientation around [X](#setAngleX(double))
and [Z](#setAngleZ(double)) axes.
You can define [attenuation coefficients](#setAttenuation(double,double,double))
for this kind of source of light.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Light3D`](Light3D.md "class in com.anylogic.engine.presentation")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3DSpot)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Light3DSpot(boolean ispublic, double x, double y, double z, double angleX, double angleZ, double cutOffAngle, double dropOffRate, double constantAttenuation, double linearAttenuation, double quadraticAttenuation, Color diffuseColor, Color specularColor, Color ambientColor, boolean global)` | Creates new 3D spot light |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Light3DSpot` | `clone()` | Creates and returns a copy of this light (i.e. |
| `float` | `getAngleX()` | Returns the orientation of the light around X axis (CW, from +Y to +Z).  Zero angle value corresponds to horizontal orientation of the light (parallel with XY-plane). |
| `float` | `getAngleZ()` | Returns the orientation of the light around Z axis (CW, from +X to +Y).  Zero angle value corresponds to orientation of the light towards -Y direction (to the North). |
| `float` | `getConstantAttenuation()` | Returns the constant [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `float` | `getCutOffAngle()` | Returns the cut-off angle of light source.  The angle is measured from the light direction axis to the light cut-off cone.  The angle lies in the range `[0, PI/2]` radians, where the angle of `PI/2` corresponds to the lighting of the half of the world's space. |
| `float` | `getDropOffRate()` | Returns the value of the exponent that is used to control how the light intensity drops off from the center to the cut off angle. |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `float` | `getLinearAttenuation()` | Returns the linear [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `float` | `getQuadraticAttenuation()` | Returns the quadratic [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `float` | `getX()` | Returns the x coordinate of the light source position |
| `float` | `getY()` | Returns the y coordinate of the light source position |
| `float` | `getZ()` | Returns the z coordinate of the light source position |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setAngleX(double angleX)` | Sets the orientation of the light around X axis (CW, from +Y to +Z).  Zero angle value corresponds to horizontal orientation of the light (parallel with XY-plane). |
| `void` | `setAngleZ(double angleZ)` | Sets the orientation of the light around Z axis (CW, from +X to +Y).  Zero angle value corresponds to orientation of the light towards -Y direction (to the North). |
| `void` | `setAttenuation(double constantAttenuation, double linearAttenuation, double quadraticAttenuation)` | Sets the attenuation factors of the light fading with the distance.  Light attenuation is calculated using this factor (where `d` is a distance from the light source):  `attenuation factor = 1 / (kC + kLd + kQd2)`  If all of provided factors are set to zero, then the light isn't faded. |
| `void` | `setConstantAttenuation(double constantAttenuation)` | Sets the constant [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setCutOffAngle(double cutOffAngle)` | Sets the cut-off angle of light source.  The angle is measured from the light direction axis to the light cut-off cone.  The angle must lie in the range `[0, PI/2]` radians, where the angle of `PI/2` corresponds to the lighting of the half of the world's space. |
| `void` | `setDropOffRate(double dropOffRate)` | Sets the value of the exponent that can be used to control how the light intensity drops off from the center to the cut off angle. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setLinearAttenuation(double linearAttenuation)` | Sets the linear [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setPos(double x, double y, double z)` | Sets the light source position |
| `void` | `setQuadraticAttenuation(double quadraticAttenuation)` | Sets the quadratic [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setX(double x)` | Sets the x coordinate of the light source position |
| `void` | `setY(double y)` | Sets the y coordinate of the light source position |
| `void` | `setZ(double z)` | Sets the z coordinate of the light source position |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
