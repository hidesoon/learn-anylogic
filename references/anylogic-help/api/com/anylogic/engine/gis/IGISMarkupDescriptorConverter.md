*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/IGISMarkupDescriptorConverter.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface IGISMarkupDescriptorConverter<T,P extends T,R extends T,MR>

Type Parameters:
:   `T` - Base type of search result entry
:   `P` - Point on the Earth
:   `R` - Region on the Earth
:   `MR` - Multiregion

---

```
@AnyLogicInternalAPI
public interface IGISMarkupDescriptorConverter<T,P extends T,R extends T,MR>
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Internal interface for geographical search in AnyLogic.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addMultiRegion(List<T> resultList, GISMultiRegionDescriptor multiRegionDescriptor)` |  |
| `static List<GISRegionDescriptor>` | `extractRegionDescriptors(GISMarkupDescriptor markupDescriptor)` | Just an utility to extract regions from the given descriptor if it is either region or multiregion descriptor. |
| `MR` | `getMultiRegion(GISMarkupDescriptor markupDescriptor)` |  |
| `P` | `getPoint(GISPointDescriptor pointDescriptor)` |  |
| `R` | `getRegion(GISRegionDescriptor regionDescriptor)` |  |
