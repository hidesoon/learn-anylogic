*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalPreConstraint.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalPreConstraint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.optimization.metal.MetalConstraint](MetalConstraint.md "class in com.anylogic.engine.optimization.metal")

com.anylogic.engine.optimization.metal.MetalPreConstraint

All Implemented Interfaces:
:   `IPreConstraint`

---

```
public class MetalPreConstraint
extends MetalConstraint
implements IPreConstraint
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalPreConstraint()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getCurrentMetalValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `void` | `setType(ConstraintTypeEnum type)` |  |
