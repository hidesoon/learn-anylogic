*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/ServerCaringGISSearch.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class ServerCaringGISSearch

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.ChainedGISSearch](ChainedGISSearch.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.ServerCaringGISSearch

All Implemented Interfaces:
:   `IGISSearch`

---

```
@AnyLogicInternalAPI
public class ServerCaringGISSearch
extends ChainedGISSearch
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
This is a short-circuiting proxy provider which disables itself for a
configured period of time, once the underlying provider returns null

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServerCaringGISSearch(IGISSearch base, long networkRecoveryTimeoutInMillis)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResult<List<GISMarkupDescriptor>>` | `get(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
