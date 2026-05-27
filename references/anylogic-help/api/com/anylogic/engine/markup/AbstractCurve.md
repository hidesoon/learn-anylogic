*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractCurve.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractCurve<T extends AbstractMarkupSegment>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.AbstractCurve<T>

All Implemented Interfaces:
:   `IPathData`, `Serializable`, `Iterable<T>`

Direct Known Subclasses:
:   `AbstractNetworkCurve`, `Curve`

---

```
@AnyLogicInternalAPI
public abstract class AbstractCurve<T extends AbstractMarkupSegment>
extends Object
implements IPathData, Iterable<T>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractCurve)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractCurve()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(T segment)` | Adss a segment to this curve when creating the curve from code. |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `double` | `getOffset3D(double offset2D)` | Returns offset on the curve, which correlates to provided offset2D on XY projection |
| `final Position` | `getPositionAt2DOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element at the XY projection with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `T` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `final boolean` | `isInitialized()` | Returns was this markup initialized of not |
| `Iterator<T>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `Stream<T>` | `segmentsStream()` | Creates and returns stream over segments |
| `String` | `toString()` |  |
