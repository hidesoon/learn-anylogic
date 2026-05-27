*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentExtensionImpl.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AgentExtensionImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.AgentExtensionImpl

All Implemented Interfaces:
:   `AgentExtension`, `Serializable`

Direct Known Subclasses:
:   `ExtAgentContinuousDelegate`, `ExtAgentWithSpatialMetricsDelegate`

---

```
@AnyLogicInternalAPI
public abstract class AgentExtensionImpl
extends Object
implements AgentExtension, Serializable
```

Base class for extensions of [`Agent`](Agent.md "class in com.anylogic.engine")s.
Please note that agent, during its lifetime, may change instances
of some extensions (e.g. replace existing extension with its subclass),
so you shouldn't store references to extensions
anywhere. Please store references to [`agent`](#getAgent()) instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.AgentExtensionImpl)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentExtensionImpl(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `RuntimeException` | `error(String errorText)` |  |
| `RuntimeException` | `error(String errorTextFormat, Object... args)` |  |
| `Agent` | `getAgent()` | Returns the agent this extension belongs to |
| `static Set<Class<?>>` | `getSupportedInterfaces_xjal(Class<? extends AgentExtension> extClass)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final AgentExtension` | `next_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `onDestroy()` | This method is called when the owner of this extension is destroyed.  Should be overridden when custom destroy is required.  Default implementation does nothing |
| `void` | `onExtensionRemoved(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Default implementation does nothing |
| `int` | `priority()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `final void` | `setNext_xjal(AgentExtension next)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `boolean` | `supportsInterface_xjal(Class<?> itfs)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
