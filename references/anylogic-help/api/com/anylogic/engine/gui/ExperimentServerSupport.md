*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/ExperimentServerSupport.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Class ExperimentServerSupport

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gui.ExperimentServerSupport

---

```
@AnyLogicInternalAPI
public class ExperimentServerSupport
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentServerSupport()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static IExperimentServer` | `newServer(IExperimentHost host)` |  |
| `static void` | `registerFactory(Function<IExperimentHost,IExperimentServer> factory)` |  |
