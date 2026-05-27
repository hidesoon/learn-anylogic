*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AutotestExperimentHost.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AutotestExperimentHost

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.FakeExperimentHost](FakeExperimentHost.md "class in com.anylogic.engine")

com.anylogic.engine.AutotestExperimentHost

All Implemented Interfaces:
:   `IExperimentHost`

---

```
public class AutotestExperimentHost
extends FakeExperimentHost
```

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Experiment<?>` | `getExperiment()` | Returns the experiment associated with this host. |
| `SVGFrameProducer` | `getFrameProducer()` |  |
| `void` | `logFrame()` | No need for synchronization because called in same thread with model execution |
