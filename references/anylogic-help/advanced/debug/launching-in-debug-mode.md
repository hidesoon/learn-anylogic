*来源 (Source): <https://anylogic.help/advanced/debug/launching-in-debug-mode.html>*

---

# Launching a model in debug mode

[Debug view](debug-view.md)[Inspecting values](inspecting-values.md)[Evaluating expressions](evaluating-expressions.md)[Breakpoints](breakpoints.md)

Launching a model in debug mode allows you to suspend and resume the program, inspect variables, and evaluate expressions using the debugger.

To launch a model in debug mode

1. In the **Projects** view, right-click (macOS: Ctrl + click) the experiment, which you want to launch, and choose **Debug** from the popup menu, or
   Click the arrow to the right of the **Debug** ![](https://anylogic.help/advanced/debug/images/debug_exc.png) toolbar button, or choose **Model > ![](https://anylogic.help/advanced/debug/images/debug_exc.png) Debug** from the main menu,
   and choose the experiment you want to launch from the drop-down list.
2. Your model is now launched in debug mode and the launched process appears in the [**Debug** view](debug-view.md).
3. The model will run until the breakpoint is reached. When the breakpoint is hit, execution is suspended, and AnyLogic IDE window (with the **Debug** perspective opened) is made active.
4. You can end a debugging session by allowing the model to run to completion or by terminating it.
   * You can continue to step over the code with the **Step** buttons until the model completes.
   * You can click the **Resume** ![Resume](https://anylogic.help/advanced/debug/images/resume_co.png) button to allow the model to run until the next breakpoint is encountered or until the model is completed.
   * You can click the **Terminate** ![](https://anylogic.help/anylogic/ui/images/toolbars/Stop_co.gif) button in the toolbar of the **Console** view to terminate the model.
