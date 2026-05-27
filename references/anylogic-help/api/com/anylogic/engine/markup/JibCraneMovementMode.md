*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/JibCraneMovementMode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Enum Class JibCraneMovementMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[JibCraneMovementMode](JibCraneMovementMode.md "enum class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.JibCraneMovementMode

All Implemented Interfaces:
:   `Serializable`, `Comparable<JibCraneMovementMode>`, `Constable`

---

```
public enum JibCraneMovementMode
extends Enum<JibCraneMovementMode>
```

Jib crane's movement modes. Defines how the parts of the crane are moving in relation to each other.:   `JIB_CRANE_MOVEMENT_STEP_BY_STEP` - parts move separately, one after another

    `JIB_CRANE_MOVEMENT_CONCURRENT` - parts move concurrent

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static JibCraneMovementMode` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static JibCraneMovementMode[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
