*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/OverheadCraneMovementMode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Enum Class OverheadCraneMovementMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[OverheadCraneMovementMode](OverheadCraneMovementMode.md "enum class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.OverheadCraneMovementMode

All Implemented Interfaces:
:   `Serializable`, `Comparable<OverheadCraneMovementMode>`, `Constable`

---

```
public enum OverheadCraneMovementMode
extends Enum<OverheadCraneMovementMode>
```

Overhead crane's movement modes. Defines how the parts of the crane are moving in relation to each other.:   `OVERHEAD_CRANE_MOVEMENT_STEP_BY_STEP` - parts move separately, one after another

    `OVERHEAD_CRANE_MOVEMENT_CONCURRENT` - parts move concurrent

    `OVERHEAD_CRANE_MOVEMENT_INDEPENDENT_HOIST` - trolley and bridge move concurrent, but separately with hoist

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static OverheadCraneMovementMode` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static OverheadCraneMovementMode[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
