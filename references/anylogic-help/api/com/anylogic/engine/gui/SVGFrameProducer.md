*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/SVGFrameProducer.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Class SVGFrameProducer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gui.SVGFrameProducer

---

```
@AnyLogicInternalAPI
public class SVGFrameProducer
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SVGFrameProducer()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addCommand(SVGCommand command)` | Should be accessed from model synchronized section only |
| `void` | `clearCoordinatesCache()` |  |
| `long` | `generateNewId()` |  |
| `SVGFrame` | `getFrame(Experiment<?> experiment, Presentable presentable, boolean fullFrame)` |  |
| `SVGFrame` | `getProgressOnlyFrame(Experiment<?> experiment)` |  |
| `com.anylogic.engine.internal.presentation.SVGAnimationShape3DObjectPositionWatcher` | `getShape3DObjectPositionWatcher()` |  |
| `com.anylogic.engine.internal.presentation.ShapeInspectPositionWatcher` | `getShapeInspectPositionWatcher()` |  |
| `void` | `navigateTo(NavigationPoint navigationPoint)` |  |
| `void` | `onError(Throwable t)` |  |
| `void` | `postInformationCommand(String type, String[] att, String[] val)` |  |
| `void` | `setBackEnabled(boolean backEnabled)` |  |
