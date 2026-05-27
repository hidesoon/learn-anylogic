*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/TrafficLight.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class TrafficLight<T extends ISignalable>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.TrafficLight<T>

All Implemented Interfaces:
:   `Serializable`

---

```
public class TrafficLight<T extends ISignalable>
extends Object
implements Serializable
```

Traffic light controls cars movement using stop lines or lane connectors. Let's call them lines.
Each line stays in one available signal: RED, GREEN, YELLOW or GRAY (not working).
Phase of traffic light is period of time when all traffic light's lines don't change its signal.
So traffic light visually can be presented as table where rows is the signals of one line and columns is the signals
of one phase:

stopLine1 | R | G | G
stopLine2 | G | R | G
