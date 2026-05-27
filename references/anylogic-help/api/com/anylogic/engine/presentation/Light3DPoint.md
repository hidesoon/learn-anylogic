*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3DPoint.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3DPoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Light3D](Light3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Light3DPoint

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Light3D.StreetLight`

---

```
public class Light3DPoint
extends Light3D
```

3D point light, may be added to 3D groups for scene lighting
Point source of light is located in one particular [`point`](#setPos(double,double,double)) of space.
It shines uniformly in all directions.
You can define [attenuation coefficients](#setAttenuation(double,double,double))
for this kind of source of light.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Light3D`](Light3D.md "class in com.anylogic.engine.presentation")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3DPoint)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Light3DPoint(boolean ispublic, double x, double y, double z, double constantAttenuation, double linearAttenuation, double quadraticAttenuation, Color diffuseColor, Color specularColor, Color ambientColor, boolean global)` | Creates new 3D point light |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Light3DPoint` | `clone()` | Creates and returns a copy of this light (i.e. |
| `float` | `getConstantAttenuation()` | Returns the constant [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `float` | `getLinearAttenuation()` | Returns the linear [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `float` | `getQuadraticAttenuation()` | Returns the quadratic [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `float` | `getX()` | Returns the x coordinate of the light source position |
| `float` | `getY()` | Returns the y coordinate of the light source position |
| `float` | `getZ()` | Returns the z coordinate of the light source position |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setAttenuation(double constantAttenuation, double linearAttenuation, double quadraticAttenuation)` | Sets the attenuation factors of the light fading with the distance.  Light attenuation is calculated using this factor (where `d` is a distance from the light source):  `attenuation factor = 1 / (kC + kLd + kQd2)`  If all of provided factors are set to zero, then the light isn't faded. |
| `void` | `setConstantAttenuation(double constantAttenuation)` | Sets the constant [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setLinearAttenuation(double linearAttenuation)` | Sets the linear [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setPos(double x, double y, double z)` | Sets the light source position |
| `void` | `setQuadraticAttenuation(double quadraticAttenuation)` | Sets the quadratic [attenuation factor](#setAttenuation(double,double,double)) of the light |
| `void` | `setX(double x)` | Sets the x coordinate of the light source position |
| `void` | `setY(double y)` | Sets the y coordinate of the light source position |
| `void` | `setZ(double z)` | Sets the z coordinate of the light source position |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
