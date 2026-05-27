*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/rail/IRailLibraryDataSourceFactory.html>*

---

Package [com.anylogic.engine.markup.rail](package-summary.md)

# Interface IRailLibraryDataSourceFactory

---

```
public interface IRailLibraryDataSourceFactory
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final IRailLibraryDataSourceFactory` | `INSTANCE` |  |
| `static final String` | `LIBRARY_FACTORY_CLASS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T> T` | `create(Object markup)` |  |
| `static <T> T` | `create(Object markup, boolean lazy)` |  |
| `static IRailLibraryDataSourceFactory` | `createInstance()` |  |
| `SwitchDataSource` | `createSwitchDataSource(RailwaySwitch markup)` |  |
| `TrackDataSource` | `createTrackDataSource(RailwayTrack markup)` |  |
| `static void` | `throwRailLibNotLoadedError()` |  |
