*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Segment3D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Segment3D

All Superinterfaces:
:   `Locatable2D`, `Locatable3D`, `Segment2D`

All Known Implementing Classes:
:   `ShapeArrowLine`, `ShapeLine`

---

```
public interface Segment3D
extends Segment2D, Locatable3D
```

This interface represents a segment:
`(x, y, z) - (x+dx, y+dy, z+dz)`

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDz()` | Returns the z-offset of the end segment point relative to the start one (the difference of z coordinates of the segment end and start points). |
| `double` | `getEndZ()` | Returns the z coordinate of the segment end point. |
| `double` | `getZ()` | Returns the z coordinate of the start segment point. |
