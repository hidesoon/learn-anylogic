*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/LevelElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface LevelElement

All Superinterfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `Serializable`

All Known Subinterfaces:
:   `LevelMarkup`

All Known Implementing Classes:
:   `AbstractFluidMarkup`, `AbstractLevelMarkup`, `AbstractShapedWall`, `AbstractWall`, `AreaNode`, `BarChart`, `BulkConveyorBelt`, `Camera3D`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `CircularWall`, `ConveyorNetwork`, `Crane`, `DensityMap`, `Elevator`, `ElevatorShaft`, `EscalatorGroup`, `Histogram`, `Histogram2D`, `JibCrane`, `LevelGate`, `Lift`, `Light3D`, `Light3D.CarHeadlight`, `Light3D.Daylight`, `Light3D.Moonlight`, `Light3D.StreetLight`, `Light3DAmbient`, `Light3DDirectional`, `Light3DPoint`, `Light3DSpot`, `Network`, `NetworkPortImpl`, `Node`, `OverheadCrane`, `OverheadCraneBridge`, `PalletRack`, `Pathway`, `PedFlowStatistics`, `PieChart`, `Pipe`, `Plot`, `PointNode`, `PolygonalNode`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `QueueArea`, `RailwayNetwork`, `RectangularNode`, `RectangularWall`, `ReplicatedShape`, `RoadNetwork`, `Robot`, `ServiceBase`, `ServiceWArea`, `ServiceWLine`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `Storage`, `StorageTank`, `TargetLine`, `TimeColorChart`, `TimePlot`, `TimeStackChart`, `Wall`

---

```
public interface LevelElement
extends HasLevel, AggregatableAnimationElement
```

Interface for all shapes and space markup elements which may be contained in a 'level',
e.g. walls, nodes, rectangles

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `setLevel(Level level)` |  |
