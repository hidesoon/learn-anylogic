*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Attractor.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Attractor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[AreaNode](AreaNode.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.Attractor

All Implemented Interfaces:
:   `Serializable`

---

```
public class Attractor
extends AbstractMarkupSubunit<AreaNode>
```

Attractor markup element: defines (x, y) location + orientation (rotation) of a point within some area / node markup.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`RectangularNode`](RectangularNode.md "class in com.anylogic.engine.markup")[`PolygonalNode`](PolygonalNode.md "class in com.anylogic.engine.markup")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Attractor)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Attractor(double x, double y, double orientation)` | Deprecated. use AreaNode#addAttractor(x, y, orientation) instead |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getOrientation()` | Returns the orientation. |
| `Position` | `getPosition(Position out)` | Returns the position associated with this attractor. |
| `double` | `getRelativeX()` | Deprecated. |
| `double` | `getRelativeY()` | Deprecated. |
| `double` | `getX()` | Returns the absolute x coordinate |
| `double` | `getY()` | Returns the absolute y coordinate |
| `double` | `getZ()` | Returns the absolute z coordinate (which is defined by container node/area) |
