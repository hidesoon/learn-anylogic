*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3DAmbient.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3DAmbient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Light3D](Light3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Light3DAmbient

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Light3D.Daylight`, `Light3D.Moonlight`

---

```
public class Light3DAmbient
extends Light3D
```

3D ambient light, may be added to 3D groups for scene lighting
Ambient light is a light that had scattered for many times, so that it
does not have any certain direction. Ambient light does not die out and is
uniformly distributed all over the space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Light3D`](Light3D.md "class in com.anylogic.engine.presentation")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3DAmbient)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Light3DAmbient(boolean ispublic, Color diffuseColor, Color specularColor, Color ambientColor, boolean global)` | Creates new 3D ambient light |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Light3DAmbient` | `clone()` | Creates and returns a copy of this light (i.e. |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
