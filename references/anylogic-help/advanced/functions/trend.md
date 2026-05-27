*来源 (Source): <https://anylogic.help/advanced/functions/trend.html>*

---

# trend

[forecast](forecast.md)[smooth](smooth.md)

trend(input, averageTime, initialTrend) is
the system dynamics function that returns the average fractional growth
rate (negative for decline) in the input.

Analogous to the Vensim function trend, see
the detailed description in the
[Vensim Reference Manual](https://www.vensim.com/documentation/index.html?fn_trend.htm).

trend can be called in formulas of system
dynamics variables.

The plot below illustrates how the function works:

![](https://anylogic.help/anylogic/system-dynamics/images/clip0023.png)

#### Units

input — [unit](https://anylogic.help/anylogic/system-dynamics/units.html)

averageTime — time

initialTrends — 1/time

trend() — 1/time
