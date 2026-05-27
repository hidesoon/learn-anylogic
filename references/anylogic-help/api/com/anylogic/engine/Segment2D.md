*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Segment2D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Segment2D

All Superinterfaces:
:   `Locatable2D`

All Known Subinterfaces:
:   `Segment3D`

All Known Implementing Classes:
:   `ShapeArrowLine`, `ShapeLine`

---

```
public interface Segment2D
extends Locatable2D
```

This interface represents a segment: `(x, y) - (x+dx, y+dy)`

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDx()` | Returns the x-offset of the end segment point relative to the start one (the difference of x coordinates of the segment end and start points). |
| `double` | `getDy()` | Returns the y-offset of the end segment point relative to the start one (the difference of y coordinates of the segment end and start points). |
| `double` | `getEndX()` | Returns the x coordinate of the segment end point. |
| `double` | `getEndY()` | Returns the y coordinate of the segment end point. |
| `double` | `getX()` | Returns the x coordinate of the start segment point. |
| `double` | `getY()` | Returns the y coordinate of the start segment point. |
