*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/IGISSearch.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface IGISSearch

All Known Implementing Classes:
:   `AnyLogicOnlineGISSearch`, `CachedGISSearch`, `ChainedGISSearch`, `ServerCaringGISSearch`

---

```
@AnyLogicInternalAPI
public interface IGISSearch
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResult<List<GISMarkupDescriptor>>` | `get(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
