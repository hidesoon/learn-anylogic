*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeModelElementsGroup.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeModelElementsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeGroup](ShapeGroup.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeModelElementsGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public final class ShapeModelElementsGroup
extends ShapeGroup
```

Shape containing/drawing model elements of agent / simulation (variables, events, flowchart blocks etc.)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeModelElementsGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeModelElementsGroup(Presentable presentable, ModelElementDescriptorUtils[] elementDescriptors, Object... iconShapes)` | Constructs a top-level presentation group with specific attributes and possibly with some content |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(Camera3D camera)` | Adds a camera to the group. |
| `void` | `add(Light3D light3d)` | Adds a light to the group. |
| `void` | `add(ReplicatedShape<?> rshape)` | Adds a replicated shape to the group. |
| `void` | `add(Shape shape)` | Adds a persistent shape to the group. |
| `void` | `addInspect(boolean showAtStartup, double x, double y, double width, double height, Presentable presentable, Object parent, String name, boolean isPublic)` |  |
| `void` | `addInspect(double x, double y, Presentable presentable, Object parent, String name, boolean showOnUpperLevel)` | Creates a new ShapeInspect on an object that belongs to a given arbitrary Presentable (not necessarily the one this shape belongs to), and adds it to this group. |
| `void` | `addInspect(double x, double y, Object inspectedObject, String name)` | Creates a new ShapeInspect and adds it to this group. |
| `static void` | `addInspect(ShapeEmbeddedObjectIcon icon, Presentable presentable)` | Is called when a (responsive) custom icon of the EO is being clicked. |
| `void` | `clear()` | Removes all shapes from the group. |
| `ShapeInspect` | `findInspect(String name)` |  |
| `Object` | `get(int i)` | Returns the shape with the given index. |
| `double` | `getIconOffsetX()` |  |
| `double` | `getIconOffsetY()` |  |
| `ShapeEmbeddedObjectIcon` | `getOwner()` | Returns the owner of this presentation if this is an agent presentation and it is embedded to another agent  This method returns `null` in case the agent is not embedded anywhere or if this is an experiment presentation |
| `List<Object>` | `getShapes()` | Returns the collection of shapes in the group (not a copy). |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `int` | `indexOf(Object shape)` | Returns the index of the specified shape (either object of class Shape, or object of class ReplicatedShape) in this group, or `-1` if this group does not contain the shape.  More formally, returns the index `i` such that `get( i ) == shape`, or `-1` if there is no such index.  Note that implementation of this method is very inefficient (has linear complexity) |
| `void` | `initialize_xjal(ModelElementDescriptorUtils[] elementDescriptors, boolean replaceAlways, boolean replaceWithNotEmpty, Object... contents)` | *This method is internal and shouldn't be called by user.*  (may be removed in the next versions) |
| `void` | `insert(int index, ReplicatedShape<?> rshape)` | Adds a replicated shape to the group at the specified index (which defines z-order of shape in 2D animation). |
| `void` | `insert(int index, Shape shape)` | Adds a persistent shape to the group at the specified index (which defines z-order of shape in 2D animation). |
| `boolean` | `remove(Camera3D camera)` | Tries to remove a camera from the group, returns `false` if the camera was not contained. |
| `boolean` | `remove(Light3D light3d)` | Tries to remove a light from the group, returns `false` if the light was not contained. |
| `boolean` | `remove(ReplicatedShape<?> rshape)` | Tries to remove a replicated shape from the group, returns `false` if the shape was not contained. |
| `boolean` | `remove(Shape shape)` | Tries to remove a persistent shape from the group, returns `false` if the shape was not contained. |
| `void` | `removeInspect(String name)` |  |
| `void` | `setIconOffsets(double x, double y)` |  |
| `void` | `setOwner_xjal(ShapeEmbeddedObjectIcon owner)` | *This method shouldn't be called by user.*  It is public due to technical reasons |
| `int` | `size()` | Returns the number of shapes in the group. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
