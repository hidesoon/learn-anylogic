*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISShortestPathData.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISShortestPathData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.ShortestPathData](ShortestPathData.md "class in com.anylogic.engine.markup")<[GISNode](GISNode.md "class in com.anylogic.engine.markup"),[GISRoute](GISRoute.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.GISShortestPathData

All Implemented Interfaces:
:   `IPathData`, `Serializable`

---

```
public class GISShortestPathData
extends ShortestPathData<GISNode,GISRoute>
```

Implementation of `ShortestPathData` for GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISShortestPathData)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISShortestPathData()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `getFromTargetPosition(double offset, Position out)` | Returns the Position object that corresponds to the point that lies at a certain distance from target point in the direction to the end point |
| `Position` | `getToSourcePosition(double offset, Position out)` | Returns the Position object that corresponds to the point that lies at a certain distance from start point in the direction to source point |
| `void` | `resetFromTargetDirection()` | Resets the direction from target to the stored toPoint |
| `void` | `resetToSourceDirection()` | Resets the direction from the stored fromPoint to the source |
| `void` | `setFromTargetDirection(Point toPoint)` | Sets the direction and rotations from the target point to the specified argument point |
| `void` | `setToSourceDirection(Point fromPoint)` | Sets the direction and rotations from the specified argument point to the source point |
