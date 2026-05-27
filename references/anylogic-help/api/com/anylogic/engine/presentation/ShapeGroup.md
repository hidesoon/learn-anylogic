*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGroup.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Preview3dShapeGroup`, `Shape3DGroup`, `ShapeAgentGroup_xjal`, `ShapeAgentPopulationGroup`, `ShapeModelElementsGroup`, `ShapeTopLevelPresentationGroup`

---

```
public class ShapeGroup
extends Shape3D
implements com.anylogic.engine.internal.Child
```

Group shape. Contains a collection of shapes. Shapes may also be replicated.
The user can add, remove and change shapes in the group dynamically.
Shapes contained in a group have reference to that group.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeGroup(Presentable presentable)` | Constructs an empty group with default attributes. |
| `ShapeGroup(Presentable presentable, boolean ispublic, double x, double y, double rotation, Object... contents)` | Constructs a 2D-only group with specific attributes and possibly with some content |
| `ShapeGroup(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotationZ, Object... contents)` | Constructs a group with specific attributes and possibly with some content |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(Camera3D camera)` | Adds a camera to the group. |
| `void` | `add(Light3D light)` | Adds a light to the group. |
| `void` | `add(ReplicatedShape<?> rshape)` | Adds a replicated shape to the group. |
| `void` | `add(Shape shape)` | Adds a persistent shape to the group. |
| `void` | `clear()` | Removes all shapes from the group. |
| `ShapeGroup` | `clone()` | Creates and returns a copy of this group (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Object` | `get(int i)` | Returns the shape with the given index. |
| `Presentable` | `getPresentable()` | Returns the presentable ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this group belongs to. |
| `double` | `getRotation()` | Returns the horizontal rotation of the shape. |
| `double` | `getRotationX()` | Returns the rotation of the shape around X axis (CW from +Y to +Z). |
| `double` | `getRotationY()` | Returns the rotation of the shape around Y axis (CW from +Z to +X). |
| `double` | `getRotationZ()` | Returns the rotation of the shape around Z axis (CW from +X to +Y). |
| `List<Object>` | `getShapes()` | Returns the collection of shapes in the group (not a copy). |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `int` | `indexOf(Object shape)` | Returns the index of the specified shape (either object of class Shape, or object of class ReplicatedShape) in this group, or `-1` if this group does not contain the shape.  More formally, returns the index `i` such that `get( i ) == shape`, or `-1` if there is no such index.  Note that implementation of this method is very inefficient (has linear complexity) |
| `void` | `initialize_xjal(boolean replaceAlways, boolean replaceWithNotEmpty, Object... contents)` | *This method is internal and shouldn't be called by user.*  (may be removed in the next versions) |
| `void` | `insert(int index, ReplicatedShape<?> rshape)` | Adds a replicated shape to the group at the specified index (which defines z-order of shape in 2D animation). |
| `void` | `insert(int index, Shape shape)` | Adds a persistent shape to the group at the specified index (which defines z-order of shape in 2D animation). |
| `boolean` | `isReplicated()` |  |
| `void` | `onDraw()` | A callback called by the group before the group has drawn itself (and only if the group drawing is needed - it is visible, etc.). |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `boolean` | `remove(Camera3D camera)` | Tries to remove a camera from the group, returns `false` if the camera was not contained. |
| `boolean` | `remove(Light3D light)` | Tries to remove a light from the group, returns `false` if the light was not contained. |
| `boolean` | `remove(ReplicatedShape<?> rshape)` | Tries to remove a replicated shape from the group, returns `false` if the shape was not contained. |
| `boolean` | `remove(Shape shape)` | Tries to remove a persistent shape from the group, returns `false` if the shape was not contained. |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setReplicated(ShapeGroup origin)` |  |
| `void` | `setRotation(double rotation)` | Sets the horizontal rotation of the shape. |
| `void` | `setRotationX(double rotationX)` | Sets rotation around X axis (CW from +Y to +Z) of the shape.  Note that 2D animation of the group is shrunk only when rotated vertically, i.e. |
| `void` | `setRotationY(double rotationY)` | Sets rotation around Y axis (CW from +Z to +X) of the shape.  Note that 2D animation of the group is shrunk only when rotated vertically, i.e. |
| `void` | `setRotationZ(double rotationZ)` | Sets the rotation of the shape around Z-axis. |
| `void` | `setVisible(boolean v)` | Sets the visibility of the shape. |
| `int` | `size()` | Returns the number of shapes in the group. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
