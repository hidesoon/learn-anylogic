*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentDiscrete.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentDiscrete

All Superinterfaces:
:   `AgentExtension`, `ExtEnvironmentInteractive`, `ExtEnvironmentWithLayout`, `ExtWithSpaceType`, `Serializable`

---

```
public interface ExtEnvironmentDiscrete
extends ExtEnvironmentInteractive, ExtEnvironmentWithLayout, ExtWithSpaceType
```

Agent environment extension for discrete 2D space

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `cToX_xjal(int c)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `getAgentAtCell(int r, int c)` | Returns the agent located in the cell with a given row and column, or null. |
| `NeighborhoodType` | `getNeighborhoodType()` | Returns the type of neighbourhood (Euclidean, Moore) |
| `boolean` | `isCellInsideSpace(int r, int c)` |  |
| `void` | `putAgent_xjal(Agent a, int r, int c)` |  |
| `CellPosition` | `randomEmptyCell()` | Tries to find a pseudo-randomly located empty cell and return its row and column in the array with two elements.  The current implementation is 100% fairly random. |
| `double` | `rToY_xjal(int r)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setupSpace(double width, double height, int rows, int columns, NeighborhoodType neighborhoodType)` | Sets the space type to discrete with the given dimensions and neighbourhood type. |
| `double` | `spaceCellHeight()` | Returns the height of the cell in discrete space. |
| `double` | `spaceCellWidth()` | Returns the width of the cell in discrete space. |
| `int` | `spaceColumns()` | Returns the number of columns in the space. |
| `double` | `spaceHeight()` | Returns the height of environment space. |
| `int` | `spaceRows()` | Returns the number of rows in the space. |
| `double` | `spaceWidth()` | Returns the width of environment space. |
| `void` | `swapAgents_xjal(int r, int c, int r2, int c2)` |  |
