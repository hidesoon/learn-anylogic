*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalContinuousVariable.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalContinuousVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.optimization.metal.MetalVariable](MetalVariable.md "class in com.anylogic.engine.optimization.metal")

com.anylogic.engine.optimization.metal.MetalContinuousVariable

All Implemented Interfaces:
:   `IBoundedVariable`, `IContinuousVariable`, `IVariable`

---

```
public class MetalContinuousVariable
extends MetalVariable
implements IContinuousVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalContinuousVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `getCurrentValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `double` | `getLowerBound()` |  |
| `int` | `getSolutionIndex()` |  |
| `double` | `getUpperBound()` |  |
| `boolean` | `isValid()` |  |
| `void` | `set(String name, String min, String max)` |  |
| `void` | `setMax(String bound)` |  |
| `void` | `setMin(String bound)` |  |
