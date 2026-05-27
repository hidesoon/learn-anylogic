*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtDefaultAnimationProvider.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtDefaultAnimationProvider

All Superinterfaces:
:   `AgentExtension`, `Serializable`

All Known Subinterfaces:
:   `ExtEntity`

All Known Implementing Classes:
:   `ExtEntityContinuousDelegate`, `ExtEntityDelegate`

---

```
@AnyLogicInternalAPI
public interface ExtDefaultAnimationProvider
extends AgentExtension
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeTopLevelPresentationGroup` | `createDefaultAnimation()` |  |
| `ShapeTopLevelPresentationGroup` | `getDefaultAnimation()` |  |
| `boolean` | `onClick()` | Should be overridden to define the reaction on mouse click. |
