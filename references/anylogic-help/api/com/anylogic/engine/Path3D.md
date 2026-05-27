*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Path3D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Path3D

All Superinterfaces:
:   `Locatable2D`, `Locatable3D`, `Path2D`

All Known Implementing Classes:
:   `ShapeCurve`, `ShapeMultiplePoints`, `ShapePolyLine`

---

```
public interface Path3D
extends Path2D, Locatable3D
```

This interface represents a sequence of `(x, y, z)` points
Coordinates of all the points
`(Path2D.getPointDx(int), Path2D.getPointDy(int), getPointDz(int))`
are relative to the base coordinates
`(Path2D.getX(), Path2D.getY(), getZ())`

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getPointDz(int i)` | Returns the z coordinate of a particular point of the path relative to the start point. |
| `double` | `getZ()` | Returns the base z coordinate of the path. |
