*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AgentList.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AgentList<E extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.AgentList<E>

Type Parameters:
:   `E` - agent type

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `IterableWithSize<E>`, `Serializable`, `Iterable<E>`

Direct Known Subclasses:
:   `AgentArrayList`, `AgentLinkedHashSet`

---

```
public abstract class AgentList<E extends Agent>
extends Object
implements Iterable<E>, IterableWithSize<E>, Serializable, com.anylogic.engine.internal.Child
```

Agent population list interface

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`AgentArrayList`](AgentArrayList.md "class in com.anylogic.engine")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.AgentList)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static boolean` | `useObjectIndexCache` | **This field is internal and shouldn't be accessed by user.** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentList(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `_add(E agent)` | **This method should not be called by user**  Call `add_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( population )` |
| `abstract boolean` | `_remove(Agent agent)` | **This method should not be called by user**  Call `remove_EONAME()` method of class containing embedded object with name EONAME or agent.`goToPopulation( null )` |
| `double` | `average(String fieldName)` | Returns the average of (numeric) field values for all agents in this collection |
| `double` | `average(String fieldName, String triggerFieldName)` | Returns the average of (numeric) field values for all agents in this collection which have `true` value of a boolean field with name `triggerFieldName` (if specified) |
| `void` | `callCreate(E agent, int index)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Calls [`Agent.create()`](Agent.md#create()) and performs some other population-related initializations (if required) |
| `void` | `callCreate(E agent, int index, TableInput tableInput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Calls [`Agent.create()`](Agent.md#create()) and performs some other population-related initializations (if required) |
| `void` | `callSetupParameters(E agent, int index)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Sets agent parameters to the values defined in population |
| `void` | `callSetupParameters(E agent, int index, TableInput tableInput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Sets agent parameters to the values defined in population |
| `abstract boolean` | `contains(Object agent)` | Returns `true` if this agent population contains the specified element. |
| `int` | `count(String triggerFieldName)` | Returns the number of agents in this collection which have `true` value of a boolean field with name `triggerFieldName` |
| `void` | `fillFromTable(TableInput tableInput)` | Creates agents from the given table using the parameters mapping configured in AnyLogic, adds to this population and starts agents. |
| `void` | `fillFromTable(TableInput tableInput, BiConsumer<TableInput,E> agentSetupCode, boolean callCreate, boolean startAgents)` | Creates agents from the given table, sets their parameters and adds to this population. |
| `void` | `fillFromTable(TableInput tableInput, BiConsumer<TableInput,E> agentSetupCode, Function<TableInput,Integer> numberOfAgents, boolean callCreate, boolean startAgents)` | Creates agents from the given table, sets their parameters and adds to this population. |
| `List<E>` | `findAll(Predicate<E> condition)` | Returns new list with agents from this population which meet the given condition.  Usage examples: |
| `E` | `findFirst(Predicate<E> condition)` | Returns the first agent from this population which meets the given condition.  Usage example: |
| `abstract E` | `get(int index)` | Returns the agent element at the specified position in this agent population.  The position index is the number of list element in the insertion order (i.e. |
| `Agent` | `getEnvironment()` | Returns the environment where this agent population belongs to. |
| `String` | `getInspectionWindowString()` |  |
| `Agent` | `getOwner()` | Returns the owner agent that encapsulates this population. |
| `<T> T` | `getValueFromTable(String columnLabel, Class<T> returnType)` |  |
| `E` | `instantiateAgent(int index)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Creates new instance of agent for this population.  Should be overridden by code generation, default implementation is unsupported |
| `abstract boolean` | `isEmpty()` | Returns `true` if this agent population contains no elements. |
| `boolean` | `isPresentationEnabled()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `abstract Iterator<E>` | `iterator()` | Returns an iterator over the agent population.  This iterator guarantees the insertion order of elements (i.e. |
| `double` | `max(String fieldName)` | Returns the maximum of (numeric) field values for all agents in this collection |
| `double` | `max(String fieldName, String triggerFieldName)` | Returns the maximum of (numeric) field values for all agents in this collection which have `true` value of a boolean field with name `triggerFieldName` (if specified) |
| `double` | `min(String fieldName)` | Returns the minimum of (numeric) field values for all agents in this collection |
| `double` | `min(String fieldName, String triggerFieldName)` | Returns the minimum of (numeric) field values for all agents in this collection which have `true` value of a boolean field with name `triggerFieldName` (if specified) |
| `double` | `min(Collection<? extends Agent> agents, String fieldName, String triggerFieldName)` | Deprecated. will be removed in the next (7.1+) release, please use [`min(String, String)`](#min(java.lang.String,java.lang.String)) instead |
| `void` | `onChange()` | Calls [onChange()](Agent.md#onChange()) for all the agents in this list. |
| `final E` | `random()` | Randomly returns one agent from this population  (uses uniform distribution from the Engine)  This method runs in linear time  This method returns `null` if the population is empty |
| `final E` | `random(Random r)` | Randomly returns one agent from this population  (ses the specified random number generator to choose the element)  This method runs in linear time  This method returns `null` if the population is empty |
| `E` | `randomExcept(Agent agent)` | Randomly returns one agent from this population except the given agent  (uses uniform distribution from the Engine)  This method runs in linear time  This method returns `null` if the population is empty or contains the only given `agent` |
| `E` | `randomExcept(Set<? extends Agent> agents)` | Randomly returns one agent from this population except the given agents  (uses uniform distribution from the Engine)  This method runs in linear time multiplied by the complexity of 'contains' check of the given set  This method returns `null` if the population is empty or all the agents are contained in the given `agents` set. |
| `final void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setEnvironment(Agent environment)` |  |
| `abstract int` | `size()` | Returns the number of elements in this agent population.  If this collection contains more than `Integer.MAX_VALUE` elements, returns `Integer.MAX_VALUE`. |
| `Stream<E>` | `stream()` | Returns a sequential Stream with this agent population as its source. |
| `double` | `sum(String fieldName)` | Returns the sum of (numeric) field values for all agents in this collection |
| `double` | `sum(String fieldName, String triggerFieldName)` | Returns the sum of (numeric) field values for all agents in this collection which have `true` value of a boolean field with name `triggerFieldName` (if specified) |
