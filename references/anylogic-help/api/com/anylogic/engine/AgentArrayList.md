*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentArrayList.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AgentArrayList<E extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentList](AgentList.md "class in com.anylogic.engine")<E>

com.anylogic.engine.AgentArrayList<E>

Type Parameters:
:   `E` - agent type

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `IterableWithSize<E>`, `Serializable`, `Iterable<E>`

---

```
public class AgentArrayList<E extends Agent>
extends AgentList<E>
```

Agent population list based on array implementation
Supports fast element retrieval by its index (the [`get(int)`](#get(int)) operation
runs in constant time).
The add operation runs in amortized constant time, that is, adding n elements
requires O(n) time.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.AgentArrayList)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentArrayList(Agent owner)` | Constructs an empty list with an initial capacity of ten. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `_add(E agent)` | **This method should not be called by user**  Call `add_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( population )` |
| `boolean` | `_remove(Agent agent)` | **This method should not be called by user**  Call `remove_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( null )` |
| `boolean` | `contains(Object agent)` | Returns `true` if this agent population contains the specified element. |
| `E` | `get(int index)` | Returns the agent element at the specified position in this agent population.  The position index is the number of list element in the insertion order (i.e. |
| `boolean` | `isEmpty()` | Returns `true` if this agent population contains no elements. |
| `Iterator<E>` | `iterator()` | Returns an iterator over the agent population.  This iterator guarantees the insertion order of elements (i.e. |
| `int` | `size()` | Returns the number of elements in this agent population.  If this collection contains more than `Integer.MAX_VALUE` elements, returns `Integer.MAX_VALUE`. |
| `Stream<E>` | `stream()` | Returns a sequential Stream with this agent population as its source. |
| `String` | `toString()` |  |
