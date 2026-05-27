*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractMarkup.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractMarkup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.AbstractMarkup

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `GISMarkupElement`, `MarkupShape`

---

```
@AnyLogicInternalAPI
public abstract class AbstractMarkup
extends Object
implements Serializable, SVGElement, UsdElement, AggregatableAnimationElement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractMarkup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractMarkup()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `discardOwner()` |  |
| `abstract RuntimeException` | `error(String errorMessage)` |  |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeDrawMode` | `getDrawMode()` | Returns the draw mode for this markup element.  Either it is drawn in 2D animation only, or in 3D only, or both in 2D and 3D. |
| `Shape` | `getGroupOrOwner()` |  |
| `ShapeInspect` | `getInspect()` |  |
| `String` | `getInspectionWindowString()` | Returns string for inspection window content |
| `String` | `getName()` | If the markup shape is declared as field in an agent class, e.g. |
| `long` | `getOrGenerateUSDId()` |  |
| `abstract Agent` | `getSpace()` | Returns the agent where the markup element is defined |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `long` | `getSVGId()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final void` | `initializeInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isPublic()` | Tests if the markup is public, i.e. |
| `boolean` | `isVisible()` | Returns the visibility of the markup element. |
| `void` | `onAggregatorInitialized()` |  |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `abstract void` | `remove()` | Removes the markup element from the presentation, if it is not a part of the presentation, does nothing. |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setInspect(ShapeInspect inspect)` |  |
| `void` | `setVisible(boolean v)` | Sets the visibility of the markup element. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
