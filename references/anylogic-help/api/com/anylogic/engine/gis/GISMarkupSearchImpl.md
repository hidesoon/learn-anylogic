*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISMarkupSearchImpl.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISMarkupSearchImpl<E,P extends E,R extends E,MR>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.GISMarkupSearchImpl<E,P,R,MR>

All Implemented Interfaces:
:   `IGISMarkupSearch<E,P,R,MR>`

Direct Known Subclasses:
:   `AnyLogicOnlineGISMarkupSearch`

---

```
@AnyLogicInternalAPI
public class GISMarkupSearchImpl<E,P extends E,R extends E,MR>
extends Object
implements IGISMarkupSearch<E,P,R,MR>
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISMarkupSearchImpl(IGISSearch search, IGISMarkupDescriptorConverter<E,P,R,MR> converter)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<E>` | `search(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area. |
| `List<MR>` | `searchMultiRegions(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
| `List<P>` | `searchPoints(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area first. |
| `List<R>` | `searchRegions(String query, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` | Search in the preferred area first. |
