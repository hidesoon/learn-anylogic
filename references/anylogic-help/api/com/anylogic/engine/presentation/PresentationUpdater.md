*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/PresentationUpdater.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class PresentationUpdater

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.PresentationUpdater

---

```
@AnyLogicInternalAPI
public abstract class PresentationUpdater
extends Object
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTempCommand(SVGCommand command)` |  |
| `abstract void` | `execute(Runnable r)` |  |
| `Collection<SVGCommand>` | `getAndClearTempCommands()` |  |
| `static PresentationUpdater` | `getInstance()` |  |
| `abstract boolean` | `isActive()` |  |
| `abstract void` | `start()` |  |
| `abstract void` | `waitForFinish()` |  |
