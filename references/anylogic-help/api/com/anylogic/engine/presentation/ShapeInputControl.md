*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeInputControl.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeInputControl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeInputControl

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeButton`, `ShapeCheckBox`, `ShapeComboBox`, `ShapeFileChooser`, `ShapeListBox`, `ShapeProgressBar`, `ShapeRadioButtonGroup`, `ShapeSlider`, `ShapeTextField`

---

```
public abstract class ShapeInputControl
extends ShapeControl
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeInputControl)

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
