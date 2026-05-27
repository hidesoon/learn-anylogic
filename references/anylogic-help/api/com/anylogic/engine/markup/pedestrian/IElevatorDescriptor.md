*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/pedestrian/IElevatorDescriptor.html>*

---

Package [com.anylogic.engine.markup.pedestrian](package-summary.md)

# Interface IElevatorDescriptor<A extends Agent>

All Superinterfaces:
:   `IMarkupLibraryDescriptor`

All Known Implementing Classes:
:   `Elevator`

---

```
public interface IElevatorDescriptor<A extends Agent>
extends IMarkupLibraryDescriptor
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Level[]` | `accessibleLevels()` |  |
| `void` | `addAccessibleLevels(Level... levels)` |  |
| `void` | `deleteCallsOnLevel(Level level)` |  |
| `void` | `disableDoor(Level level, ElevatorDoor door)` |  |
| `void` | `dropOffPeds(Collection<? extends Agent> peds)` |  |
| `void` | `enableDoor(Level level, ElevatorDoor door)` |  |
| `void` | `fail()` |  |
| `double` | `getCabinZ()` |  |
| `List<? extends Elevator.Call<A>>` | `getCalls()` |  |
| `int` | `getCapacity()` |  |
| `ElevatorDirection` | `getCurrentDirection()` |  |
| `Level` | `getCurrentLevel()` |  |
| `ElevatorMovementMode` | `getMovementMode()` |  |
| `Level` | `getNearestLevel()` |  |
| `Set<A>` | `getPeds()` |  |
| `Level` | `getPedTargetLevel(Agent ped)` |  |
| `List<Level>` | `getRoute()` |  |
| `double` | `getSpeed(SpeedUnits units)` |  |
| `ElevatorState` | `getState()` |  |
| `Level` | `getTargetLevel()` |  |
| `double` | `getTimePerLevel(TimeUnits units)` |  |
| `Set<A>` | `getWaitingPeds()` |  |
| `Set<A>` | `getWaitingPeds(Level level)` |  |
| `boolean` | `isAllLevels()` |  |
| `boolean` | `isDoorEnabled(Level level, ElevatorDoor door)` |  |
| `boolean` | `isFailed()` |  |
| `boolean` | `isManualMode()` |  |
| `double` | `meanWaitingTime()` |  |
| `double` | `meanWaitingTime(Level level)` |  |
| `double` | `meanWaitingTime(Level level, TimeUnits units)` |  |
| `double` | `meanWaitingTime(TimeUnits units)` |  |
| `double` | `minStayTime(TimeUnits units)` |  |
| `void` | `moveTo(Level level, boolean stayInManualMode)` |  |
| `int` | `nDroppedOffPeds(Level level)` |  |
| `int` | `nPickedUpPeds(Level level)` |  |
| `int` | `nTransportedPeds()` |  |
| `void` | `onArrival(Level level, List<A> waitingAgents)` |  |
| `void` | `onDeparture(Level level)` |  |
| `void` | `onFailed()` |  |
| `void` | `onRepaired()` |  |
| `void` | `onStateChanged(ElevatorState newState)` |  |
| `void` | `pickUpPeds(Collection<? extends Agent> peds)` |  |
| `void` | `repair()` |  |
| `void` | `resetStats()` |  |
| `void` | `setAllLevels(boolean allLevels)` |  |
| `void` | `setCapacity(int capacity)` |  |
| `void` | `setManualMode(boolean on)` |  |
| `void` | `setMarkup(Elevator<A> elevator)` |  |
| `void` | `setMovementMode(ElevatorMovementMode movementMode)` |  |
| `void` | `setOwner(Agent owner)` |  |
| `void` | `setSpeed(double speed, SpeedUnits units)` |  |
| `void` | `setTimePerLevel(double timePerLevel, TimeUnits units)` |  |
| `double` | `timeInState(ElevatorState state)` |  |
| `double` | `timeInState(ElevatorState state, TimeUnits units)` |  |
| `double` | `totalTravelTime()` |  |
| `double` | `totalTravelTime(TimeUnits units)` |  |
| `double` | `utilization()` |  |
