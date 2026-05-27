*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Elevator.Call.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface Elevator.Call<T extends Agent>

Enclosing class:
:   [Elevator](Elevator.md "class in com.anylogic.engine.markup")<[A](Elevator.md "type parameter in Elevator") extends [Agent](../Agent.md "class in com.anylogic.engine")>

---

```
public static interface Elevator.Call<T extends Agent>
```

Class describing elevator call at certain level

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ElevatorDirection` | `getDirection()` | Returns call direction. |
| `Level` | `getLevel()` | Returns level this call came from |
| `List<T>` | `getWaitingPeds()` | Returns list of pedestrians waiting for elevator on the level to move in specified direction |
