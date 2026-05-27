*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentWithLayout.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentWithLayout

All Superinterfaces:
:   `AgentExtension`, `ExtEnvironmentInteractive`, `Serializable`

All Known Subinterfaces:
:   `ExtEnvironmentContinuous`, `ExtEnvironmentDiscrete`

---

```
public interface ExtEnvironmentWithLayout
extends ExtEnvironmentInteractive
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `applyLayout()` | Rearranges agents in this space according to the selected layout type. |
| `LayoutType` | `getLayoutType()` | Returns the layout type. |
| `void` | `setLayoutType(LayoutType type)` | Sets the layout type. |
