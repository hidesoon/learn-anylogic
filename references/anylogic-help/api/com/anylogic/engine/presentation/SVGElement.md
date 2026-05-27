*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/SVGElement.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Interface SVGElement

All Known Subinterfaces:
:   `AbstractPositionalMarkup`

All Known Implementing Classes:
:   `AbstractFluidMarkup`, `AbstractLevelMarkup`, `AbstractMarkup`, `AbstractRailwayMarkup`, `AbstractRoadConnectableElement`, `AbstractRoadMarkup`, `AbstractRoadPart`, `AbstractRoadSidePart`, `AbstractShapedWall`, `AbstractWall`, `AreaNode`, `BarChart`, `BulkConveyorBelt`, `BusStop`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `CircularWall`, `ConveyorCustomStation`, `ConveyorMarkupElement`, `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSimpleStation`, `ConveyorSpur`, `ConveyorStation`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `Crane`, `DensityMap`, `Elevator`, `ElevatorShaft`, `EscalatorGroup`, `GISMarkupElement`, `GISNode`, `GISPoint`, `GISRegion`, `GISRoute`, `Histogram`, `Histogram2D`, `Intersection`, `JibCrane`, `LevelGate`, `Lift`, `LiftPortImpl`, `Light3D`, `Light3D.CarHeadlight`, `Light3D.Daylight`, `Light3D.Moonlight`, `Light3D.StreetLight`, `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`, `MarkupShape`, `NetworkMarkupElement`, `NetworkPortImpl`, `Node`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `ParkingLot`, `Path`, `Pathway`, `PedFlowStatistics`, `PieChart`, `Pipe`, `Plot`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `PositionOnTrack`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `QueueArea`, `RailwaySwitch`, `RailwayTrack`, `RectangularNode`, `RectangularWall`, `ReplicatedShape`, `Road`, `Robot`, `ServiceBase`, `ServiceWArea`, `ServiceWLine`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `StopLine`, `Storage`, `StorageTank`, `TargetLine`, `TimeColorChart`, `TimePlot`, `TimeStackChart`, `Wall`

---

```
@AnyLogicInternalAPI
public interface SVGElement
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Shape` | `getGroupOrOwner()` |  |
| `Presentable` | `getPresentable()` |  |
| `default com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `long` | `getSVGId()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `default void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement shapeBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
