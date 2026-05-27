*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/TrafficLightDelegate.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface TrafficLightDelegate

---

```
@AnyLogicInternalAPI
public interface TrafficLightDelegate
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getCurrentPhaseElapsedTime()` | Returns time elapsed from beginning of the current phase in **model time units** or -1 if the traffic light is off |
| `int` | `getCurrentPhaseIndex()` | Returns 0-based index of the current phase, or -1 if the traffic light is off |
| `boolean` | `isOn()` | Returns `true` if the traffic light is on, `false` otherwise |
| `void` | `switchToNextPhase()` | Switches traffic light to next phase. |
| `void` | `turnOff()` | Turns off traffic light |
| `void` | `turnOn(double offset)` | Turns on traffic light with offset in **model time units** |
