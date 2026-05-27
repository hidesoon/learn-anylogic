*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentExtensionFactory.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AgentExtensionFactory<T extends AgentExtension>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.AgentExtensionFactory<T>

---

```
public abstract class AgentExtensionFactory<T extends AgentExtension>
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentExtensionFactory()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract T` | `create(Agent owner)` | This method should create an extension for the given agent.  If designed, this method may perform check for compatibility with existing agent extensions and may throw error (e.g. |
| `static <T extends AgentExtension> AgentExtensionFactory<? extends T>` | `get(Class<T> c)` |  |
| `static <T extends AgentExtension> void` | `register(Class<T> c, AgentExtensionFactory<? extends T> factory)` | Registers new extension factory. |
