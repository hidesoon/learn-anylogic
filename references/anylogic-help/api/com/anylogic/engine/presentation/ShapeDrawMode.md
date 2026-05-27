*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeDrawMode.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Enum Class ShapeDrawMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[ShapeDrawMode](ShapeDrawMode.md "enum class in com.anylogic.engine.presentation")>

com.anylogic.engine.presentation.ShapeDrawMode

All Implemented Interfaces:
:   `Serializable`, `Comparable<ShapeDrawMode>`, `Constable`

---

```
public enum ShapeDrawMode
extends Enum<ShapeDrawMode>
```

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getSVGString()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `has2D()` |  |
| `boolean` | `has3D()` |  |
| `abstract ShapeDrawMode` | `intersection(ShapeDrawMode drawMode)` |  |
| `boolean` | `intersects(ShapeDrawMode drawMode)` | Tests if a given draw mode has any intersection with this one, i.e. |
| `ShapeDrawMode` | `limitBy(ShapeDrawMode drawMode)` |  |
| `static ShapeDrawMode` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static ShapeDrawMode[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
