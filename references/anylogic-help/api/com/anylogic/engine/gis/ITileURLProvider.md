*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/ITileURLProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface ITileURLProvider

All Known Implementing Classes:
:   `TileURLProvider`

---

```
@AnyLogicInternalAPI
public interface ITileURLProvider
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
`com.anylogic.engine.presentation.ShapeGISMap` has tile layer. This interface is used to get URL for downloading tile.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getSourceName()` | Returns the name of tile provider. |
| `String` | `getTileURL(int x, int y, int zoom)` | See details on [openstreetmap.org](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) |
