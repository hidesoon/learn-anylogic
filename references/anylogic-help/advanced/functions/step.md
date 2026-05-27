*来源 (Source): <https://anylogic.help/advanced/functions/step.html>*

---

# step

* [Example](#example)

step(double height, double stepTime)

Returns 0 until the stepTime and then returns height.

The plot below illustrates how the function works:

![](https://anylogic.help/advanced/functions/images/step.png)

#### Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | height | double | The height of the step. |
    | stepTime | double | The time of the step. |

#### Result
:   | Type | Description |
    | --- | --- |
    | double | 0 until the stepTime and then returns height. |

#### Units

height — [units](https://anylogic.help/anylogic/system-dynamics/units.html)

stepTime — time

step() — [units](https://anylogic.help/anylogic/system-dynamics/units.html)

## Example

You can study the **Multiplier Simul Eqns** example model to understand the function usage. The step() function is used in the formula of the GovernmentExpenditure dynamic variable: **GovernmentExpenditure =** 90 + step( 10, 1 ). If you run the model and switch to the **Graphs** page, you will see how the step logic affects the system behavior at the time 1.

[**Demo model:**

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/bfa42be4-8f32-4cac-a7e5-2e5e79756996?mode=SETTINGS)
[**Demo model:** Open the model in your AnyLogic desktop installation.](alp:)
