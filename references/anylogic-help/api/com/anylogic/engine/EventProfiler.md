*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/EventProfiler.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class EventProfiler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.EventProfiler

All Implemented Interfaces:
:   `Serializable`

---

```
public class EventProfiler
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.EventProfiler)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `EventProfiler.EventType` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `EventProfiler(IExperimentHost experimentHost)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `EventInfo` | `getEventInfo(int maxevents, boolean fullFrame)` | Creates and returns the information structure about the events scheduled and conditions monitored. |
| `EventItem[]` | `getEvents(int istart, int number)` |  |
| `EventItem[]` | `getPredicates(int istart, int number)` |  |
