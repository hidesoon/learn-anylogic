*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentDiscrete.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtAgentDiscrete

All Superinterfaces:
:   `AgentExtension`, `ExtAgentInteractive`, `ExtAnimationParams`, `ExtWithSpaceType`, `Serializable`

---

```
public interface ExtAgentDiscrete
extends ExtAgentInteractive, ExtAnimationParams, ExtWithSpaceType
```

An extension of [`Agent`](Agent.md "class in com.anylogic.engine") designed to support agent based modeling in
discrete 2D space, in particular:
- time (continuous or discrete)
- 2D discrete space
- connections between agents, networks (e.g. social) and their visualization
- communication - message passing and broadcasting

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Agent` | `getAgentAtCell(int r, int c)` | Returns the agent located in the cell with a given row and column, or null. |
| `Agent` | `getAgentNextToMe(CellDirection dir)` | Returns the agent next to this agent in a given direction, if any. |
| `int` | `getC()` | Returns the column of the agent's cell. |
| `Agent[]` | `getNeighbors()` | Returns the array of neighbor agents, subject to the current neighborhood type (Euclidean - {N,S,E,W}, Moore - also {..,NW,NW,SE,SW}) |
| `int` | `getR()` | Returns the row of the agent's cell. |
| `boolean` | `isNextCellInsideSpace(CellDirection dir)` | Returns `true` if there is an adjacent cell in a given direction. |
| `void` | `jumpToCell(int r, int c)` | Moves the agent into a cell with the given row and column. |
| `boolean` | `jumpToRandomEmptyCell()` | Finds a random empty cell and places the agent there. |
| `void` | `moveToNextCell(CellDirection dir)` | Moves the agent to an adjacent cell in a given direction. |
| `CellPosition` | `randomEmptyCell()` | Finds a pseudo-randomly located empty cell and returns its row and column in the array with two elements. |
| `void` | `setCell(int r, int c)` | Puts the agent into a given cell. |
| `void` | `setRC_xjal(int r, int c)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `swapWithAgent(Agent anotherAgent)` | Swaps the cell location of this agent with another agent. |
| `void` | `swapWithCell(int r, int c)` | Swaps this agent with an agent at the cell with the given row and column. |
| `void` | `swapWithNextCell(CellDirection dir)` | Swaps the agent with an agent at the adjacent cell in a given direction. |
