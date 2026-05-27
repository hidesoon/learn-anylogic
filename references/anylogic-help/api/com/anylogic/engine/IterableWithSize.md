*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IterableWithSize.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IterableWithSize<T>

Type Parameters:
:   `E` - element type

All Superinterfaces:
:   `Iterable<T>`

All Known Implementing Classes:
:   `AgentArrayList`, `AgentLinkedHashSet`, `AgentList`

---

```
@AnyLogicInternalAPI
public interface IterableWithSize<T>
extends Iterable<T>
```

**This interface is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Declares a collection with known size and ability to get element by index.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `T` | `get(int index)` | Returns the element at the specified position in this collection.  Depending on implementation, this method may have good or bad performance. |
| `boolean` | `isEmpty()` | Returns `true` if this collection contains no elements. |
| `int` | `size()` | Returns the number of elements in this collection. |
