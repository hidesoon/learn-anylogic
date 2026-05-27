*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Presentable.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Presentable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Presentable

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `Utilities`

---

```
public abstract class Presentable
extends Object
implements Serializable
```

A base for any object that can be displayed by presentation panel. Is capable
of drawing model and presentation parts of the object in a Graphics2D context
of a Panel.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Presentable)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final TextAlignment` | `ALIGNMENT_CENTER` | Text alignment type constant |
| `static final TextAlignment` | `ALIGNMENT_LEFT` | Text alignment type constant |
| `static final TextAlignment` | `ALIGNMENT_RIGHT` | Text alignment type constant |
| `static final LineArrowStyle` | `ARROW_FILLED` |  |
| `static final LineArrowStyle` | `ARROW_NONE` |  |
| `static final LineArrowStyle` | `ARROW_THIN` |  |
| `static final int` | `CAD_ANTIALIASING` | Attribute of CAD indicating that CAD should be drawn using antialiasing.  By default antialiasing is turned off for CADs. |
| `static final int` | `CAD_INVERTED` | Attribute of CAD indicating that CAD should be drawn in inverted colors.  Doesn't affect appearance of layers with custom colors (where `customLayerColors[i] != null`) |
| `static final LineStyle` | `LINE_STYLE_DASHED` |  |
| `static final LineStyle` | `LINE_STYLE_DOTTED` |  |
| `static final LineStyle` | `LINE_STYLE_SOLID` |  |
| `static final ShapeDrawMode` | `SHAPE_DRAW_2D` |  |
| `static final ShapeDrawMode` | `SHAPE_DRAW_2D3D` |  |
| `static final ShapeDrawMode` | `SHAPE_DRAW_3D` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Presentable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static Map<String,IElementDescriptor>` | `createElementDescriptors(Class<?> presentableClass)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `executeShapeControlAction(int id, int index)` | Deprecated. |
| `void` | `executeShapeControlAction(int id, int index, boolean value)` | Deprecated. |
| `void` | `executeShapeControlAction(int id, int index, double value)` | Deprecated. |
| `void` | `executeShapeControlAction(int id, int index, int value)` | Deprecated. |
| `void` | `executeShapeControlAction(int id, int index, String value)` | Deprecated. |
| `void` | `executeShapeControlAction(int id, int index, String value, String[] values)` | Deprecated. |
| `Map<String,IElementDescriptor>` | `getElementDesciptors()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `<T> T` | `getElementProperty(String elementName, String propertyName)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `abstract Engine` | `getEngine()` | Returns the simulation engine. |
| `Experiment<?>` | `getExperiment()` | Returns the experiment controlling the model execution. |
| `abstract IExperimentHost` | `getExperimentHost()` | Returns the experiment host object of the model, or some dummy object with no functionality if there is none. |
| `ShapeModelElementsGroup` | `getModelElementsShape()` |  |
| `IExperimentHost` | `getPresentation()` | Deprecated. this method will be removed in the next releases. |
| `ShapeTopLevelPresentationGroup` | `getPresentationShape()` |  |
| `boolean` | `getShapeControlDefaultValueBoolean(int id, int index)` | Deprecated. |
| `double` | `getShapeControlDefaultValueDouble(int id, int index)` | Deprecated. |
| `int` | `getShapeControlDefaultValueInt(int id, int index)` | Deprecated. |
| `String` | `getShapeControlDefaultValueString(int id, int index)` | Deprecated. |
| `int` | `getViewAreas(Map<String,ViewArea> output)` | Adds all [`ViewArea`](presentation/ViewArea.md "class in com.anylogic.engine.presentation")s of this presentable to the given map `output`, if it is not `null`.  Default implementation does nothing and returns `0`. |
| `final boolean` | `iconContains(double px, double py)` | Tests if any of the icon shapes contain the point with the coordinates (px,py). |
| `void` | `onSelectionChanged_xjal(int id, int index, int[] selectedIndices, boolean programmatically)` | Deprecated. |
| `boolean` | `onShapeClick(int id, int index, double clickx, double clicky)` | Deprecated. |
| `void` | `onShapeGroupDraw(int id, int index)` | Deprecated. |
| `final boolean` | `presentationContains(double px, double py)` | Tests if any of the presentation shapes contain the point with the coordinates (px,py). |
| `void` | `readCustomData(ObjectInputStream in)` | This method may be overridden to perform custom data reading when loading model snapshot |
| `final void` | `updateShapeDynamicProperties(boolean publicOnly)` | Updates dynamic properties of persistent presentation elements of the of the presentable object (shapes, controls, charts, and presentations of the embedded objects). |
| `void` | `writeCustomData(ObjectOutputStream out)` | This method may be overridden to perform custom data writing when saving model snapshot |
