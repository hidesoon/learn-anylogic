*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/LevelGate.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class LevelGate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.LevelGate

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `MarkupPort`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class LevelGate
extends AbstractLevelMarkup
implements MarkupPort, HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.LevelGate)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LevelGate()` |  |
| `LevelGate(double x, double y, double dx, double dy)` |  |
| `LevelGate(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double dx, double dy)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Returns true if the gate contains the point with the given coordinates using the given distance tolerance; returns false otherwise. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Returns true if the gate contains the point with the given coordinates using the given square distance tolerance; returns false otherwise. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Point` | `getCentroid()` |  |
| `Color` | `getColor()` | Returns the color of the level gate, or null if the level gate has no color. |
| `double` | `getDx()` | Returns the end x coordinate of the gate. |
| `double` | `getDy()` | Returns the end y coordinate of the gate. |
| `Point` | `getLeft()` |  |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this markup port. |
| `Point` | `getRight()` |  |
| `double` | `getX()` | Returns the start x coordinate of the gate. |
| `Point` | `getXYZ()` |  |
| `double` | `getY()` | Returns the start y coordinate of the gate. |
| `double` | `getZ()` | *This method shouldn't be called by user  (is public due to technical reasons)* |
| `void` | `setColor(Color color)` | Sets the color of the level gate |
| `void` | `setDx(double dx)` | Sets the end x coordinate of the gate. |
| `void` | `setDy(double dy)` | Sets the end y coordinate of the gate. |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this markup port. |
| `void` | `setX(double x)` | Sets the start x coordinate of the gate. |
| `void` | `setY(double y)` | Sets the start y coordinate of the gate. |
