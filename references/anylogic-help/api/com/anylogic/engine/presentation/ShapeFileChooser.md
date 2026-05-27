*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeFileChooser.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeFileChooser

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeFileChooser

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeFileChooser
extends ShapeInputControl
```

File chooser control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeFileChooser)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `ShapeFileChooser.Type` | File chooser type constants |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final ShapeFileChooser.Type` | `TYPE_DOWNLOAD` |  |
| `static final ShapeFileChooser.Type` | `TYPE_UPLOAD` |  |
| `String` | `value` | Returns the currently selected file name (or empty string if no file selected) that can be accessed *in the overridden action() method*.  **Use [`getValue()`](#getValue()) to obtain the currently selected file name from other places** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeFileChooser(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, String title, ShapeFileChooser.Type type, String fileTypes, String value)` | Creates a file chooser control. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `destroy()` |  |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String` | `getTitle()` | Returns the title of the file chooser - the string always displayed in Download case and displayed before the file has been uploaded in Upload case. |
| `String` | `getValue()` | Returns the currently selected file name or empty string if no file selected |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `setTitle(String title)` | Sets the new title of the file chooser - the string always displayed in Download case and displayed before the file has been uploaded in Upload case. |
| `void` | `setValue(String fileName)` | Sets the selected filename to given `fileName`  Doesn't execute user action code |
| `void` | `setValue(String fileName, boolean callAction)` | Sets the selected filename to given `fileName`  Executes user action code (if any exists) if `callAction` parameter is `true` |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
