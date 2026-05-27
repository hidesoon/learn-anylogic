*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeTopLevelPresentationGroup.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeTopLevelPresentationGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeGroup](ShapeGroup.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeTopLevelPresentationGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Preview3dShapeTopLevelPresentationGroup`

---

```
public class ShapeTopLevelPresentationGroup
extends ShapeGroup
```

Top-level group of agent or experiment presentation

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeTopLevelPresentationGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeTopLevelPresentationGroup(Presentable presentable, boolean ispublic, double x, double y, double z, double rotationXY, Object... contents)` | Constructs a top-level presentation group with specific attributes and possibly with some content |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(Level level)` | This is a helper method to add all the markups and shapes contained in this level to this group |
| `void` | `add(MarkupShape shape)` | Adds a space markup shape to the group. |
| `Configuration3D` | `getConfiguration3D()` | Returns 3D configuration of agent.  Returns `null` for experiments. |
| `ShapeEmbeddedObjectPresentation` | `getOriginalOwner()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeEmbeddedObjectPresentation` | `getOwner()` | Returns the owner of this presentation if this is an agent presentation and it is embedded to another agent  This method returns `null` in case the agent is not embedded anywhere or if this is an experiment presentation |
| `List<Object>` | `getShapes()` | Returns the collection of shapes in the group (not a copy). |
| `void` | `insert(int index, MarkupShape shape)` | Adds a space markup to the group at the specified index (which defines z-order of shape in 2D animation). |
| `boolean` | `remove(MarkupShape shape)` | Tries to remove a space markup shape from the group, returns `false` if the shape was not contained. |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setOwner_xjal(ShapeEmbeddedObjectPresentation owner)` | *This method shouldn't be called by user.*  It is public due to technical reasons |
| `void` | `setPos(double x, double y)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setPos(double x, double y, double z)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setPos(Point p)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setRotation(double rotation)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setRotationX(double rotationX)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setRotationY(double rotationY)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setRotationZ(double rotationZ)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScale(double s)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScale(double sx, double sy)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScale(double sx, double sy, double sz)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScaleX(double sx)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScaleY(double sy)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setScaleZ(double sz)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setVisible(boolean v)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setX(double x)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setY(double y)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
| `void` | `setZ(double z)` | **This method is not supported for top-level 'presentation' group.** Please create your own group and add all the contents to that group in order to have the intended control. |
