*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/HasLevel.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface HasLevel

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `LevelElement`, `LevelMarkup`

All Known Implementing Classes:
:   `AbstractFluidMarkup`, `AbstractLevelMarkup`, `AbstractRailwayMarkup`, `AbstractRoadConnectableElement`, `AbstractRoadMarkup`, `AbstractRoadPart`, `AbstractRoadSidePart`, `AbstractShapedWall`, `AbstractWall`, `AreaNode`, `BarChart`, `BulkConveyorBelt`, `BusStop`, `Camera3D`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `CircularWall`, `ConveyorCustomStation`, `ConveyorMarkupElement`, `ConveyorNetwork`, `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSimpleStation`, `ConveyorSpur`, `ConveyorStation`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `Crane`, `DensityMap`, `Elevator`, `ElevatorShaft`, `EscalatorGroup`, `Histogram`, `Histogram2D`, `Intersection`, `JibCrane`, `LevelGate`, `Lift`, `LiftPortImpl`, `Light3D`, `Light3D.CarHeadlight`, `Light3D.Daylight`, `Light3D.Moonlight`, `Light3D.StreetLight`, `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`, `MarkupShape`, `Network`, `NetworkMarkupElement`, `NetworkPortImpl`, `Node`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `ParkingLot`, `Path`, `Pathway`, `PedFlowStatistics`, `PieChart`, `Pipe`, `Plot`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `PositionOnTrack`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `QueueArea`, `RailwayNetwork`, `RailwaySwitch`, `RailwayTrack`, `RectangularNode`, `RectangularWall`, `ReplicatedShape`, `Road`, `RoadNetwork`, `Robot`, `ServiceBase`, `ServiceWArea`, `ServiceWLine`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `StopLine`, `Storage`, `StorageTank`, `TargetLine`, `TimeColorChart`, `TimePlot`, `TimeStackChart`, `Wall`

---

```
public interface HasLevel
extends Serializable
```

Interface for all space elements which may be contained in a 'level'

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
