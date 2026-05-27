*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/descriptors/IDescriptorFactory.html>*

---

Package [com.anylogic.engine.markup.descriptors](package-summary.md)

# Interface IDescriptorFactory

---

```
public interface IDescriptorFactory
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final IDescriptorFactory` | `INSTANCE` |  |
| `static final String` | `LIBRARY_FACTORY_CLASS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T extends IDescriptor> T` | `create(Class<T> type)` |  |
| `static <T extends IDescriptor> T` | `create(Class<T> type, boolean lazy)` |  |
| `<T extends Agent> IAreaNodeDescriptor<T>` | `createAreaNodeDescriptor()` |  |
| `static IDescriptorFactory` | `createInstance()` |  |
| `<T extends Agent> IRailStopLineDescriptor<T>` | `createRailStopLineDescriptor()` |  |
| `<T extends Agent> IStopLineDescriptor<T>` | `createStopLineDescriptor()` |  |
