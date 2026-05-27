*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AnyLogicOnlineGISSearch.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AnyLogicOnlineGISSearch

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.AnyLogicOnlineGISSearch

All Implemented Interfaces:
:   `IGISSearch`

---

```
@AnyLogicInternalAPI
public class AnyLogicOnlineGISSearch
extends Object
implements IGISSearch
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AnyLogicOnlineGISSearch(int precisionInMeters)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResult<List<GISMarkupDescriptor>>` | `get(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
| `void` | `setUrlParamsEncoder(UnaryOperator<String> urlParamsEncoder)` |  |
