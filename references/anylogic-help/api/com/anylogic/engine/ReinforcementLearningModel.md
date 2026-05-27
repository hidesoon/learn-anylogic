*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ReinforcementLearningModel.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ReinforcementLearningModel<ROOT extends Agent,O,A,C>

All Known Implementing Classes:
:   `ExperimentReinforcementLearning`

---

```
public interface ReinforcementLearningModel<ROOT extends Agent,O,A,C>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ROOT` | `createModel()` | Is called to obtain a new pre-initialized top-level agent. |
| `ReinforcementLearningDataAccessor<ROOT,O,A,C>` | `getDataAccessor()` | This method must be defined in a subclass |
