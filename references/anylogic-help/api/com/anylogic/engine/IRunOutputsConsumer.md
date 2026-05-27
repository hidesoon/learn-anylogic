*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IRunOutputsConsumer.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IRunOutputsConsumer

---

```
@AnyLogicInternalAPI
public interface IRunOutputsConsumer
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `storeOutput(String name, Class<?> type, IUnits<?> units, Object value)` |  |
| `default void` | `storeOutput(String name, Class<?> type, Object value)` |  |
| `default void` | `storeOutput(String name, Object value)` |  |
