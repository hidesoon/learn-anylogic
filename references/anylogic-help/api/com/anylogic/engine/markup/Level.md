*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Level.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Level

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

[com.anylogic.engine.markup.AbstractDrawableMarkupAggregator](AbstractDrawableMarkupAggregator.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Level

All Implemented Interfaces:
:   `Serializable`

---

```
public class Level
extends AbstractDrawableMarkupAggregator
```

Level logically groups other animation elements like shapes, space markup elements, controls and charts.
Levels operate with top-level elements, e.g. a shape inside a group knows about level from that group,
and a path inside a network knows about level from that network.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Level)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Level(Agent owner, String name, ShapeDrawMode drawMode, double z)` |  |
| `Level(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible)` |  |
| `Level(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible, LevelMarkup... markupShapes)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(LevelElement shape)` | Add shape to this level |
| `void` | `add(LevelMarkup markup)` | Add markup element to this level |
| `void` | `addAll(LevelElement... elements)` | Adds specified elements to the level. |
| `Stream<? extends AggregatableAnimationElement>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `List<AreaNode>` | `getAreas()` | Deprecated. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `List<BulkConveyorBelt>` | `getBulkConveyorBelts()` | Returns a list of all conveyor belts on this level |
| `final Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` |  |
| `List<ConveyorNetwork>` | `getConveyorNetworks()` | Returns a list of all conveyor networks on this level |
| `List<Crane<?>>` | `getCranes()` | Returns a list of all cranes on this level |
| `DensityMap` | `getDensityMap()` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |
| `DensityMap` | `getDensityMap(DensityMapType type)` | Returns the density map of a particular type from this level |
| `List<DensityMap>` | `getDensityMaps()` | Returns a list of all density maps on this level |
| `List<EscalatorGroup>` | `getEscalators()` | Returns a list of all escalator groups on this level |
| `List<LevelGate>` | `getGates()` | Returns a list of all gates on this level |
| `List<Lift<?>>` | `getLifts()` | Returns a list of all lifts on this level |
| `List<LevelMarkup>` | `getMarkups()` |  |
| `List<Network>` | `getNetworks()` | Returns a list of all networks on this level |
| `List<Node>` | `getNodes()` | Returns a list of all nodes on this level |
| `List<Obstacle>` | `getObstacles()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `List<Pathway>` | `getPathways()` | Returns a list of all pathways on this level |
| `List<PedFlowStatistics>` | `getPedFlowStatistics()` | Returns a list of all elements that collect pedestrian statistics on this level. |
| `Collection<Agent>` | `getPeds()` | Return unmodifiable list of all the pedestrians in this level. |
| `List<Pipe>` | `getPipes()` | Returns a list of all pipes on this level |
| `List<RailwayNetwork>` | `getRailwayNetworks()` | Returns a list of all railway networks on this level |
| `List<RoadNetwork>` | `getRoadNetworks()` | Returns a list of all road networks on this level |
| `List<ServiceBase<?,?>>` | `getServices()` | Returns a list of all services on this level |
| `List<Object>` | `getShapes()` | Returns the collection of shapes in the level. |
| `Agent` | `getSpace()` | Returns the space where the markup element is defined |
| `List<Storage>` | `getStorages()` | Returns a list of all storages on this level |
| `List<StorageTank>` | `getStorageTanks()` | Returns a list of all storage tanks on this level |
| `List<TargetLine>` | `getTargetLines()` | Returns a list of all target lines on this level |
| `List<AbstractWall>` | `getWalls()` | Returns a list of all walls on this level |
| `double` | `getZ()` | Returns the base level z coordinate. |
| `double` | `getZ(double x, double y)` | Returns the z coordinate of the given point |
| `void` | `initialize()` | This method finalizes creation of level. |
| `int` | `pedestriansCount()` | Returns number of pedestrians currently on this level. |
| `void` | `remove(SVGElement element)` | Tries to remove an element from the level, returns `false` if the element was not contained. |
| `void` | `setDataSource(LevelDataSource dataSource)` |  |
| `void` | `setDensityMap(DensityMap densityMap)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |
| `int` | `size()` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |
| `String` | `toString()` |  |
