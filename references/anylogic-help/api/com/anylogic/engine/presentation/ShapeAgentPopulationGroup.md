*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeAgentPopulationGroup.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeAgentPopulationGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeGroup](ShapeGroup.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeAgentPopulationGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeAgentPopulationGroup
extends ShapeGroup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeAgentPopulationGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeAgentPopulationGroup(Agent presentable, ShapeDrawMode drawMode, boolean ispublic, AgentList<?> population)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(int shape)` | Deprecated. This function is deprecated and will be removed in the next release |
| `void` | `add(Camera3D camera)` | Deprecated. |
| `void` | `add(Light3D light)` | Deprecated. |
| `void` | `add(ReplicatedShape<?> rshape)` | Deprecated. |
| `void` | `add(Shape shape)` | Deprecated. |
| `void` | `clear()` | Deprecated. |
| `void` | `createShapes()` | Creates missing and removes redundant shapes so that current number of shapes in this replicated shape equals value returned by `#getReplication()` |
| `ShapeEmbeddedObjectPresentation` | `createShapeWithStaticProperties_xjal(Agent agent, int index)` | Creates a new shape with static properties already set. |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Object` | `get(int i)` | Deprecated. |
| `ShapeEmbeddedObjectPresentation` | `get(Agent a)` | Returns the embedded presentation shape shape of the given agent. |
| `Iterable<Agent>` | `getAgents_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* Returns the unsorted collection of agents - may be inconsistent with the real population state because of shape update sequence |
| `Iterator<Agent>` | `getAgentsIterator_xjal()` |  |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `int` | `indexOf(Object shape)` | Deprecated. |
| `void` | `initialize_xjal(Object... contents)` | Deprecated. |
| `void` | `insert(int index, int shape)` | Deprecated. This function is deprecated and will be removed in the next release |
| `void` | `insert(int index, ReplicatedShape<?> rshape)` | Deprecated. |
| `void` | `insert(int index, Shape shape)` | Deprecated. |
| `boolean` | `isVisibleCurrently()` | Takes into account visibility of the [`Level`](../markup/Level.md "class in com.anylogic.engine.markup") |
| `boolean` | `remove(int shape)` | Deprecated. This function is deprecated and will be removed in the next release |
| `boolean` | `remove(Camera3D camera)` | Deprecated. |
| `boolean` | `remove(Light3D light)` | Deprecated. |
| `boolean` | `remove(ReplicatedShape<?> rshape)` | Deprecated. |
| `boolean` | `remove(Shape shape)` | Deprecated. |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `setShapeDynamicProperties_xjal(ShapeEmbeddedObjectPresentation shape, int index)` | Sets the dynamic properties of a shape with the given index. |
| `int` | `size()` | Returns the number of shapes in the group. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
