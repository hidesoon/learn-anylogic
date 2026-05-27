*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/elements/IElementDescriptor.html>*

---

Package [com.anylogic.engine.elements](package-summary.md)

# Interface IElementDescriptor

All Superinterfaces:
:   `Serializable`

All Known Implementing Classes:
:   `ElementDescriptorImpl`

---

```
@AnyLogicInternalAPI
public interface IElementDescriptor
extends Serializable
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `GIS_MARKUP_SEGMENTS` |  |
| `static final String` | `LAT_LON_PAIRS` |  |
| `static final String` | `MARKUP_SEGMENTS` |  |
| `static final String` | `MODEL_ELEMENT_DESCRIPTORS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `getProperty(String id)` |  |
| `Set<String>` | `getPropertyNames()` |  |
| `void` | `setProperty(String id, Object value)` |  |
