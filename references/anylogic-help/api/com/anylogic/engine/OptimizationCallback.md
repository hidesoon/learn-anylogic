*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/OptimizationCallback.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class OptimizationCallback

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.OptimizationCallback

---

```
public abstract class OptimizationCallback
extends Object
```

This class is designed for usage in optimizations performed within custom
experiments, see
[`ExperimentOptimization.createOptimization(Engine, OptimizationCallback)`](ExperimentOptimization.md#createOptimization(com.anylogic.engine.Engine,com.anylogic.engine.OptimizationCallback)).

**Usage example** (the code of custom experiment, requires
`import com.opttek.optquest.*;`):

```
 try {
        // Create Engine, initialize random number generator:
        Engine engine = createEngine();
        // Set stop time:
        engine.setStopTime(1);

        // Create optimization variable
        final COptQuestContinuousVariable v = new COptQuestContinuousVariable();
        v.SetLowerBound(0.0);
        v.SetUpperBound(100.0);

        // Create objective
        final COptQuestObjective obj = new COptQuestUserControlledObjective();
        obj.SetMinimize();

        // Create optimization engine
        final COptQuestOptimization opt = ExperimentOptimization.createOptimization(engine, new OptimizationCallback() {

                                @Override
                                public void evaluate(COptQuestOptimization optimization,
                                                COptQuestSolution solution, Engine engine) {
                                        try {
                                                // Create new top-level agent:
                                                Main root = new Main(engine, null, null);
                                                // Setup parameters of top-level agent here
                                                root.param = solution.GetVariableValue(v);
                                                // Prepare Engine for simulation:
                                                engine.start(root);
                                                // Start simulation in fast mode:
                                                engine.runFast();
                                                // Process results of simulation here
                                                solution.SetObjectiveValue(obj, root.objective);
                                                // Destroy the model:
                                                engine.stop();
                                        } catch (COptQuestException e) {
                                                traceln(e.Description());
                                        }
                                }

                                // Trace each iteration (optional!)
                                @Override
                                public void monitorStatus(COptQuestOptimization optimization,
                                                COptQuestSolution solution, Engine engine) {
                                        try {
                                                traceln(String.format(
                                                                "  %3d : %6.2f : %8.2f  -- %8.2f",
                                                                solution.GetIteration(),
                                                                solution.GetVariableValue(v),
                                                                solution.GetObjectiveValue(),
                                                                optimization.GetBestSolution() != null ? optimization
                                                                                .GetBestSolution().GetObjectiveValue(
                                                                                                obj) : Double.NaN));
                                        } catch (COptQuestException e) {
                                                traceln(e.Description());
                                        }
                                }

                        });

        // Setup optimization engine
        opt.AddVariable(v);
        opt.AddObjective(obj);
        // Set the number of iterations to run
        opt.SetMaximumIterations(500);

  // Add suggested solution (initial solution)
        COptQuestSolution suggestedSolution = opt.CreateSolution();
        suggestedSolution.SetVariableValue(v, 50.0);
        opt.AddSuggestedSolution(suggestedSolution);

        // Perform optimization
        opt.Optimize();

        // Output results
        COptQuestSolution bestSolution = opt.GetBestSolution();
        traceln("Best objective: " + format(bestSolution.GetObjectiveValue(obj)));
        traceln("Best parameter: " + format(bestSolution.GetVariableValue(v)));
 } catch (COptQuestException e) {
        traceln(e.Description());
 }
```

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   * [`ExperimentOptimization.createOptimization(Engine, OptimizationCallback)`](ExperimentOptimization.md#createOptimization(com.anylogic.engine.Engine,com.anylogic.engine.OptimizationCallback))

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OptimizationCallback()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `evaluate(com.opttek.optquest.COptQuestOptimization optimization, com.opttek.optquest.COptQuestSolution solution, Engine engine)` | This callback should evaluate a solution.  This method is called at each iteration/replication of optimization.  Please call `COptQuestVariable#GetCurrentValue()` to obtain calculated values of optimization parameters and save objective value using `COptQuestOptimization#SetCurrentObjectiveValue(double)`  The most common implementation of this method is a single simulation (using [runFast()](Engine.md#runFast())) of a newly created (each time) model agent |
| `void` | `monitorStatus(com.opttek.optquest.COptQuestOptimization optimization, com.opttek.optquest.COptQuestSolution solution, Engine engine)` | This method is called at the end of each iteration (after [`evaluate(COptQuestOptimization, COptQuestSolution, Engine)`](#evaluate(com.opttek.optquest.COptQuestOptimization,com.opttek.optquest.COptQuestSolution,com.anylogic.engine.Engine))).  When this method is called, the solution has been checked for feasibility. |
