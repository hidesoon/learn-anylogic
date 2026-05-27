*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentReinforcementLearning.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentReinforcementLearning<ROOT extends Agent,O,A,C>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.ExperimentCustom](ExperimentCustom.md "class in com.anylogic.engine")

com.anylogic.engine.ExperimentReinforcementLearning<ROOT,O,A,C>

Type Parameters:
:   `ROOT` - root model agent type
:   `O` - Observation data structure type, see `#getObservation(Agent, Object)`
:   `A` - Action data structure type, see `#applyAction(Agent, Object)`
:   `C` - Configuration data structure type, see `#applyConfiguration(Agent, Object)`

All Implemented Interfaces:
:   `LearningAgentModelInterface<ROOT>`, `ReinforcementLearningModel<ROOT,O,A,C>`, `Serializable`

---

```
public abstract class ExperimentReinforcementLearning<ROOT extends Agent,O,A,C>
extends ExperimentCustom
implements ReinforcementLearningModel<ROOT,O,A,C>, LearningAgentModelInterface<ROOT>
```

Base class for Reinforcement Learning experiments.

This class serves as an interface between the model and the platform (Learning Platform) using Reinforcement Learning
to train some Learning Agent which is based on that platform (e.g. artificial neural network).
The experiment itself is platform-agnostic and speaks in general terms.
Experiment may be used in two forms:

* exported to the Learning Platform supported by AnyLogic,
* and used during simulation with
  an already trained Learning Agent (testing purpose) - together with the Learning Platform-specific connector block from the
  Reinforcement Learning Library.

The learning process depends on the specific Learning Platform.
Below, we describe an example use: it may perform several simulation runs - the sequence of so called Episodes.
The number of Episodes is determined by the Learning Platform.
Each Episode contains the following logic:
1. Get the Episode Configuration (used for model initialization) from the Learning Agent (may be absent for models which don't require specific initialization).
2. Create root model agent and initialize it using the Configuration: `#applyConfiguration(Agent, Object)`
3. Start simulation:
3.1 Check the Stop condition (if `true`, the Learning Platform will be notified about Episode termination condition)
3.2 Get Observation from the model: `#getObservation(Agent, Object)`
3.3 Pass the Observation to the Learning Agent and receive the Action (or alternative responses like Stop Episode or Stop learning)
3.4 Apply the Action to the model: `#applyAction(Agent, Object)`
3.5 Run the model until some Stepping point, which should be defined by a user event or another trigger inside the model.
To define this point, call `ExperimentReinforcementLearning.takeAction( this );`,
where `this` is an existing agent containing the event.
3.6 Repeat to 3.1

If your Learning Platform has finished learning, and you want to test your Learning Agent. To do that, add a block
from platform-specific reinforcement learning library to your root (Main) model agent, fill in the properties of that block and ensure
there is an event/code inside your model calling the code noted in the p.3.5 above. Then simply run any simulation experiment with your model.

Usage:

* Define observation, action and configuration data structure classes and corresponding methods (p.3).
* In order to define the moment when the reinforcement learning should take place, create an event or any other type action with the code described in p. 3.5 above.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentReinforcementLearning)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentReinforcementLearning()` |  |
| `ExperimentReinforcementLearning(LearningAgentInterface<O,A,C> learningAgentInterface)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ROOT` | `createModel()` | Is called to obtain a new pre-initialized top-level agent. |
| `abstract ROOT` | `createRoot(Engine engine)` | Is called to obtain a new top-level agent. |
| `Date` | `date()` | Returns the current model date with respect to the start time/date and the model time unit. |
| `void` | `initDefaultRandomNumberGenerator(Engine engine)` | This method should be overridden to initialize random number generator of the given engine  Default implementation set new random generation with random seed - for unique experiments |
| `void` | `run()` | Use [`ExperimentCustom.createEngine()`](ExperimentCustom.md#createEngine()) |
| `static void` | `takeAction(Agent agent)` | This method should be called from the user event associated with the experiment step to be performed. |
| `void` | `takeActionForModel(ROOT root)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `time()` | Returns the current model (logical) time. |
| `double` | `time(TimeUnits units)` | Returns the current model (logical) time. |
