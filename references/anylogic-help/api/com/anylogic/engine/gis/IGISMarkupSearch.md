*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/IGISMarkupSearch.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface IGISMarkupSearch<T,P extends T,R extends T,MR>

Type Parameters:
:   `T` - Base type of search result entry
:   `P` - Point on the Earth
:   `R` - Region on the Earth
:   `MR` - Multiregion

All Known Implementing Classes:
:   `AnyLogicOnlineGISMarkupSearch`, `GISMarkupSearchImpl`

---

```
@AnyLogicInternalAPI
public interface IGISMarkupSearch<T,P extends T,R extends T,MR>
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Basic interface for geographical search in AnyLogic.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<T>` | `search(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area. |
| `List<MR>` | `searchMultiRegions(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
| `List<P>` | `searchPoints(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area first. |
| `List<R>` | `searchRegions(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area first. |
