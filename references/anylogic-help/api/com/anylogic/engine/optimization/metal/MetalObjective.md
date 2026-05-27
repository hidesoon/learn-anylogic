*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalObjective.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalObjective

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.metal.MetalObjective

All Implemented Interfaces:
:   `IObjective`

---

```
public class MetalObjective
extends Object
implements IObjective
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalObjective()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static double` | `getCurrentMetalValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `double` | `getCurrentPublicValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `boolean` | `isMinimize()` |  |
| `void` | `setCurrentPublicValue(double publicValue, org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `void` | `setMaximize()` |  |
| `void` | `setMinimize()` |  |
