*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalConstraint.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalConstraint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.metal.MetalConstraint

Direct Known Subclasses:
:   `MetalPostConstraint`, `MetalPreConstraint`

---

```
public abstract class MetalConstraint
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalConstraint()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getBound()` |  |
| `abstract double` | `getCurrentMetalValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `int` | `getInternalIndex()` |  |
| `void` | `setBound(double bound)` |  |
| `void` | `setCurrentValue(double currentValue, org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `void` | `setInternalIndex(int index)` |  |
| `abstract void` | `setType(ConstraintTypeEnum type)` |  |
