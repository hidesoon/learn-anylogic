*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ViewArea.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ViewArea

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.ViewArea

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public final class ViewArea
extends Object
implements Serializable, com.anylogic.engine.internal.Child
```

View area class.
This element references to a particular model animation coordinates of
agent/experiment.
Provides ability of fast and convenient animation positioning in
the model animation panel (using controls on toolbar or API, see:
[`navigateTo()`](#navigateTo()), `Panel#navigateTo(ViewArea)`).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ViewArea)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ViewArea(Presentable owner, String title, double x, double y, double width, double height)` | Constructor, creates new ViewArea with specified parameters |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getHeight()` | Returns the height of the view area |
| `Presentable` | `getOwner()` | Returns agent or experiment object containing this view area. |
| `String` | `getTitle()` | Returns the title of view area (will be shown in View areas menu) |
| `double` | `getWidth()` | Returns the width of the view area |
| `double` | `getX()` | Returns the x coordinate of the view area |
| `double` | `getY()` | Returns the y coordinate of the view area |
| `void` | `navigateTo()` | Displays this view area in the model animation panel |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setHeight(double height)` | Sets the height of the view area |
| `void` | `setTitle(String title)` | Sets the title of view area (will be shown in View areas menu) |
| `void` | `setWidth(double width)` | Sets the width of the view area |
| `void` | `setX(double x)` | Sets the x coordinate of the view area |
| `void` | `setY(double y)` | Sets the y coordinate of the view area |
