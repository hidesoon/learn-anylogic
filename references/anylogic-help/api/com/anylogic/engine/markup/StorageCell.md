*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/StorageCell.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface StorageCell

All Superinterfaces:
:   `Serializable`

---

```
public interface StorageCell
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Agent` | `cancelReservation()` | Cancels reservation for the agent that reserved this cell. |
| `void` | `deactivate()` | Deactivates the cell and disallows all operations with it. |
| `Agent` | `getAgent()` | Returns the agent that occupies this cell or null if the cell is not occupied |
| `int` | `getBay()` | Returns the index of the bay that this cell belongs to |
| `int` | `getDeepPosition()` | Returns the index of this cell in the slot |
| `int` | `getRack()` | Returns the index of the rack that this cell belongs to |
| `double` | `getRotation()` | Returns the rotation of the storage in radians. |
| `int` | `getShelf()` | Returns the index of the shelf that this cell belongs to |
| `StorageCellState` | `getState()` |  |
| `Storage` | `getStorage()` | Returns the rack storage that this cell belongs to |
| `double` | `getX()` | Returns the X coordinate of this storage cell. |
| `double` | `getY()` | Returns the Y coordinate of this storage cell. |
| `double` | `getZ()` | Returns the Z coordinate of this storage cell. |
| `boolean` | `isActive()` | Returns `true` if the cell is NOT disabled and operates normally, `false` otherwise. |
| `boolean` | `isAvailableToRetrieve()` | Returns `true` if the cell is both accessible and contains an agent, `false` otherwise. |
| `boolean` | `isAvailableToStore()` | Returns `true` if the cell is both open for reservation and accessible, `false` otherwise. |
| `boolean` | `isFree()` | Returns `true` if the cell is empty, active, and not reserved by any agent, `false` otherwise. |
| `Agent` | `retrieve()` | Removes the agent that currently occupies this cell. |
| `void` | `setReservation(Agent agent)` | Reserves this cell for the specified agent. |
| `void` | `store(Agent agent)` | Stores the specified agent in this cell. |
