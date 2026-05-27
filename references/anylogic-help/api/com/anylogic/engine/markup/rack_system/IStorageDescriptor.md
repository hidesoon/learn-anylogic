*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/rack_system/IStorageDescriptor.html>*

---

Package [com.anylogic.engine.markup.rack\_system](package-summary.md)

# Interface IStorageDescriptor

All Superinterfaces:
:   `IMarkupLibraryDescriptor`, `IRackSystemDescriptor`

---

```
public interface IStorageDescriptor
extends IRackSystemDescriptor
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `capacity()` |  |
| `boolean` | `contains(Agent agent)` |  |
| `void` | `deactivateCells(int rack)` |  |
| `void` | `deactivateCells(int rack, int bay)` |  |
| `void` | `deactivateCells(int rack, int bay, int shelf)` |  |
| `void` | `enableDebugAnimator(ShapeDrawMode mode)` |  |
| `void` | `enableGeometryAnimator()` |  |
| `List<StorageCell>` | `freeCellsInBay(int unit, int bay)` |  |
| `List<StorageCell>` | `freeCellsInSlot(int unit, int bay, int level)` |  |
| `List<StorageCell>` | `freeCellsInUnit(int unit)` |  |
| `List<Agent>` | `getAccessibleAgents()` |  |
| `List<Agent>` | `getAgents()` |  |
| `List<Agent>` | `getAgentsInCell(int unit, int bay, int level, int deep)` |  |
| `int` | `getAisleCapacityRestriction()` |  |
| `StorageCell` | `getCell(int rack, int bay, int shelf, int deepPosition)` |  |
| `StorageCell` | `getCell(Agent agent)` |  |
| `List<StorageCell>` | `getCells()` |  |
| `double` | `getInslotSpeed(SpeedUnits units)` |  |
| `Position` | `getPositionInAisle(int rack, int bay, boolean loadingSide)` |  |
| `Position` | `getPositionInAisle(Agent agent, boolean loadingSide)` |  |
| `StorageSlot` | `getRandomAvailableSlot()` |  |
| `StorageCell` | `getRandomFreeCell()` |  |
| `Map<? extends StorageSlot,? extends Supplier<Pair<Double,Integer>>>` | `getShiftingSlotsInfo()` |  |
| `StorageSlot` | `getSlotPointer(int rack, int bay, int shelf)` |  |
| `boolean` | `hasSpace()` |  |
| `boolean` | `hasSpace(int unit, int bay, int level)` |  |
| `boolean` | `isFree(int unit, int bay, int level, int depth)` |  |
| `boolean` | `isIgnoreCellAccessibility()` |  |
| `boolean` | `isRestrictedAisleAccess()` |  |
| `boolean` | `isSpecifiedInslotSpeed()` |  |
| `boolean` | `isUnitAccessibleFromLeftAdd(int unit)` |  |
| `boolean` | `isUnitAccessibleFromLeftRemove(int unit)` |  |
| `boolean` | `isUnitAccessibleFromRightAdd(int unit)` |  |
| `boolean` | `isUnitAccessibleFromRightRemove(int unit)` |  |
| `int` | `nFreeCells()` |  |
| `int` | `nFreeCells(int rack)` |  |
| `int` | `nFreeCells(int rack, int bay)` |  |
| `int` | `nFreeCells(int rack, int bay, int level)` |  |
| `int` | `nReservedCells()` |  |
| `int` | `nRetrieved()` |  |
| `int` | `nStored()` |  |
| `void` | `onAgentRetrieval(Agent agent, StorageCell cell)` |  |
| `void` | `onAgentStorage(Agent agent, StorageCell cell)` |  |
| `void` | `reserve(int unit, int bay, int level, Agent agent)` |  |
| `void` | `reserve(int rack, int bay, Agent agent)` |  |
| `List<StorageCell>` | `reservedCells(int unit)` |  |
| `List<StorageCell>` | `reservedCells(int unit, int bay)` |  |
| `List<StorageCell>` | `reservedCells(int unit, int bay, int level)` |  |
| `void` | `resetStats()` |  |
| `Agent` | `retrieve(int rack)` |  |
| `Agent` | `retrieve(int rack, int bay)` |  |
| `Agent` | `retrieve(int rack, int bay, int shelf)` |  |
| `Agent` | `retrieveAgent(Agent agent)` |  |
| `void` | `setAisleCapacityRestriction(int value)` |  |
| `void` | `setIgnoreCellAccessibility(boolean ignore)` |  |
| `void` | `setInslotSpeed(double value, SpeedUnits units)` |  |
| `void` | `setRestrictedAisleAccess(boolean value)` |  |
| `void` | `setSpecifiedInslotSpeed(boolean value)` |  |
| `int` | `size()` |  |
| `void` | `store(Agent agent)` |  |
| `void` | `store(Agent agent, int rack)` |  |
| `void` | `store(Agent agent, int rack, int bay)` |  |
| `void` | `store(Agent agent, int rack, int bay, int shelf)` |  |
| `boolean` | `unitHasAvailableCells(int unit, Agent agent)` |  |
| `void` | `unreserve(Agent agent)` |  |
| `double` | `utilization()` |  |
