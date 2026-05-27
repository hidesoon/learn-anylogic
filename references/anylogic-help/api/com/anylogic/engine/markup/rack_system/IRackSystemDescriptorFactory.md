*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/rack_system/IRackSystemDescriptorFactory.html>*

---

Package [com.anylogic.engine.markup.rack\_system](package-summary.md)

# Interface IRackSystemDescriptorFactory

---

```
public interface IRackSystemDescriptorFactory
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final IRackSystemDescriptorFactory` | `INSTANCE` |  |
| `static final String` | `LIBRARY_FACTORY_CLASS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T extends IRackSystemDescriptor> T` | `create(Class<T> type)` |  |
| `static <T extends IRackSystemDescriptor> T` | `create(Class<T> type, boolean lazy)` |  |
| `static IRackSystemDescriptorFactory` | `createInstance()` |  |
| `<T extends Agent> IStorageDescriptor` | `createStorageDescriptor()` |  |
