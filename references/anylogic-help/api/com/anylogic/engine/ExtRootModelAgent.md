*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtRootModelAgent.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtRootModelAgent

All Superinterfaces:
:   `AgentExtension`, `Serializable`

---

```
public interface ExtRootModelAgent
extends AgentExtension
```

This extension may be defined only in the top-level agent of the model.
It owns 'default population' which e.g. takes agents created dynamically in flowcharts.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDestroyListener(AgentDestroyListener listener)` | Adds listener for top-level agent destroy. |
| `<T> T` | `getCustomObject(Object requestor)` | Returns custom object previously set by [`setCustomObject(Object, Object)`](#setCustomObject(java.lang.Object,T)) |
| `default <T> T` | `getCustomObject(Object requestor, Supplier<T> initializer)` | Returns custom object previously set by [`setCustomObject(Object, Object)`](#setCustomObject(java.lang.Object,T)) or creates a new one using the given `initializer` |
| `AgentList<Agent>` | `getDefaultPopulation()` | Returns 'default population' which e.g. |
| `void` | `removeDestroyListener(AgentDestroyListener listener)` | Adds listener for top-level agent destroy |
| `<T> T` | `setCustomObject(Object requestor, T object)` | Registers some custom object for the given `requestor` Throws error if `requestor` is `null` |
