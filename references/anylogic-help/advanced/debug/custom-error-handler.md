*来源 (Source): <https://anylogic.help/advanced/debug/custom-error-handler.html>*

---

# Custom error handler

[Checking model syntax](checking-model-syntax.md)[Runtime errors](runtime-errors.md)

You can define your own custom error handler by overriding the onError() function of your AnyLogic experiment.

The handler will be invoked every time an exception is thrown (in any action of transitions, events, dynamic events, etc.), the model execution is stopped and the engine is switched to the ERROR state.

To define the custom error handler

1. Add **Function** ![](https://anylogic.help/anylogic/data/images/Function_obj.gif) on the diagram of the experiment.

   Note that you define function for an experiment (e.g. Simulation), not in Main or other agent type.
2. Name the function onError.
3. In the **Arguments** section of the function's properties, add the parameter of **Type** java.lang.Throwable. The **Name** of the argument can be arbitrary, say, err.
4. In the **Function body**, define the error handler code (using Java). For example, we want to output the error information in AnyLogic Console and then automatically shut down the model. To do this, write there:

   ```
   traceln("An error occurred: " + err);
   close();
   ```
5. In the **Advanced** properties section change the type of **Access** to **public**.

   ![](https://anylogic.help/advanced/debug/images/onError.png)
