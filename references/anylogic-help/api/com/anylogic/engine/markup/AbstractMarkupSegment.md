*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractMarkupSegment.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractMarkupSegment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.AbstractMarkupSegment

All Implemented Interfaces:
:   `IMarkupSegment`, `Serializable`

Direct Known Subclasses:
:   `GISMarkupSegment`, `MarkupSegment`

---

```
public abstract class AbstractMarkupSegment
extends Object
implements IMarkupSegment, Serializable
```

This class represents a segment of `IPath`.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractMarkupSegment)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractMarkupSegment()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getAngle()` | Returns the angle between the segment and XY plane |
| `abstract Position` | `getEnd(Position out)` | Returns the location of the end position of the segment |
| `abstract Position` | `getStart(Position out)` | Returns the location of the start position of the segment |
| `boolean` | `is2D()` | Returns true, if the segment is flat in XY plane (dz = 0), false otherwise |
| `double` | `length()` | Returns the length of the path segment |
| `double` | `length2D()` | Returns the length of the projection of the path segment on XY plane |
