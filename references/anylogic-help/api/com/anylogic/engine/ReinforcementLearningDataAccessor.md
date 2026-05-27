*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ReinforcementLearningDataAccessor.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ReinforcementLearningDataAccessor<ROOT extends Agent,O,A,C>

---

```
public interface ReinforcementLearningDataAccessor<ROOT extends Agent,O,A,C>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `applyAction(ROOT root, A action)` | This method must be defined in a subclass to get the data from the given `action` object and apply it to the model (`root`).  The method is called each step of reinforcement learning / AI test loop. |
| `void` | `applyConfiguration(ROOT root, C configuration)` | This method must be defined in a subclass to get the data from the given `configuration` object and apply it as the initial setup to the model (`root`).  The method is called only once per the whole model run - at the beginning. |
| `boolean` | `checkEpisodeStopCondition(ROOT root)` | This method may be defined in a subclass to check the additional stop condition of the Episode. |
| `A` | `createAction()` | This method must be defined in a subclass - just to create new *empty* Action object |
| `C` | `createConfiguration()` | This method must be defined in a subclass - just to create new *empty* Configuration object |
| `O` | `createObservation()` | This method must be defined in a subclass - just to create new *empty* Observation object |
| `void` | `getObservation(ROOT root, O observation)` | This method must be defined in a subclass to get the data from `root` and write it to the fields of the given `observation`.  The method is called each step of reinforcement learning / AI test loop. |
