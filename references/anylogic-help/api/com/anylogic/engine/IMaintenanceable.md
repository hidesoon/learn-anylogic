*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IMaintenanceable.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IMaintenanceable

All Known Subinterfaces:
:   `IMaintenanceableMarkup`

All Known Implementing Classes:
:   `Agent`, `ConveyorPath`, `ConveyorSimpleStation`, `FlowchartBlock`, `JibCrane`, `OverheadCraneBridge`

---

```
@AnyLogicInternalAPI
public interface IMaintenanceable
```

General parent interface that is implemented by {@link Agent)} AND
(transitively) by all markups that offer Downtime functionality.
It is required to generalize a Downtime block in PML library to both agents and markups.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>
