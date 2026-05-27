*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/SDIntegrationManager.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class SDIntegrationManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.SDIntegrationManager

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalCodegenAPI
public class SDIntegrationManager
extends Object
implements Serializable
```

This class solves a system of algebraic differential equations.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.SDIntegrationManager)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SDIntegrationManager(int mathDiffEqCount, int mathAlgEqCount, int mathFormEqCount)` | Constructor |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `doStep(Agent ao, double currentTime, double TOUT, boolean initialConditionsSolving)` | Does integration step for the given agent |
| `int` | `FEX(double T, double[] D, double[] A, double[] RD, double[] RA)` |  |
| `int` | `SOLOUT(double time, double[] y, double[] x)` |  |
