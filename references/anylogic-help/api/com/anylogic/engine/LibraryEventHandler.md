*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LibraryEventHandler.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class LibraryEventHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.LibraryEventHandler

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class LibraryEventHandler
extends Object
implements Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.LibraryEventHandler)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `LibraryEventHandler.Event` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LibraryEventHandler(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addEvent(double dt, LibraryEventHandler.Event event)` |  |
| `LibraryEventHandler.Event` | `addEvent(double dt, Runnable runnable)` |  |
| `void` | `removeEvent(LibraryEventHandler.Event event)` |  |
