*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/metal/MetalDoubleMutator.html>*

---

Package [com.anylogic.engine.optimization.metal](package-summary.md)

# Class MetalDoubleMutator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.metal.MetalDoubleMutator

All Implemented Interfaces:
:   `Serializable`, `org.uma.jmetal.operator.mutation.MutationOperator<org.uma.jmetal.solution.doublesolution.DoubleSolution>`, `org.uma.jmetal.operator.Operator<org.uma.jmetal.solution.doublesolution.DoubleSolution,org.uma.jmetal.solution.doublesolution.DoubleSolution>`

---

```
public class MetalDoubleMutator
extends Object
implements org.uma.jmetal.operator.mutation.MutationOperator<org.uma.jmetal.solution.doublesolution.DoubleSolution>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.optimization.metal.MetalDoubleMutator)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalDoubleMutator(double probability, double distributionIndex)` |  |
| `MetalDoubleMutator(int nVars)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `org.uma.jmetal.solution.doublesolution.DoubleSolution` | `execute(org.uma.jmetal.solution.doublesolution.DoubleSolution solution)` |  |
| `double` | `getMutationProbability()` |  |
