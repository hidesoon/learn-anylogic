*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Locatable2D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Locatable2D

All Known Subinterfaces:
:   `Area2D`, `Area3D`, `Locatable3D`, `Path2D`, `Path3D`, `Segment2D`, `Segment3D`

All Known Implementing Classes:
:   `BarChart`, `Chart`, `Chart1D`, `Chart1DSum`, `Chart2D`, `Chart2DPlot`, `ElevatorShaft`, `Histogram`, `Histogram2D`, `PieChart`, `Plot`, `Point`, `Position`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `Shape`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeButton`, `ShapeCAD`, `ShapeCanvas`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeControl`, `ShapeCurve`, `ShapeEmbeddedObjectIcon`, `ShapeEmbeddedObjectPresentation`, `ShapeFileChooser`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeInputControl`, `ShapeInspect`, `ShapeLine`, `ShapeLineFill`, `ShapeListBox`, `ShapeModelElementsGroup`, `ShapeModelPrimitives`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeScale`, `ShapeSlider`, `ShapeSVG`, `ShapeText`, `ShapeTextField`, `ShapeTopLevelPresentationGroup`, `ShapeWindow3D`, `StackChart`, `TimeColorChart`, `TimePlot`, `TimeStackChart`

---

```
public interface Locatable2D
```

This interface represents some point location.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getX()` | Returns the x coordinate of the location. |
| `double` | `getY()` | Returns the y coordinate of the location. |
