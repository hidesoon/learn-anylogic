*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentContinuous.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentContinuous

All Superinterfaces:
:   `AgentExtension`, `ExtEnvironmentInteractive`, `ExtEnvironmentWithLayout`, `ExtEnvironmentWithMetrics`, `ExtWithSpaceType`, `Serializable`

---

```
public interface ExtEnvironmentContinuous
extends ExtEnvironmentInteractive, ExtEnvironmentWithMetrics, ExtEnvironmentWithLayout, ExtWithSpaceType
```

Agent environment extension for continuous (3D) space

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Point` | `randomPointOfSpace()` | Returns the random location inside within the space bounds of this environment |
| `void` | `setupSpace(double width, double height)` | Sets the space to the given dimensions. |
| `void` | `setupSpace(double width, double height, double zHeight)` | Sets the space to the given dimensions. |
| `double` | `spaceHeight()` | Returns the height of environment space. |
| `double` | `spaceWidth()` | Returns the width of environment space. |
| `double` | `spaceZHeight()` | Returns the height of environment space along Z-axis. |
