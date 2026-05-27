*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/QueueSerpentine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class QueueSerpentine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[ServiceWLine](ServiceWLine.md "class in com.anylogic.engine.markup")<?>>

[com.anylogic.engine.markup.QueuePath](QueuePath.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.QueueSerpentine

All Implemented Interfaces:
:   `HasBoundingRectangle`, `QueueUnit`, `Serializable`

---

```
public class QueueSerpentine
extends QueuePath
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.QueueSerpentine)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `QueueSerpentine()` |  |
| `QueueSerpentine(double width, Color beltBarrierColor, MarkupSegment... segments)` |  |
| `QueueSerpentine(int capacity, double width, Color beltBarrierColor, MarkupSegment... segments)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `Color` | `getBeltBarrierColor()` | Returns the color of belt barrier |
| `double` | `getWidth()` | Returns the width of the queue in pixels |
| `void` | `setBeltBarrierColor(Color beltBarrierColor)` | Sets the color of belt barrier |
| `void` | `setWidth(double width)` | Sets the width of this queue |
