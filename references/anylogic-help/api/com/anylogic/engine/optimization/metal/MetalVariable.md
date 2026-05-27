*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalVariable.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.metal.MetalVariable

All Implemented Interfaces:
:   `IVariable`

Direct Known Subclasses:
:   `MetalBinaryVariable`, `MetalContinuousVariable`, `MetalDiscreteVariable`

---

```
public abstract class MetalVariable
extends Object
implements IVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `getBestValue()` |  |
| `double` | `getBestValueAsDouble()` |  |
| `abstract Object` | `getCurrentValue(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `double` | `getCurrentValueAsDouble(org.uma.jmetal.solution.compositesolution.CompositeSolution solution)` |  |
| `int` | `getInternalIndex()` |  |
| `String` | `getName()` |  |
| `abstract int` | `getSolutionIndex()` |  |
| `abstract boolean` | `isValid()` |  |
| `void` | `setBestValue(Object bestValue)` |  |
| `void` | `setInternalIndex(int index)` |  |
| `void` | `setName(String name)` |  |
