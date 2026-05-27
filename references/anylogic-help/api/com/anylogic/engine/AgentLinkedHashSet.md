*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentLinkedHashSet.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AgentLinkedHashSet<E extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentList](AgentList.md "class in com.anylogic.engine")<E>

com.anylogic.engine.AgentLinkedHashSet<E>

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `IterableWithSize<E>`, `Serializable`, `Iterable<E>`

---

```
public class AgentLinkedHashSet<E extends Agent>
extends AgentList<E>
```

Agent population collection based on [`LinkedHashSet`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashSet.html "class or interface in java.util") implementation
This collection offers constant time performance for the basic operations (add,
remove, contains and size) and guarantees insertion-order during iteration

*Note, that due to set-based implementation, element retrieval by its index
([`get(int)`](#get(int))) is extremely slow when rapidly invoked it with random
index for large collections. In a similar manner, [`Agent.getIndex()`](Agent.md#getIndex())
method of agents in this collection will be slow too.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.AgentLinkedHashSet)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentLinkedHashSet(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `_add(E agent)` | **This method should not be called by user**  Call `add_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( population )` |
| `boolean` | `_remove(Agent agent)` | **This method should not be called by user**  Call `remove_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( null )` |
| `boolean` | `contains(Object agent)` | Returns `true` if this agent population contains the specified element. |
| `E` | `get(int index)` | Returns the agent element at the specified position in this agent population.  This method is extremely slow when rapidly calling it with random index for large collections |
| `boolean` | `isEmpty()` | Returns `true` if this agent population contains no elements. |
| `Iterator<E>` | `iterator()` | Returns an iterator over the agent population.  This iterator guarantees the insertion order of elements (i.e. |
| `int` | `size()` | Returns the number of elements in this agent population.  If this collection contains more than `Integer.MAX_VALUE` elements, returns `Integer.MAX_VALUE`. |
| `Stream<E>` | `stream()` | Returns a sequential Stream with this agent population as its source. |
| `String` | `toString()` |  |
