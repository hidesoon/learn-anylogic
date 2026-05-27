*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalIntegerMutator.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalIntegerMutator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.metal.MetalIntegerMutator

All Implemented Interfaces:
:   `Serializable`, `org.uma.jmetal.operator.mutation.MutationOperator<org.uma.jmetal.solution.integersolution.IntegerSolution>`, `org.uma.jmetal.operator.Operator<org.uma.jmetal.solution.integersolution.IntegerSolution,org.uma.jmetal.solution.integersolution.IntegerSolution>`

---

```
public class MetalIntegerMutator
extends Object
implements org.uma.jmetal.operator.mutation.MutationOperator<org.uma.jmetal.solution.integersolution.IntegerSolution>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.optimization.metal.MetalIntegerMutator)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalIntegerMutator(double probability, double distributionIndex)` |  |
| `MetalIntegerMutator(int nVars)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `org.uma.jmetal.solution.integersolution.IntegerSolution` | `execute(org.uma.jmetal.solution.integersolution.IntegerSolution solution)` |  |
| `double` | `getMutationProbability()` |  |
