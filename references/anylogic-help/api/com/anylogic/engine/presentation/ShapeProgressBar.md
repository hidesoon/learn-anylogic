*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeProgressBar.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeProgressBar

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeProgressBar

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeProgressBar
extends ShapeInputControl
```

Progress bar control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeProgressBar)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeProgressBar(Presentable p, boolean ispublic, double x, double y, double width, double height, boolean vertical, double min, double max)` | Creates a persistent progress bar control. |
| `ShapeProgressBar(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, boolean vertical, double min, double max)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final void` | `action()` | Does nothing since progress bar has no action. |
| `void` | `executeAction()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getMax()` | Returns the maximum value of the progress bar. |
| `double` | `getMin()` | Returns the minimum value of the progress bar. |
| `int` | `getPercent()` | Returns progress percents (integer value from 0 to 100) |
| `double` | `getValue()` | Returns the current value of the progress bar. |
| `void` | `setDeterminate(boolean val)` | Sets determinate property of progress bar, which determines whether the progress bar is in determinate or indeterminate mode.  An indeterminate progress bar continuously displays animation indicating that an operation of unknown length is occurring.  By default, this property is `true`. |
| `void` | `setProgressString(String val)` | Sets the String value of the progress bar. |
| `void` | `setRange(double min, double max)` | Sets the minimum and maximum values of the progress bar. |
| `void` | `setValue(double val)` | Sets the value of the progress bar. |
| `final void` | `setValueToDefault()` | Does nothing since progress bar has no default value. |
