*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalDiscreteVariable.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalDiscreteVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.optimization.metal.MetalVariable](MetalVariable.md "class in com.anylogic.engine.optimization.metal")

com.anylogic.engine.optimization.metal.MetalDiscreteVariable

All Implemented Interfaces:
:   `IBoundedVariable`, `IDiscreteVariable`, `IVariable`

---

```
public class MetalDiscreteVariable
extends MetalVariable
implements IDiscreteVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalDiscreteVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `getCurrentValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `DiscreteParameterDataType` | `getDataType()` |  |
| `int` | `getLowerBound()` |  |
| `int` | `getSolutionIndex()` |  |
| `int` | `getUpperBound()` |  |
| `boolean` | `isValid()` |  |
| `void` | `set(String name, DiscreteParameterDataType dataType, String min, String max, String step)` |  |
| `void` | `setMax(String bound)` |  |
| `void` | `setMin(String bound)` |  |
