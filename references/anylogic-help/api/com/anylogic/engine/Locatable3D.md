*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Locatable3D.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface Locatable3D

All Superinterfaces:
:   `Locatable2D`

All Known Subinterfaces:
:   `Area3D`, `Path3D`, `Segment3D`

All Known Implementing Classes:
:   `ElevatorShaft`, `Preview3dShapeEmbeddedObjectPresentation`, `Preview3dShapeGroup`, `Preview3dShapeTopLevelPresentationGroup`, `Shape3D`, `Shape3DGroup`, `Shape3DObject`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeArc`, `ShapeArrowLine`, `ShapeCurve`, `ShapeEmbeddedObjectPresentation`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeLine`, `ShapeLineFill`, `ShapeModelElementsGroup`, `ShapeMultiplePoints`, `ShapeOval`, `ShapePolyLine`, `ShapeRectangle`, `ShapeRoundedRectangle`, `ShapeText`, `ShapeTopLevelPresentationGroup`

---

```
public interface Locatable3D
extends Locatable2D
```

This interface represents some location.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getZ()` | Returns the z coordinate of the location base. |
| `double` | `getZOffset()` | Returns the offset from z coordinate of the location base.  This e.g. |
