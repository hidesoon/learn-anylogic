*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Light3D.StreetLight.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Light3D.StreetLight

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Light3D](Light3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Light3DPoint](Light3DPoint.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Light3D.StreetLight

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Enclosing class:
:   [Light3D](Light3D.md "class in com.anylogic.engine.presentation")

---

```
public static class Light3D.StreetLight
extends Light3DPoint
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Light3D.StreetLight)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StreetLight(double x, double y, double z)` |  |
| `StreetLight(Color baseColor, double x, double y, double z, boolean ispublic, boolean global)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
