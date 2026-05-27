*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3D.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.Light3D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`

---

```
public abstract class Light3D
extends Object
implements UsdElement, SVGElement
```

Base class for all 3D lights, may be added to 3D groups for scene lighting

The light consists of a number of different components: Ambient, Diffuse and
Specular.

* *Ambient light* is a light that had scattered for many times, so that it
  does not have any certain direction. Ambient light does not die out and is
  uniformly distributed all over the space.
* *Diffuse light* shines in a particular direction but is reflected
  homogenously from each point of the surface (for example, fluorescent
  lights).
* *Specular light* is a light that reflects off a smooth shiny surface.

The intensity and color of each component is defined in terms of general [`Color`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html "class or interface in java.awt") object.
For example, [Black](ColorConstants.md#BLACK) means "No light",
[White](ColorConstants.md#WHITE) - white light with maximum intensity,
[Red](ColorConstants.md#RED) - red light with maximum intensity (e.g. green shape will be invisible under this light),
[Dark Red](ColorConstants.md#DARK_RED) - red light with low intensity.
Each component is applied to the corresponding color part of shape's texture (if shape
has texture) or the general shape's color (if shape has only [`Color`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html "class or interface in java.awt")).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`ShapeGroup.add(Light3D)`](ShapeGroup.md#add(com.anylogic.engine.presentation.Light3D))[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3D)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `Light3D.CarHeadlight` |  |
| `static class` | `Light3D.Daylight` |  |
| `static class` | `Light3D.Moonlight` |  |
| `static class` | `Light3D.StreetLight` |  |

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Light3D` | `clone()` | Creates and returns a copy of this light (i.e. |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Color` | `getAmbientColor()` | Returns the [ambient color component](#lightColors) |
| `Color` | `getDiffuseColor()` | Returns the [diffuse color component](#lightColors) |
| `ShapeGroup` | `getGroup()` | Returns the group containing this light. |
| `Shape` | `getGroupOrOwner()` |  |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `String` | `getName()` | If the light is declared as field in a presentable object class ([`Agent`](../Agent.md "class in com.anylogic.engine")), e.g. |
| `long` | `getOrGenerateUSDId()` |  |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this light belongs to, or `null`. |
| `Color` | `getSpecularColor()` | Returns the [specular color component](#lightColors) |
| `long` | `getSVGId()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isEnabled()` | Returns `true` if this light is turned on. |
| `boolean` | `isGlobal()` | Returns `true` if this light affects shapes outside the parent group of this light |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setAmbientColor(Color ambientColor)` | Sets the [ambient color component](#lightColors) |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setDiffuseColor(Color diffuseColor)` | Sets the [diffuse color component](#lightColors) |
| `void` | `setEnabled(boolean enabled)` | Enables or disables this light |
| `void` | `setGlobal(boolean global)` | Sets whether this light should affect shapes outside the parent group of this light |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setSpecularColor(Color specularColor)` | Sets the [specular color component](#lightColors) |
| `void` | `update()` | User extension point for dynamic properties update code |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> commands, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
