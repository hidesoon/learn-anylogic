*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISMarkupElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISMarkupElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISMarkupElement

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `INetworkMarkupElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `GISNode`, `GISRoute`

---

```
public abstract class GISMarkupElement
extends AbstractMarkup
implements INetworkMarkupElement, Serializable
```

Basic GIS markup element could be a part of `GISNetwork`.
GIS map is able to draw GIS markup element in geographic coordinate system (latitude, longitude).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISMarkupElement)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `discardOwner()` |  |
| `RuntimeException` | `error(String errorText)` |  |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `LineStyle` | `getLineStyle()` | Returns the line style of the markup element: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getLineWidth()` | Returns the line width of the markup element. |
| `INetwork<GISNode,GISRoute>` | `getNetwork()` |  |
| `Agent` | `getSpace()` | Returns the agent where the markup element is defined |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `initialize()` | Prepares the object after setting parameters/adding segments.  This function should be called after setup of markup element initially created using constructor without arguments. |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `remove()` | Removes the markup element from the presentation, if it is not a part of the presentation, does nothing. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setLineStyle(LineStyle lineStyle)` | Sets the line style of the markup element: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `void` | `setLineWidth(double width)` | Sets the line width of the markup element, 0 means thinnest possible |
| `void` | `setOwner(ShapeGISMap map)` | Sets GIS map this element belongs to. |
| `void` | `setPermanent()` |  |
