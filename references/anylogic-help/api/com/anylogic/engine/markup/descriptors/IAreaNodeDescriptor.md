*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/descriptors/IAreaNodeDescriptor.html>*

---

Package [com.anylogic.engine.markup.descriptors](package-summary.md)

# Interface IAreaNodeDescriptor<T extends Agent>

All Superinterfaces:
:   `IDescriptor`, `IMarkupLibraryDescriptor`

All Known Implementing Classes:
:   `AreaNode`, `PolygonalNode`, `QueueArea`, `RectangularNode`

---

```
public interface IAreaNodeDescriptor<T extends Agent>
extends IDescriptor
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `accessRestrictionCondition(T agent)` |  |
| `AreaAccessRestrictionType` | `getAccessRestrictionType()` |  |
| `int` | `getCapacity()` |  |
| `double` | `getMaxSpeed(SpeedUnits units)` |  |
| `Class<? extends Agent>` | `getRestrictedAgentClass()` |  |
| `Schedule<Boolean>` | `getSchedule()` |  |
| `double` | `getThroughput(RateUnits units)` |  |
| `boolean` | `isAccessRestricted()` |  |
| `boolean` | `isAvoidedIfClosed()` |  |
| `boolean` | `isSpeedRestricted()` |  |
| `void` | `onClose()` |  |
| `void` | `onEnter(T agent)` |  |
| `void` | `onEnterDenied(T agent)` |  |
| `void` | `onExit(T agent)` |  |
| `void` | `onOpen()` |  |
| `void` | `setAccessRestricted(boolean restricted)` |  |
| `void` | `setAccessRestrictionType(AreaAccessRestrictionType restrictionType)` |  |
| `void` | `setAvoidedIfClosed(boolean avoided)` |  |
| `void` | `setCapacity(int capacity)` |  |
| `void` | `setMaxSpeed(double speed, SpeedUnits units)` |  |
| `void` | `setRestrictedAgentClass(Class<? extends Agent> appliyngClass)` |  |
| `void` | `setSchedule(Schedule<Boolean> schedule)` |  |
| `void` | `setSpeedRestricted(boolean restricted)` |  |
| `void` | `setThroughput(double throughput, RateUnits units)` |  |
