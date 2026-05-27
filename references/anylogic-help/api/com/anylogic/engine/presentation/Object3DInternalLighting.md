*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Object3DInternalLighting.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Enum Class Object3DInternalLighting

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[Object3DInternalLighting](Object3DInternalLighting.md "enum class in com.anylogic.engine.presentation")>

com.anylogic.engine.presentation.Object3DInternalLighting

All Implemented Interfaces:
:   `Serializable`, `Comparable<Object3DInternalLighting>`, `Constable`

---

```
public enum Object3DInternalLighting
extends Enum<Object3DInternalLighting>
```

This enum defines how the internal lights located inside [`Shape3DObject`](Shape3DObject.md "class in com.anylogic.engine.presentation") will operate on the scene:
[turned off](#OBJECT_3D_INTERNAL_LIGHTING_OFF),
[lighting this 3D object only](#OBJECT_3D_INTERNAL_LIGHTING_INSIDE) (self lighting), or
[lighting on the global level](#OBJECT_3D_INTERNAL_LIGHTING_GLOBAL) (like headlamp of the car).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static Object3DInternalLighting` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static Object3DInternalLighting[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
