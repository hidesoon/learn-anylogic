*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/rail/TrackDataSource.html>*

---

Package [com.anylogic.engine.markup.rail](package-summary.md)

# Interface TrackDataSource

All Superinterfaces:
:   `Serializable`

---

```
public interface TrackDataSource
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addToReservations(Agent... trains)` | Allow the specified trains to go through the track. |
| `void` | `cancelReservation()` | Cancel any existing reservations, if any. |
| `Agent` | `getCar(int index)` | Returns a car on the track at a given position counted from the beginning of the track. |
| `List<Agent>` | `getCars()` | Returns the list of rail cars that are (maybe, partially) located of this track |
| `Agent` | `getFirstCar()` | Returns the car closest to the beginning of the track, or null if the track is empty |
| `double` | `getFreeSpace(boolean fromstart)` | Tests the availability of space on the track. |
| `Agent` | `getLastCar()` | Returns the car closest to the end of the track, or null if the track is empty |
| `int` | `getNCars()` | Returns the number of cars on the track (including partially) |
| `List<Agent>` | `getReservations()` | Return all the trains that this track has been reserved for |
| `List<Agent>` | `getTrains()` | Returns the list of the trains on the track |
| `boolean` | `isAvailableFor(Agent train)` | Tests if the certain train is prohibited from moving through the track |
| `boolean` | `isEmpty()` | Tests if the track is empty, i.e. |
| `void` | `onToggleBlock()` | Callback at block status toggle |
| `void` | `removeFromReservations(Agent... trains)` | Disallow the specified trains to go through the track. |
| `void` | `reserveFor(Agent... trains)` | Allow or disallow the specified trains to go through the track. |
