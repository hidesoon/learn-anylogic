*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PathConnector.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PathConnector<P extends IPath<N>,N extends INode<N,P>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.PathConnector<P,N>

All Implemented Interfaces:
:   `Serializable`

---

```
public class PathConnector<P extends IPath<N>,N extends INode<N,P>>
extends Object
implements Serializable
```

Path connector inside a point node connects one path with another one.
If moving in the opposite direction is possible then connector is also bidirectional.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PathConnector)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PathConnector(P startPath, P endPath, boolean bidirectional, MarkupSegment... segments)` | A connection between two paths inside [`PointNode`](PointNode.md "class in com.anylogic.engine.markup") |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `P` | `getEndPath()` | Returns the path this connector ends at |
| `Path` | `getPathConnector()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `P` | `getStartPath()` | Returns the path this connector starts at |
| `boolean` | `isBidirectional()` | Returns the 'bidirectional' property |
| `double` | `length()` |  |
| `double` | `length(LengthUnits units)` |  |
| `String` | `toString()` |  |
