*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentGIS.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentGIS

All Superinterfaces:
:   `AgentExtension`, `ExtEnvironmentInteractive`, `ExtEnvironmentWithMetrics`, `ExtWithSpaceType`, `Serializable`

---

```
public interface ExtEnvironmentGIS
extends ExtEnvironmentInteractive, ExtEnvironmentWithMetrics, ExtWithSpaceType
```

Agent space extension for continuous 2D space based on GIS map

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeGISMap` | `getGISMap()` | Deprecated. |
| `double` | `getNetworkConnectionRange()` | Returns the range of agent connections, it is measured in meters. |
| `void` | `setNetworkAllInRange(double connectionRange)` | Sets network type to the one when agents are connected if the distance between them is not longer that a given one. |
| `void` | `setupSpace(ShapeGISMap gisMap)` | Sets the space to be based on given `gisMap`. |
