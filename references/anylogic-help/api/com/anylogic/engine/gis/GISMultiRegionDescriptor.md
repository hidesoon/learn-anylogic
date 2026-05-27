*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISMultiRegionDescriptor.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISMultiRegionDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.GISMarkupDescriptor](GISMarkupDescriptor.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GISMultiRegionDescriptor

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class GISMultiRegionDescriptor
extends GISMarkupDescriptor
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.GISMultiRegionDescriptor)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISMultiRegionDescriptor(Long id, String name, String address, String clazz, String type, List<GISRegionDescriptor> regionHolders)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<GISRegionDescriptor>` | `getRegionDescriptors()` |  |
