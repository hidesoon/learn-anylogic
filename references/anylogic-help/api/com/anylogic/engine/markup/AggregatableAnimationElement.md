*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AggregatableAnimationElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface AggregatableAnimationElement

All Known Subinterfaces:
:   `LevelElement`, `LevelMarkup`

All Known Implementing Classes:
:   `AbstractFluidMarkup`, `AbstractLevelMarkup`, `AbstractMarkup`, `AbstractRailwayMarkup`, `AbstractRoadConnectableElement`, `AbstractRoadMarkup`, `AbstractRoadPart`, `AbstractRoadSidePart`, `AbstractShapedWall`, `AbstractWall`, `AreaNode`, `BarChart`, `BulkConveyorBelt`, `BusStop`, `Camera3D`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `CircularWall`, `ConveyorCustomStation`, `ConveyorMarkupElement`, `ConveyorNetwork`, `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSimpleStation`, `ConveyorSpur`, `ConveyorStation`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `Crane`, `DensityMap`, `Elevator`, `ElevatorShaft`, `EscalatorGroup`, `GISMarkupElement`, `GISNode`, `GISPoint`, `GISRegion`, `GISRoute`, `Histogram`, `Histogram2D`, `Intersection`, `JibCrane`, `LevelGate`, `Lift`, `LiftPortImpl`, `Light3D`, `Light3D.CarHeadlight`, `Light3D.Daylight`, `Light3D.Moonlight`, `Light3D.StreetLight`, `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`, `MarkupShape`, `Network`, `NetworkMarkupElement`, `NetworkPortImpl`, `Node`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `ParkingLot`, `Path`, `Pathway`, `PedFlowStatistics`, `PieChart`, `Pipe`, `Plot`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `PositionOnTrack`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `QueueArea`, `RailwayNetwork`, `RailwaySwitch`, `RailwayTrack`, `RectangularNode`, `RectangularWall`, `ReplicatedShape`, `Road`, `RoadNetwork`, `Robot`, `ServiceBase`, `ServiceWArea`, `ServiceWLine`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `StopLine`, `Storage`, `StorageTank`, `TargetLine`, `TimeColorChart`, `TimePlot`, `TimeStackChart`, `Wall`

---

```
@AnyLogicInternalAPI
public interface AggregatableAnimationElement
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default void` | `initializeInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `default void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
