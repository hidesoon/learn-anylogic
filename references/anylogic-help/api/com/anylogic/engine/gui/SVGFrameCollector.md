*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/SVGFrameCollector.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Class SVGFrameCollector

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gui.SVGFrameCollector

---

```
@AnyLogicInternalAPI
public abstract class SVGFrameCollector
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SVGFrameCollector(IExperimentHost host)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `destroy()` |  |
| `abstract SVGFrame` | `getEmptyFrame(Runnable onStartWithMutexAcquired, Consumer<SVGFrame> onFinishWithMutexAcquired)` |  |
| `abstract SVGFrame` | `getModelFrame(boolean fullFrame, Runnable onStartWithMutexAcquired, Consumer<SVGFrame> onFinishWithMutexAcquired)` |  |
| `AnimationPacket` | `getUpdate(boolean fullFrame)` |  |
