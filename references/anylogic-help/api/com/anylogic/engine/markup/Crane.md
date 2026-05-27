*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Crane.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Crane<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Crane<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `JibCrane`, `OverheadCrane`, `OverheadCraneBridge`

---

```
public abstract class Crane<T extends Agent>
extends AbstractLevelMarkup
implements com.anylogic.engine.markup.material_handling.IMaterialFallible, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Crane)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `fail()` | Sets the crane to `failed` state |
| `abstract Position` | `getAbsoluteHookPosition()` | Returns the current hook position as an instance of `Position` in pixels. |
| `abstract double` | `getCraneHeight()` |  |
| `abstract double` | `getCraneHeight(LengthUnits units)` |  |
| `abstract Point` | `getInitialHookPoint()` | Returns the initial hook point in **pixels**, calculated according to the crane's dimensions and converted to pixels with crane's space. |
| `abstract Point` | `getInitialHookPoint(LengthUnits units)` | Returns the initial hook point in the specified length units. |
| `double` | `getRotation()` |  |
| `abstract double` | `getStatisticsStartTime()` |  |
| `abstract double` | `getUtilization()` | Returns the crane utilization: the fraction of time the crane was operating. |
| `double` | `getX()` | Returns the X coordinate of this crane |
| `Point` | `getXYZ()` | Returns the point location of this element |
| `double` | `getY()` | Returns the Y coordinate of this crane |
| `double` | `getZ()` | Returns Z-coordinate of this crane relative to crane's level |
| `abstract boolean` | `isFailed()` | Returns `true` if the crane is failed and `false` otherwise. |
| `abstract boolean` | `isReady()` | Returns `true` if the crane is ready to work with new agent and `false` otherwise. |
| `void` | `notifyDirtyState()` | should be called by controller, when it forces the changing of markup's state |
| `abstract void` | `onLoading(T agent)` |  |
| `abstract void` | `onUnloading(T agent)` |  |
| `abstract void` | `repair()` | Repairs the crane from `failed` state |
| `abstract void` | `resetStats()` | Resets the crane utilization statistics. |
| `void` | `setX(double x)` | Sets the X coordinate of this crane |
| `void` | `setXYZ(Point point)` | Places the crane into the argument point location |
| `void` | `setY(double y)` | Sets the Y coordinate of this crane |
| `void` | `setZ(double z)` | Sets the Z coordinate of this crane |
