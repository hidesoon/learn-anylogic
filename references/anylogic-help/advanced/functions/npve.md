*来源 (Source): <https://anylogic.help/advanced/functions/npve.html>*

---

# npve

npve(stream, discountRate, initialValue, factor, timeStep)
is the system dynamics function that returns the net present value of
stream computed using
discountRate. The computation done assumes
that the stream is valued at the end of the
period and that the discount rate is intended as a discrete period rate.

The plot on the figure below illustrates how the delay function works:

![](https://anylogic.help/anylogic/system-dynamics/images/clip0025.png)

This function can be called in formulas of system dynamics variables.

#### Units

stream — [unit](https://anylogic.help/anylogic/system-dynamics/units.html)

discountRate — 1/time

initialValue — [unit](https://anylogic.help/anylogic/system-dynamics/units.html)\*time

factor — dimensionless

timeStep — time

npve() — [unit](https://anylogic.help/anylogic/system-dynamics/units.html)\*time
