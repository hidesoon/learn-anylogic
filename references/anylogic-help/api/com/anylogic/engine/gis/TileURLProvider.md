*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/TileURLProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class TileURLProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.TileURLProvider

All Implemented Interfaces:
:   `ITileURLProvider`

---

```
@AnyLogicInternalAPI
public class TileURLProvider
extends Object
implements ITileURLProvider
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TileURLProvider(String... urls)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static String` | `applyParameters(String url, int x, int y, int z)` |  |
| `String` | `getSourceName()` | Returns the name of tile provider. |
| `String` | `getTileURL(int x, int y, int z)` | See details on [openstreetmap.org](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) |
