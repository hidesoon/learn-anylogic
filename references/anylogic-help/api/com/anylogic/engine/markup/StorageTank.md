*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/StorageTank.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class StorageTank

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractFluidMarkup](AbstractFluidMarkup.md "class in com.anylogic.engine.markup")<[StorageTankDataSource](StorageTankDataSource.md "interface in com.anylogic.engine.markup")>

com.anylogic.engine.markup.StorageTank

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class StorageTank
extends AbstractFluidMarkup<StorageTankDataSource>
implements AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.StorageTank)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StorageTank()` |  |
| `StorageTank(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double diameter, double height, Paint color)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getDiameter()` | Returns the diameter of the tank |
| `double` | `getHeight()` | Returns the height of the tank |
| `double` | `getX()` | Returns the x coordinate of the tank |
| `double` | `getY()` | Returns the y coordinate of the tank |
| `double` | `getZ()` | Returns the z coordinate of the tank |
| `void` | `setDiameter(double diameter)` | Sets the diameter of the tank |
| `void` | `setHeight(double height)` | Sets the height of the tank |
| `void` | `setX(double x)` | Sets x coordinate of the tank |
| `void` | `setY(double y)` | Sets y coordinate of the tank |
| `void` | `setZ(double z)` | Sets z coordinate of the tank |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
