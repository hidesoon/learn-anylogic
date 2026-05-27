*来源 (Source): <https://anylogic.help/advanced/debug/runtime-errors.html>*

---

# Runtime errors

[Checking model syntax](checking-model-syntax.md)[Custom error handler](custom-error-handler.md)

Various errors may occur during the model execution. Runtime errors can be of two types:

* Java exceptions
* Simulation errors

You can [throw runtime error](#throwing-runtime-errors) and terminate model execution as a reaction to different undesirable occurrences.

#### Java exceptions

Java code written by the user may contain unintentional errors like computational errors in expressions specified by the user (division by zero, or square root of a negative value), accessing null pointer and so on. Such errors are detected by Java runtime environment. If such an error occurs, Java throws an exception.

#### Simulation errors

Simulation errors are logical errors of model execution. For example, if a statechart is unable to exit a branch because all exiting transitions are closed, it is a simulation error. Simulation errors are detected by AnyLogic rather than by Java runtime environment. If a simulation error occurs, AnyLogic stops the model and notifies the user with an error message.

#### Throwing runtime errors

You can debug your model at runtime by throwing runtime errors as a reaction to undesirable occurrences using the function error() of the class [Engine](https://anylogic.help/api/com/anylogic/engine/Engine.html). The error() function throws runtime exception to the simulation engine.
