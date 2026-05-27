*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAnimationParams.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtAnimationParams

All Superinterfaces:
:   `AgentExtension`, `Serializable`

All Known Subinterfaces:
:   `ExtAgentContinuous`, `ExtAgentDiscrete`, `ExtAgentGIS`, `ExtAgentWithSpatialMetrics`, `ExtEntity`

All Known Implementing Classes:
:   `ExtAgentContinuousDelegate`, `ExtAgentWithSpatialMetricsDelegate`, `ExtEntityContinuousDelegate`, `ExtEntityDelegate`

---

```
@AnyLogicInternalAPI
public interface ExtAnimationParams
extends AgentExtension
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `getAnimationPosition(Position out)` | ... |
| `double` | `getAnimationX()` |  |
| `double` | `getAnimationY()` |  |
| `double` | `getAnimationZ()` |  |
| `double` | `getPresentationScaleOnOwnerSpace()` | Returns the scale of the agent presentation animation on its space or `1.0` if space isn't defined or agent list is empty |
| `Agent` | `getSpace()` | Returns the agent representing space this agent lives in |
| `boolean` | `isAnimationVisible_xjal()` |  |
| `void` | `setSpace(Agent space)` | Sets the space for agent. |
