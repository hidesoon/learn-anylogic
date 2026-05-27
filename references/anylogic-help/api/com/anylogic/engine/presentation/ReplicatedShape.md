*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ReplicatedShape.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ReplicatedShape<T extends Shape>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.ReplicatedShape<T>

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`, `Iterable<T>`

---

```
public abstract class ReplicatedShape<T extends Shape>
extends Object
implements Serializable, Cloneable, com.anylogic.engine.internal.Child, SVGElement, UsdElement, Iterable<T>, LevelElement
```

Persistent replicated shape - a container for a number of shapes of the
same type but possibly different properties. Both the number of shapes
and their properties may change dynamically.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ReplicatedShape)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ReplicatedShape()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final ReplicatedShape<T>` | `clone()` | Creates and returns a copy of this replicated shape (i.e. |
| `boolean` | `contains(double px, double py)` | Tests if any of the shapes in this replicated shape contains the point with the given coordinates |
| `int` | `createShapes()` | Creates missing and removes redundant shapes so that current number of shapes in this replicated shape equals value returned by [`getReplication()`](#getReplication()) |
| `abstract T` | `createShapeWithStaticProperties_xjal(int index)` | Creates a new shape with static properties already set. |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `T` | `get(int i)` | Returns the shape with the given index.  Number of shapes is maintained to be equal with [`getReplication()`](#getReplication()): shapes are created/deleted automatically during frame drawing requests or by explicit [`createShapes()`](#createShapes()) call. |
| `ShapeGroup` | `getGroup()` | Returns the group containing this replicated shape. |
| `Shape` | `getGroupOrOwner()` |  |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `long` | `getOrGenerateUSDId()` |  |
| `Presentable` | `getPresentable()` |  |
| `abstract int` | `getReplication()` | Returns the current number of shapes in replicated shape. |
| `abstract Class<T>` | `getShapeClass()` | Returns the class of shapes in replicated shape. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `long` | `getSVGId()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `indexOf(T shape)` | Returns the index of a given shape in this replicated shape. |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Iterator<T>` | `iterator()` | Returns iterator over shapes created so far.  Number of shapes is maintained to be equal with [`getReplication()`](#getReplication()): shapes are created/deleted automatically during frame drawing requests or by explicit [`createShapes()`](#createShapes()) call. |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setShapeDynamicProperties_xjal(T shape, int index)` | Sets the dynamic properties of a shape with the given index. |
| `int` | `size()` | Returns the current number of shapes, which may not always equal to what is returned by getReplication(). |
| `Stream<T>` | `stream()` |  |
| `final void` | `updateDynamicPropertiesStructural(boolean publicOnly)` | Updates dynamic properties of the replicated shape in a given context, adding and removing the shapes as needed. |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> commands, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
