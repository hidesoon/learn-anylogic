*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/pedestrian/IPedestrianLibraryDescriptorFactory.html>*

---

Package [com.anylogic.engine.markup.pedestrian](package-summary.md)

# Interface IPedestrianLibraryDescriptorFactory

---

```
public interface IPedestrianLibraryDescriptorFactory
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final IPedestrianLibraryDescriptorFactory` | `INSTANCE` |  |
| `static final String` | `LIBRARY_FACTORY_CLASS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T extends IMarkupLibraryDescriptor> T` | `create(Class<T> type)` |  |
| `static <T extends IMarkupLibraryDescriptor> T` | `create(Class<T> type, boolean lazy)` |  |
| `<A extends Agent> IElevatorDescriptor<A>` | `createElevatorDescriptor()` |  |
| `static IPedestrianLibraryDescriptorFactory` | `createInstance()` |  |
