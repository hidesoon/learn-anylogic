*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentExtension.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface AgentExtension

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `ExtAgentContinuous`, `ExtAgentDiscrete`, `ExtAgentGIS`, `ExtAgentInteractive`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtDefaultAnimationProvider`, `ExtEntity`, `ExtEnvironmentContinuous`, `ExtEnvironmentDiscrete`, `ExtEnvironmentGIS`, `ExtEnvironmentInteractive`, `ExtEnvironmentWithLayout`, `ExtEnvironmentWithMetrics`, `ExtRootModelAgent`, `ExtSpace`

All Known Implementing Classes:
:   `AgentExtensionImpl`, `ExtAgentContinuousDelegate`, `ExtAgentWithSpatialMetricsDelegate`, `ExtEntityContinuousDelegate`, `ExtEntityDelegate`

---

```
@AnyLogicInternalCodegenAPI
public interface AgentExtension
extends Serializable
```

Base interface for extensions of [`Agent`](Agent.md "class in com.anylogic.engine")s.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final int` | `P_AGENT_INTERACTIVE_DELEGATE` |  |
| `static final int` | `P_AGENT_WITH_SPATIAL_METRICS_DELEGATE` |  |
| `static final int` | `P_AGENT_WITH_SPECIFIC_SPACE` |  |
| `static final int` | `P_AGENT_WITH_SPECIFIC_SPACE_DELEGATE` |  |
| `static final int` | `P_ENTITY_DELEGATE` |  |
| `static final int` | `P_ENV_WITH_SPECIFIC_SPACE` |  |
| `static final int` | `P_ROOT` |  |
| `static final int` | `P_SPACE` |  |
| `static final int` | `P_USER_EXT` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Agent` | `getAgent()` | Returns the agent this extension belongs to |
| `AgentExtension` | `next_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `onDestroy()` | This method is called when the owner of this extension is destroyed.  Should be overridden when custom destroy is required.  Default implementation does nothing |
| `void` | `onExtensionRemoved(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Callback invoked when some other agent extension is removed. |
| `int` | `priority()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `void` | `setNext_xjal(AgentExtension next)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `boolean` | `supportsInterface_xjal(Class<?> itfs)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
