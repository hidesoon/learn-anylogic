*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentWithMetrics.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentWithMetrics

All Superinterfaces:
:   `AgentExtension`, `ExtEnvironmentInteractive`, `Serializable`

All Known Subinterfaces:
:   `ExtEnvironmentContinuous`, `ExtEnvironmentGIS`

---

```
public interface ExtEnvironmentWithMetrics
extends ExtEnvironmentInteractive
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `connectAllInRange_xjal()` |  |
| `double` | `getNetworkConnectionRange()` | Returns the range of agent connections. |
| `void` | `setNetworkAllInRange(double connectionRange)` | Sets network type to the one when agents are connected if the distance between them is not longer that a given one. |
