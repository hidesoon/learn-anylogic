*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PalletRack.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PalletRack

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.PalletRack

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `INetworkMarkupElement`, `LevelElement`, `LevelMarkup`, `PalletRackAccess<Agent>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class PalletRack
extends NetworkMarkupElement
implements PalletRackAccess<Agent>, LevelMarkup, HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PalletRack)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final PalletRackDirection` | `PALLET_RACK_LEFT_TO_RIGHT` |  |
| `static final PalletRackDirection` | `PALLET_RACK_NO_DIRECTION` |  |
| `static final PalletRackDirection` | `PALLET_RACK_RIGHT_TO_LEFT` |  |
| `static final PalletRackType` | `PALLET_RACK_SINGLE_AISLE_LEFT` |  |
| `static final PalletRackType` | `PALLET_RACK_SINGLE_AISLE_RIGHT` |  |
| `static final PalletRackType` | `PALLET_RACK_TWO_AISLES` |  |
| `static final PalletRackType` | `PALLET_RACK_TWO_PALLET_RACKS` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PalletRack()` |  |
| `PalletRack(Agent owner)` |  |
| `PalletRack(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double x, double y, double z, double length, double depth, double depthR, double levelHeight, double rotation, PalletRackType type, PalletRackDirection direction, double aisleDepth, double aisleRDepth, double cellWidth, int nPositions, int nLevels, int nDeep, Paint fillColor, Color lineColor, int cellsBetweenLegs)` | /\*\* **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `capacity()` | Returns the total number of cell positions (all the levels and all racks, if there are two racks), which is `(1 or 2) * number of positions along row * number of deep positions * number of levels` |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(Agent entity)` | Returns `true` if the given agent is contained within this object |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `get(int row, int position, int level, int deepPosition)` | Returns the agent stored at the specified cell [row,position,level,deepPosition], or `null` if the cell is reserved or free. |
| `double` | `getAisleDepth()` |  |
| `double` | `getAisleRightDepth()` |  |
| `PalletRackApproachDirection` | `getApproachDirection(Agent entity, int rowToSearch)` | Return the approach direction to the given agent or `null` if agent is unreachable (lies deep in the cell, behind other entities) |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Agent` | `getByIndex(int index)` | Returns the stored agent with a given index. |
| `PalletRackLocation` | `getCellOf(Agent entity)` | Returns the coordinates of a cell with a given agent [row,position,level], or null if the agent is not stored here. |
| `double` | `getCellWidth()` | Returns the width of cell |
| `double` | `getDepth()` |  |
| `double` | `getDepthRight()` |  |
| `Color` | `getFillColor()` | Returns the fill color of the markup element, or `null` if markup element has no fill color or has textured fill (in this case `#getFillTexture()` should be used instead) |
| `PalletRackLocation` | `getFreeCell(boolean infront)` | Returns the array [row,position,level] with the coordinates of a free cell that is closest to either front of back of the rack system, depending on the parameter infront. |
| `double` | `getLength()` |  |
| `double` | `getLevelHeight()` |  |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `Position` | `getPositionAtCell(int row, int position, int level, int deepPosition, double offset, double depth, boolean leftAisle, Position out)` | Returns the position at the given cell |
| `Position` | `getPositionAtCellEntry(int row, int position, int level, boolean leftAisle, Position out)` | Returns the position at the given cell |
| `Position` | `getPositionInAisle(int row, int position, boolean leftAisle, Position out)` | Returns the position in the given aisle at the given cell |
| `double` | `getRotation()` |  |
| `PalletRackType` | `getType()` | Returns the type of this pallet rack |
| `double` | `getX()` |  |
| `double` | `getY()` |  |
| `double` | `getZ()` |  |
| `boolean` | `hasSpace()` | Returns `true` if there is enough space for at least one more agents |
| `boolean` | `isFree(int row, int position, int level)` | Tests if a given cell [row,position,level] is free, i.e. |
| `boolean` | `isObstacle()` |  |
| `int` | `nFree(int row, int position, int level)` | Tests if a given cell [row,position,level] is free, i.e. |
| `int` | `nReserved(int row, int position, int level)` | Tests if a given cell [row,position,level] is reserved. |
| `int` | `numberOfDeepPositions()` | Returns the number of positions in the depth of each cell |
| `int` | `numberOfLevels()` | Returns the number of levels in this pallet rack |
| `int` | `numberOfPositions()` | Returns the number of positions (cells) in one shelf. |
| `int` | `numberOfRows()` | Returns the number of rows (pallet racks).  To set this number, please use [`setType(PalletRackType)`](#setType(com.anylogic.engine.markup.PalletRackType)) |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `put(int row, int position, int level, boolean leftAisle, Agent entity)` | Puts the agent into the cell with the specified coordinates [row,position,level]. |
| `Agent` | `randomAgent()` | Returns a random agent in the rack system, or `null` if the rack system is empty. |
| `Agent` | `randomEntity()` | Deprecated. please use [`randomAgent()`](#randomAgent()) |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `release(int row, int position, int level, boolean leftAisle)` | Discards a reservation of a given cell [row,position,level]. |
| `Agent` | `remove(Agent entity)` | Removes a given agent from the rack system and returns it. |
| `Agent` | `removeFromCell(int row, int position, int level, boolean leftAisle)` | Removes the agent stored in a given cell [row,position,level] from the rack system and returns it. |
| `Agent` | `removeFromCell(PalletRackLocation location, boolean leftAisle)` | Removes the agent stored in a given cell [row,position,level] from the rack system and returns it. |
| `void` | `reserve(int row, int position, int level, boolean leftAisle)` | Marks a given cell [row,position,level] as reserved. |
| `int` | `reserved()` | Returns the number of reserved cells in the pallet rack(s). |
| `void` | `resetStats()` | Resets the statistics collected for this object. |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setAisleDepth(double aisleDepth)` |  |
| `void` | `setAisleRightDepth(double aisleRDepth)` |  |
| `void` | `setCellWidth(double cellWidth)` | Sets the width of cell |
| `void` | `setConnectedSystem_xjal(PalletRackAccess<?> connectedSystem)` |  |
| `void` | `setDepth(double depth)` |  |
| `void` | `setDepthRight(double depthR)` |  |
| `void` | `setFillColor(Color fillColor)` | Sets the fill color of the markup element. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setLength(double length)` |  |
| `void` | `setLevelHeight(double levelHeight)` |  |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `void` | `setNumberOfDeepPositions(int nDeep)` |  |
| `void` | `setNumberOfLevels(int nLevels)` | Sets the number of levels in this pallet rack |
| `void` | `setNumberOfPositions(int nPositions)` | Sets the number of positions (cells) in one shelf. |
| `void` | `setObstacle(boolean isObstacle)` |  |
| `void` | `setRotation(double rotation)` |  |
| `void` | `setType(PalletRackType type)` | Sets the type of this pallet rack |
| `void` | `setX(double x)` |  |
| `void` | `setY(double y)` |  |
| `void` | `setZ(double z)` |  |
| `int` | `size()` | Returns the number of entities inside |
| `void` | `updateColorMap(int row, int position, int level, int deepPosition, boolean put)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
