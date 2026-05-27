*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISCurve.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISCurve

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractCurve](AbstractCurve.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.AbstractNetworkCurve](AbstractNetworkCurve.md "class in com.anylogic.engine.markup")<[GISMarkupSegment](GISMarkupSegment.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.GISCurve

All Implemented Interfaces:
:   `IPathData`, `Serializable`, `Iterable<GISMarkupSegment>`

---

```
@AnyLogicInternalAPI
public abstract class GISCurve
extends AbstractNetworkCurve<GISMarkupSegment>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISCurve)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISCurve()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `lineTo(double lat, double lon)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `lineTo(Point endPoint)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `startDrawing(double lat, double lon)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `void` | `startDrawing(Point startPoint)` | Starts drawing (available for markup elements created with no-argument constructor) |
