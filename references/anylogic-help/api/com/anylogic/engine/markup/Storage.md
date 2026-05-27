*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Storage.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Storage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Storage

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `RackUnitAggregator`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Storage
extends AbstractLevelMarkup
implements RackUnitAggregator, HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Storage)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Storage()` | Creates a new Storage with default parameters. |
| `Storage(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, IStorageDescriptor d, double x, double y, double z, RackType rackType, boolean flipped, RackPlacement rackPlacement, int numberOfStorageUnits, int numberOfBays, int numberOfCellsPerSlot, double rightPassageMeter, double leftPassageMeter, double heightMeter, double widthMeter, double aisleWidthMeter, double slotDepthMeter, double cellWidthMeter, double rotation, double tiltAngle, boolean placeSingleRacksAtSides, RackOddSingleRackSide placeOddSingleRack, Color shelvesColor, Color frameColor, boolean drawLegs, int baysBetweenLegs, boolean simplifiedAgentAnimation, int numberOfShelves, double shelfHeightMeter)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancelReservation(Agent agent)` | Discards any reservations made for the specified agent. |
| `int` | `capacity()` | Returns the maximum possible number of agents that can be stored in the storage. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(Agent agent)` | Returns `true` if the specified agent is stored in the storage and `false` otherwise. |
| `List<RectangularNode<Agent>>` | `createAislesGeometry()` |  |
| `void` | `deactivateCells(int rack)` |  |
| `void` | `deactivateCells(int rack, int bay)` |  |
| `void` | `deactivateCells(int rack, int bay, int shelf)` |  |
| `void` | `enableDebugAnimator(ShapeDrawMode mode)` |  |
| `void` | `enableGeometryAnimator()` |  |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `List<StorageCell>` | `freeCells(int rack)` | Returns a list of all free cells in the specified rack. |
| `List<StorageCell>` | `freeCells(int rack, int bay)` | Returns a list of all free cells in the specified bay. |
| `List<StorageCell>` | `freeCells(int rack, int bay, int shelf)` | Returns a list of all free cells in the specified slot Can be called only after markup initialization. |
| `List<Agent>` | `getAccessibleAgents()` |  |
| `double` | `getAccessZone(LengthUnits units)` | Returns the width of access zone in specified length units. |
| `Agent` | `getAgentInCell(int rack, int bay, int shelf, int deepPosition)` | Returns the agent stored in the specified cell. |
| `List<Agent>` | `getAgents()` | Returns a list of agents stored in the storage, ordered according to rack type. |
| `int` | `getAisleCapacityRestriction()` | Returns maximum number of allowed transporters is the storage aisles. |
| `double` | `getAisleWidth()` |  |
| `double` | `getAisleWidth(LengthUnits units)` | Returns the aisle width in specified length units. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `StorageCell` | `getCell(int rack, int bay, int shelf, int deepPosition)` | Returns the specified cell. |
| `StorageCell` | `getCell(Agent agent)` | Returns the cell that contains the specified agent. |
| `Position` | `getCellCenter(int rack, int bay, int shelf, int depth)` |  |
| `double` | `getCellDepth()` |  |
| `double` | `getCellDepth(LengthUnits units)` |  |
| `double` | `getCellHeight()` |  |
| `List<StorageCell>` | `getCells()` | Returns a list of cells ordered according to rack type. |
| `double` | `getCellWidth()` |  |
| `double` | `getCellWidth(LengthUnits units)` | Returns the cell width in specified length units. |
| `Point[]` | `getCorners()` |  |
| `Color` | `getFrameColor()` | Returns the color of rack frame. |
| `double` | `getFullHeight()` |  |
| `double` | `getFullWidth()` |  |
| `double` | `getInslotSpeed(SpeedUnits units)` | Returns in-slot speed in specified speed units. |
| `double` | `getLeftPassage()` |  |
| `IStorageDescriptor` | `getLibraryDescriptor()` |  |
| `int` | `getNumberOfAisles()` |  |
| `int` | `getNumberOfBays()` | Returns the number of bays per rack. |
| `int` | `getNumberOfCellsPerSlot()` | Returns the number of cells per slot. |
| `int` | `getNumberOfRacks()` | Returns the number of racks. |
| `int` | `getNumberOfShelves()` | Returns the number of shelves per rack. |
| `RackOddSingleRackSide` | `getPlaceOddSingleRack()` | Returns the side of the stand alone rack in case of an odd number of racks. |
| `boolean` | `getPlaceSingleRacksAtSides()` | Returns true if stand-alone racks are placed at the sides of the storage. |
| `Position` | `getPositionInAisle(int rack, int bay)` | Returns the position in front of the specified bay (on the side used for storage). |
| `Position` | `getPositionInAisle(int rack, int bay, boolean loadingSide)` | Returns the position in front of the specified bay (on the specified side). |
| `Position` | `getPositionInAisle(Agent agent)` | Returns the position in front of the bay where the specified agent is stored (on the side used for storage). |
| `Position` | `getPositionInAisle(Agent agent, boolean loadingSide)` | Returns the position in front of the bay where the specified agent is stored (on the specified side). |
| `double` | `getRackDepth(LengthUnits units)` | Returns the rack depth in specified length units. |
| `RackPlacement` | `getRackPlacement()` | Returns rack placement type. |
| `RackType` | `getRackType()` | Returns the rack type. |
| `Agent` | `getRandomAccessibleAgent()` | Returns a random accessible agent stored in the storage. |
| `Agent` | `getRandomAgent()` | Returns a random agent stored in the storage. |
| `StorageSlot` | `getRandomAvailableSlot()` |  |
| `StorageCell` | `getRandomFreeCell()` | Returns the next cell available for reservation in a random slot from the storage. |
| `double` | `getRightPassage()` |  |
| `double` | `getRotation()` | Returns the rotation of the storage in radians. |
| `double` | `getShelfHeight(LengthUnits units)` | Returns the z-height of a shelf in specified length units. |
| `Color` | `getShelvesColor()` | Returns the color of rack shelves. |
| `double` | `getShelvesTiltAngle()` | Returns shelves tilt angle in radians. |
| `StorageSlot` | `getSlot(int rack, int bay, int shelf)` | Returns slot address. |
| `double` | `getSlotDepth()` |  |
| `RackUnitAggregator` | `getStorageSystem()` | Returns the storage system this element belongs to. |
| `double` | `getUnitHeight()` |  |
| `double` | `getUnitLength()` |  |
| `double` | `getX()` | Returns the X coordinate of this storage. |
| `double` | `getY()` | Returns the Y coordinate of this storage. |
| `double` | `getZ()` | Returns the Z coordinate of this storage. |
| `boolean` | `hasSpace()` | Returns `true` if the storage has cells available for reservation and `false` otherwise. |
| `boolean` | `hasSpace(int rack, int bay, int shelf)` | Returns `true` if the specified slot has cells available for reservation and `false` otherwise. |
| `boolean` | `isFree(int rack, int bay, int shelf, int depth)` |  |
| `boolean` | `isIgnoreCellAccessibility()` |  |
| `boolean` | `isInvertedRack(int rack)` |  |
| `boolean` | `isLoadingDirectionReversed()` | Returns value of parameter 'Reverse loading direction' |
| `boolean` | `isObstacle()` | Returns `true` if racks of this storage are considered obstacles by transporters moving in free space mode. |
| `boolean` | `isRestrictedAisleAccess()` | If enabled, you can specify maximum number of allowed transporters in each aisle of the storage. |
| `boolean` | `isSimplifiedAgentAnimation()` | Returns `true` if stored agent animation is replaced with cell color indication, otherwise returns `false`. |
| `boolean` | `isSingleUnitFirst()` |  |
| `boolean` | `isSpecifiedInslotSpeed()` | Returns `true` if specific in-slot speed was enabled and `false` otherwise. |
| `boolean` | `isUnitAccessibleFromLeftAdd(int unit)` |  |
| `boolean` | `isUnitAccessibleFromLeftRemove(int unit)` |  |
| `boolean` | `isUnitAccessibleFromRightAdd(int unit)` |  |
| `boolean` | `isUnitAccessibleFromRightRemove(int unit)` |  |
| `void` | `muteCallbacks(boolean areCallbacksMuted)` |  |
| `int` | `nFreeCells()` | Returns the number of free cells. |
| `int` | `nFreeCells(int rack)` | Returns the number of free cells in the specified rack. |
| `int` | `nFreeCells(int rack, int bay)` | Returns the number of free cells in the specified bay. |
| `int` | `nFreeCells(int rack, int bay, int shelf)` | Returns the number of free cells in the specified slot Can be called only after markup initialization. |
| `int` | `nReservedCells()` | Returns the number of reserved (but not occupied) cells. |
| `int` | `nRetrieved()` | Returns the total number of retrieved agents. |
| `int` | `nStored()` | Returns the total number of stored agents. |
| `void` | `onAgentRetrieval(Agent agent, StorageCell cell)` | Calls the storage's `onAgentRetrieval` callback code |
| `void` | `onAgentStorage(Agent agent, StorageCell cell)` | Calls the storage's `onAgentStorage` callback code |
| `List<StorageCell>` | `reservedCells(int rack, int bay)` | Returns a list of reserved cells located in the specified bay. |
| `List<StorageCell>` | `reservedCells(int rack, int bay, int shelf)` | Returns a list of reserved cells located in the specified slot. |
| `void` | `resetStats()` | Resets statistics: the number of stored agents and the number of retrieved agents. |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `retrieve(int rack)` | Retrieves and returns the next agent from the specified rack. |
| `Agent` | `retrieve(int rack, int bay)` | Retrieves and returns the next agent from the specified bay. |
| `Agent` | `retrieve(int rack, int bay, int shelf)` | Retrieves and returns the next agent from the specified slot. |
| `Agent` | `retrieve(Agent agent)` | Retrieves and returns the previously stored agent from the storage. |
| `void` | `setAccessZone(double zoneWidth, LengthUnits units)` | Sets the width of access zone in specified length units. |
| `void` | `setAisleCapacityRestriction(int maxNumber)` | Sets maximum number of allowed transporters is the storage aisles. |
| `void` | `setAisleWidth(double aisleWidth, LengthUnits units)` | Sets the aisle width in specified length units. |
| `void` | `setCellWidth(double cellWidth, LengthUnits units)` | Sets the cell width in specified length units. |
| `void` | `setFrameColor(Color frameColor)` | Sets the color of rack frame. |
| `void` | `setIgnoreCellAccessibility(boolean ignore)` |  |
| `void` | `setInslotSpeed(double speed, SpeedUnits units)` | Sets in-slot speed in specified speed units |
| `void` | `setNumberOfBays(int numberOfBays)` | Sets the number of bays per rack. |
| `void` | `setNumberOfCellsPerSlot(int numberOfCells)` | Sets number of cells per slot. |
| `void` | `setNumberOfRacks(int numberOfRacks)` | Sets the number of racks. |
| `void` | `setNumberOfShelves(int numberOfShelves)` | Sets number of shelves per rack. |
| `void` | `setObstacle(boolean isObstacle)` | Sets the racks of this storage as obstacles for transporters moving in free space mode. |
| `void` | `setPlaceOddSingleRack(RackOddSingleRackSide side)` | Sets the side of the stand alone rack in case of an odd number of racks. |
| `void` | `setPlaceSingleRacksAtSides(boolean placeSingleRacksAtSides)` | Places stand-alone racks at the sides of the storage. |
| `void` | `setRackDepth(double rackDepth, LengthUnits units)` | Sets the rack depth in specified length units. |
| `void` | `setRackPlacement(RackPlacement rackPlacement)` | Defines rack placement. |
| `void` | `setRackType(RackType type)` | Sets the rack type. |
| `void` | `setReservation(Agent agent, int rack, int bay)` | Reserves a cell for the specified agent in the specified bay. |
| `void` | `setReservation(Agent agent, int rack, int bay, int shelf)` | Reserves a cell for the specified agent in the specified slot. |
| `void` | `setReservation(Agent agent, StorageSlot slot)` | Reserves a cell for the specified agent in the specified slot. |
| `void` | `setRestrictedAisleAccess(boolean restricted)` | Enables possibility to specify maximum number of allowed transporters in each aisle of the storage. |
| `void` | `setReverseLoadingDirection(boolean reversed)` | Sets value of parameter 'Reverse loading direction'. |
| `void` | `setRotation(double rotation)` | Sets the rotation of the storage. |
| `void` | `setShelfHeight(double shelfHeight, LengthUnits units)` | Sets the z-height of a shelf in specified length units. |
| `void` | `setShelvesColor(Color shelvesColor)` | Sets the color of rack shelves. |
| `void` | `setShelvesTiltAngle(double tiltAngle)` | Sets the tilt angle of shelves. |
| `void` | `setSimplifiedAgentAnimation(boolean simplifiedAgentAnimation)` | Controls the way the stored agents are drawn. |
| `void` | `setSpecifiedInslotSpeed(boolean enabled)` | Enables specific in-slot speed if the argument is `true` and disables if the argument is `false`. |
| `void` | `setStorageSystem(RackUnitAggregator rs)` |  |
| `void` | `setX(double x)` | Sets the X coordinate of this storage. |
| `void` | `setY(double y)` | Sets the Y coordinate of this storage. |
| `void` | `setZ(double z)` | Sets the Z coordinate of this storage. |
| `int` | `size()` | Returns the number of stored agents. |
| `void` | `store(Agent agent)` | Stores the given agent in the storage. |
| `void` | `store(Agent agent, int rack)` | Stores the agent in the specified rack. |
| `void` | `store(Agent agent, int rack, int bay)` | Stores the agent in the specified bay. |
| `void` | `store(Agent agent, int rack, int bay, int shelf)` | Stores the agent in the specified slot. |
| `void` | `store(Agent agent, StorageSlot slot)` | Stores the agent in the specified slot. |
| `boolean` | `unitHasAvailableCells(int unit, Agent agent)` |  |
| `void` | `updateColorMap(int unit, int bay, int level, int deepPosition, Color color)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
| `double` | `utilization()` | Returns the storage's utilization. |
