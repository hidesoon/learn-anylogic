*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IRunConfiguration.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IRunConfiguration<T extends Agent>

---

```
@AnyLogicInternalAPI
public interface IRunConfiguration<T extends Agent>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `T` | `createRootAgent(Engine engine)` |  |
| `void` | `getOutputValues(T root, IRunOutputsConsumer outputsConsumer)` |  |
| `void` | `setup(IExperimentHost experimentHost)` | Is called after the experiment is constructed. |
| `void` | `setupEngine(Engine engine)` |  |
| `void` | `setupRootParameters(T agent, boolean callOnChangeActions, IRunValueAccessor parameterSource)` | Sets agent parameters |
