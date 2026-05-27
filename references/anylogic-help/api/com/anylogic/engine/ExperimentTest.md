*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentTest.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentTest<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.ExperimentCustom](ExperimentCustom.md "class in com.anylogic.engine")

com.anylogic.engine.ExperimentTest<ROOT>

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public abstract class ExperimentTest<ROOT extends Agent>
extends ExperimentCustom
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentTest)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ExperimentSimulation<ROOT>` | `getSimulation()` |  |
| `void` | `run()` | Use [`ExperimentCustom.createEngine()`](ExperimentCustom.md#createEngine()) |
| `void` | `setupEngine_xjal(Engine engine)` | *This method should not be called by user* |
