*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PalletRackAccess.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface PalletRackAccess<T extends Agent>

All Known Implementing Classes:
:   `PalletRack`

---

```
public interface PalletRackAccess<T extends Agent>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `capacity()` | Returns the total number of cell positions (all the levels and all racks, if there are several), which is `number of rows * number of positions along row * number of deep positions * number of levels` |
| `boolean` | `contains(Agent agent)` | Returns `true` if the given agent is contained within this object |
| `T` | `get(int row, int position, int level, int deepPosition)` | Returns the agent stored at the specified cell [row,position,level,deepPosition], or `null` if the cell is reserved or free. |
| `PalletRackApproachDirection` | `getApproachDirection(Agent agent, int rowToSearch)` | Return the approach direction to the given agent or `null` if agent is unreachable (lies deep in the cell, behind other entities) |
| `T` | `getByIndex(int index)` | Returns the stored agent with a given index. |
| `PalletRackLocation` | `getCellOf(Agent agent)` | Returns the coordinates of a cell with a given agent [row,position,level], or null if the agent is not stored here. |
| `PalletRackLocation` | `getFreeCell(boolean infront)` | Returns the array [row,position,level] with the coordinates of a free cell that is closest to either front of back of the rack system, depending on the parameter infront. |
| `Position` | `getPositionAtCell(int row, int position, int level, int deepPosition, double offset, double depth, boolean leftAisle, Position out)` | Returns the position at the given cell |
| `Position` | `getPositionAtCellEntry(int row, int position, int level, boolean leftAisle, Position out)` | Returns the position at the enter to the given cell |
| `Position` | `getPositionInAisle(int row, int position, boolean leftAisle, Position out)` | Returns the position in the pallet rack aisle located in front of a cell with a given row and position (level does not matter as cells located one above the other have aisle position). |
| `boolean` | `hasSpace()` | Returns `true` if there is enough space for at least one more agents |
| `boolean` | `isFree(int row, int position, int level)` | Tests if a given cell [row,position,level] is free, i.e. |
| `int` | `nFree(int row, int position, int level)` | Tests if a given cell [row,position,level] is free, i.e. |
| `int` | `nReserved(int row, int position, int level)` | Tests if a given cell [row,position,level] is reserved. |
| `void` | `put(int row, int position, int level, boolean leftAisle, Agent agent)` | Puts the agent into the cell with the specified coordinates [row,position,level]. |
| `T` | `randomAgent()` | Returns a random agent in the rack system, or `null` if the rack system is empty. |
| `void` | `release(int row, int position, int level, boolean leftAisle)` | Discards a reservation of a given cell [row,position,level]. |
| `T` | `remove(Agent agent)` | Removes a given agent from the rack system and returns it. |
| `T` | `removeFromCell(int row, int position, int level, boolean leftAisle)` | Removes the agent stored in a given cell [row,position,level] from the rack system and returns it. |
| `T` | `removeFromCell(PalletRackLocation location, boolean leftAisle)` | Removes the agent stored in a given cell [row,position,level] from the rack system and returns it. |
| `void` | `reserve(int row, int position, int level, boolean leftAisle)` | Marks a given cell [row,position,level] as reserved. |
| `int` | `reserved()` | Returns the number of reserved cells in the pallet rack(s). |
| `void` | `resetStats()` | Resets the statistics collected for this object. |
| `int` | `size()` | Returns the number of entities inside |
