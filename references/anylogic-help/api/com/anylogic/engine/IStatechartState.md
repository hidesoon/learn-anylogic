*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IStatechartState.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IStatechartState<A extends Agent,T extends Enum<T> & IStatechartState<A,T>>

Type Parameters:
:   `T` - the self-type of units enum

---

```
public interface IStatechartState<A extends Agent,T extends Enum<T> & IStatechartState<A,T>>
```

Base interface for all statechart state enumerations

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default Collection<T>` | `calculateAllSimpleStatesDeep()` |  |
| `default Set<T>` | `calculateFullState()` |  |
| `default Set<T>` | `calculateStatesInside()` |  |
| `default boolean` | `containsState(T simpleState)` | Checks if this state of a statechart is composite and it contains another (deep contents - inside contained composite states - are also checked). |
| `default T` | `getContainerState()` | Returns the immediate container state of this state or `null` if this state is at the topmost level (has no container state). |
| `Set<T>` | `getFullState()` | Returns the *unordered* set containing this state and all (if any) composite states containing this state.   Internal technical info for code generation: Typical implementation:`return fullState;` where the field is initialized lazily: `fullState = calculateFullState();` |
| `Collection<T>` | `getSimpleStatesDeep()` | Returns collection of all simple states inside this state.  Typical implementation:`return simpleStates;` where the field is initialized in constructor: `simpleStates = calculateAllSimpleStatesDeep();` |
| `Statechart<T>` | `getStatechart(A agent)` | Returns statechart from the given agent which owns this state.  Returns `null` if the agent has no statechart with this state |
| `Set<T>` | `getStatesInside()` | Returns *unordered* set of all, simple & composite, states inside this state. |
| `default boolean` | `inState(Agent agent)` |  |
| `default boolean` | `isSimpleState()` | Returns `true` if this state is a simple (not composite) state |
| `String` | `name()` | Returns the name of a statechart state. |
| `int` | `ordinal()` | Returns the ordinal number of this state in the statechart (states are numbered in some deterministic order) |
