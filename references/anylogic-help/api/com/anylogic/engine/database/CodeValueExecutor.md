*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/CodeValueExecutor.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Interface CodeValueExecutor

All Known Implementing Classes:
:   `Agent`, `Experiment`, `ExperimentCompareRuns`, `ExperimentMultipleRuns`, `ExperimentOptimization`, `ExperimentParamVariation`, `ExperimentRunFast`, `ExperimentSimulation`, `FlowchartBlock`, `Utilities`

---

```
@AnyLogicInternalAPI
public interface CodeValueExecutor
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Class containing some executable action / evaluatable expression code inside.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `<T> T` | `executeExpression(Class<T> returnType, String code, Object... argDescriptors)` | Executes/evaluates the given code, e.g. |
