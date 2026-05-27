*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Statechart.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Statechart<T extends Enum<T> & IStatechartState<?,T>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Statechart<T>

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class Statechart<T extends Enum<T> & IStatechartState<?,T>>
extends Object
implements Serializable, com.anylogic.engine.internal.Child
```

Statechart - the most advanced construct to describe event- and time-driven
behavior. Statechart has states and transitions. Transitions may be triggered
by timeouts or rates, messages received by the statechart, and conditions.
Transition execution may lead to a state change where a new set of transitions
becomes active. States in the statechart may be hierarchical, i.e. contain other
states and transitions. The actual structure of state diagram is stored in the
agent.
There are two ways to send a message to the statechart:
- call [`receiveMessage(Object)`](#receiveMessage(java.lang.Object)) or [`receiveMessage(int)`](#receiveMessage(int)) method, and
- call [`fireEvent(Object)`](#fireEvent(java.lang.Object)) method.
**receiveMessage()** assumes no queuing for incoming messages. If the received message
cannot immediately cause scheduling of a transition, it is discarded. Therefore,
if, for example, there are two transitions: one (from state S0 to S1) triggered by
message A, and another (from S1 to S2) triggered by message B, and the statechart
receives messages A and B at the same time while in the state S0, only first
transition will be taken, and message B will be discarded.
**fireEvent()** supports queuing for incoming messages.
The message added to the queue by fireEvent() can be consumed
either immediately or after a number of zero-time steps of the statechart, otherwise
it will be discarded. In the example above both transitions will be taken if the
messages A and B are received via fireEvent() method.
Using fireEvent() is less efficient than using receiveMessage() both time and
memory-wise, so if you do care and are sure that no "chains" of zero-time
message-triggered transitions can happen, use receiveMessage().
**Memory**: sizeof(Object) + 18 bytes + sizeof(array with concurrently active transitions)
+ sizeof(message queue)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Statechart)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Statechart(Agent ao, short maxat)` | Constructs the statechart object. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `fireEvent(Object msg)` | Adds a message to the statechart queue. |
| `Agent` | `getActiveObject()` | Deprecated. Use [`getAgent()`](#getAgent()) instead |
| `T` | `getActiveSimpleState()` | Returns the currently active simple state of the statechart |
| `Agent` | `getAgent()` | Returns the agent that owns the statechart. |
| `String` | `getFullName()` | Returns the name of the statechart prefixed by the full name of its agent. |
| `Set<T>` | `getFullState()` | Returns the currently active composite states of the statechart, including the current simple state. |
| `String` | `getName()` | Returns the name of the statechart as specified by the user |
| `T` | `getState()` | Returns the currently active *simple state* of the statechart.  Please note that this function doesn't return composite states |
| `boolean` | `isStateActive(IStatechartState state)` | Returns `true` if the statechart is at the specified state, i.e. |
| `void` | `onChange()` | Should be called if the statechart has at least one transition of type Condition or Rate when something changes in the agent and probably rate changes or condition becomes `true`. |
| `void` | `onDestroy()` | Should be called when the statechart is destroyed, e.g. |
| `boolean` | `receiveMessage(int msg)` | Same as [`receiveMessage(Object)`](#receiveMessage(java.lang.Object)) but with an integer as message. |
| `boolean` | `receiveMessage(Object msg)` | Posts a message to the statechart without queueing: the message is either immediately consumed (if there is a matching transition active) or is discarded. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setActiveState_xjal(T st)` | *This method is shouldn't be called by user (is public due to technical reasons)* |
| `void` | `start()` | Should be called when the agent starts. |
| `String` | `toString()` |  |
