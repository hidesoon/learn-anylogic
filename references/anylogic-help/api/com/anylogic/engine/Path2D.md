*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Path2D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Path2D

All Superinterfaces:
:   `Locatable2D`

All Known Subinterfaces:
:   `Path3D`

All Known Implementing Classes:
:   `ShapeCurve`, `ShapeMultiplePoints`, `ShapePolyLine`

---

```
public interface Path2D
extends Locatable2D
```

This interface represents a sequence of `(x, y)` points
Coordinates of all the points
`(getPointDx(int), getPointDy(int))`
are relative to the base coordinates
`(getX(), getY())`

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `getNPoints()` | Returns the number of points in the path. |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the path relative to the start point. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the path relative to the start point. |
| `double` | `getX()` | Returns the base x coordinate of the path. |
| `double` | `getY()` | Returns the base y coordinate of the path. |
