*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Shape3DObject.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Shape3DObject

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Shape3DObject

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class Shape3DObject
extends Shape3D
implements com.anylogic.engine.internal.Child
```

3D object shape loaded from COLLADA (.dae) file. Also visible on 2D animation (in the form of top-view).
This shape enables AnyLogic users to import ready-to-use 3D objects created in some
third-party 3D graphics packets into their models.
[COLLADA](https://en.wikipedia.org/wiki/COLLADA) format is the XML-based file format
for representing 3D computer graphics.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Shape3DObject)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Object3DAxisOrder` | `XYZ_AXIS_ORDER` | Deprecated. |
| `static final Object3DAxisOrder` | `YZX_AXIS_ORDER` | Deprecated. |
| `static final Object3DAxisOrder` | `ZXY_AXIS_ORDER` | Deprecated. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Shape3DObject(Presentable presentable, boolean ispublic, double x, double y, double z, double rotation, double scale, String packagePrefix, String fileName, Object3DAxisOrder axisOrder, boolean applyShading, double topLeftX, double topLeftY, double width, double height)` | Deprecated. this constructor is deprecated and will be removed in future releases |
| `Shape3DObject(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, double scale, boolean autoScale, String packagePrefix, String fileName, Object3DAxisOrder axisOrder, boolean applyShading, double topLeftX, double topLeftY, double width, double height)` | Deprecated. this constructor is deprecated and will be removed in future releases |
| `Shape3DObject(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, double scale, boolean autoScale, String packagePrefix, String fileName, Object3DAxisOrder axisOrder, boolean applyShading, double topLeftX, double topLeftY, double width, double height, Long imageFileId, Pair<String,Color>... customColors)` | Deprecated. this constructor is deprecated and will be deleted in future releases |
| `Shape3DObject(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, double scale, boolean autoScale, String packagePrefix, String fileName, Object3DAxisOrder axisOrder, double topLeftX, double topLeftY, double width, double height)` | Constructs a 3D shape with specific attributes. |
| `Shape3DObject(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, double scale, boolean autoScale, String packagePrefix, String fileName, Object3DAxisOrder axisOrder, Object3DInternalLighting internalLighting, boolean ignoreSceneLights, double topLeftX, double topLeftY, double width, double height, Long imageFileId, boolean visible, Pair<String,Color>... customColors)` | Constructs a 3D shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Shape3DObject` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `dispose()` | Releases resources allocated by this object, should be called on agent destroy. |
| `double` | `getAgentScalingFactor()` | Returns additional scaling factor for sizing accordingly to the Scale element on the Agent. |
| `Object3DAxisOrder` | `getAxisOrder()` |  |
| `String` | `getFilename()` | Returns the name of 3D object file |
| `String` | `getFilePath_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setColor(String materialName, Color color)` | Changes custom color for the shape material with the given name.  *Current implementation updates object on the 3D scene only, it doesn't update the 2D picture - this will be implemented in future releases.* |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
