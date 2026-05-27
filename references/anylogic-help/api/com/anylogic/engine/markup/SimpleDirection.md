*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/SimpleDirection.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Enum Class SimpleDirection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[SimpleDirection](SimpleDirection.md "enum class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.SimpleDirection

All Implemented Interfaces:
:   `Serializable`, `Comparable<SimpleDirection>`, `Constable`

---

```
@AnyLogicInternalAPI
public enum SimpleDirection
extends Enum<SimpleDirection>
```

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract Position` | `getEndPosition(IPath path, Position out)` |  |
| `abstract INode` | `getNextNode(INode node)` | Call this method for [`NodeType.TRANSIT`](NodeType.md#TRANSIT) nodes only |
| `abstract INode` | `getNextNode(IPath path)` |  |
| `abstract IPath` | `getNextPath(INode node)` | Call this method for [`NodeType.TRANSIT`](NodeType.md#TRANSIT) nodes only |
| `abstract double` | `getOffsetOnPath(double baseOffset, double relativeOffset)` |  |
| `abstract double` | `getOffsetOnPath(IPath path, double distance)` |  |
| `abstract Position` | `getPositionAtOffset(IPath path, double offset, Position out)` |  |
| `abstract double` | `getRemainingLength(IPath path, double baseOffset)` |  |
| `abstract SimpleDirection` | `reverse()` |  |
| `static SimpleDirection` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static SimpleDirection[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
