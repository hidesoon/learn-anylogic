*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISMarkupSegment.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISMarkupSegment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSegment](AbstractMarkupSegment.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISMarkupSegment

All Implemented Interfaces:
:   `IMarkupSegment`, `Serializable`

Direct Known Subclasses:
:   `GISMarkupSegmentLine`

---

```
public abstract class GISMarkupSegment
extends AbstractMarkupSegment
```

Markup segment for GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISMarkupSegment)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `length()` | Returns the length of the path segment |
| `final void` | `setEnd(double lat, double lon)` | Sets the end point of this GIS segment. |
| `void` | `setEnd(Point endPoint)` | Sets end point of this segment. |
| `final void` | `setStart(double lat, double lon)` | Sets the starting point of this GIS segment. |
| `void` | `setStart(Point startPoint)` | Sets start point of this segment. |
| `final void` | `setStartNextTo(IMarkupSegment previousSegment)` | Sets coordinates of the end of the specified segment as start coordinates of this segment. |
