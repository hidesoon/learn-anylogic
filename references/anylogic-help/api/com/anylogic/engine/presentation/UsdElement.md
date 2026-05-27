*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/UsdElement.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Interface UsdElement

All Known Subinterfaces:
:   `AbstractPositionalMarkup`

All Known Implementing Classes:
:   `AbstractFluidMarkup`, `AbstractLevelMarkup`, `AbstractMarkup`, `AbstractRailwayMarkup`, `AbstractRoadConnectableElement`, `AbstractRoadMarkup`, `AbstractRoadPart`, `AbstractRoadSidePart`, `AbstractShapedWall`, `AbstractWall`, `AreaNode`, `BarChart`, `BulkConveyorBelt`, `BusStop`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `CircularWall`, `ConveyorCustomStation`, `ConveyorMarkupElement`, `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSimpleStation`, `ConveyorSpur`, `ConveyorStation`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `Crane`, `DensityMap`, `Elevator`, `ElevatorShaft`, `EscalatorGroup`, `GISMarkupElement`, `GISNode`, `GISPoint`, `GISRegion`, `GISRoute`, `Histogram`, `Histogram2D`, `Intersection`, `JibCrane`, `LevelGate`, `Lift`, `LiftPortImpl`, `Light3D`, `Light3D.CarHeadlight`, `Light3D.Daylight`, `Light3D.Moonlight`, `Light3D.StreetLight`, `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`, `MarkupShape`, `NetworkMarkupElement`, `NetworkPortImpl`, `Node`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `ParkingLot`, `Path`, `Pathway`, `PedFlowStatistics`, `PieChart`, `Pipe`, `Plot`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `PositionOnTrack`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `QueueArea`, `RailwaySwitch`, `RailwayTrack`, `RectangularNode`, `RectangularWall`, `ReplicatedShape`, `Road`, `Robot`, `ServiceBase`, `ServiceWArea`, `ServiceWLine`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `StopLine`, `Storage`, `StorageTank`, `TargetLine`, `TimeColorChart`, `TimePlot`, `TimeStackChart`, `Wall`

---

```
@AnyLogicInternalAPI
public interface UsdElement
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final long` | `ID_NOT_SET` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `getOrGenerateUSDId()` |  |
