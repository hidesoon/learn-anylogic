*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IRunValueAccessor.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IRunValueAccessor

---

```
@AnyLogicInternalAPI
public interface IRunValueAccessor
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default <T> Optional<T>` | `getValue(IRunValueDescriptor<T> d)` |  |
| `<T> Optional<T>` | `getValue(String name, Class<T> type, IUnits<?> units)` |  |
