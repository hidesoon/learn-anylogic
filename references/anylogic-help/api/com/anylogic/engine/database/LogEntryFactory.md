*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/LogEntryFactory.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class LogEntryFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.LogEntryFactory

---

```
@AnyLogicInternalAPI
public class LogEntryFactory
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static ILogEntry` | `agentDied(Agent agent)` | Agent have died. |
| `static ILogEntry` | `agentLogEntry(Agent agent)` | Instance of agent has been created or destroyed. |
| `static ILogEntry` | `agentMovementLogEntry(int agentId, double speed, long startTime, long stopTime)` | Log agent's movement. |
| `static ILogEntry` | `agentParametersLogEntry(Agent agent)` | Instance of agent has been created or destroyed. |
| `static ILogEntry` | `agentTypeElementLogEntry(int elementId, Agent agent, String elementName)` | Create agent type's element like state or event. |
| `static ILogEntry` | `agentTypeLogEntry(int agentTypeId, String agentTypeName)` | Agent type |
| `static ILogEntry` | `changeAgentNameLogEntry(int agentId, String newName)` | Agent changed name. |
| `static ILogEntry` | `dataSetLogEntry(Agent agent, String name, DataSet dataSet)` |  |
| `static ILogEntry` | `eventOccurredLogEntry(EventOriginator eventOriginator)` | Event have occurred. |
| `static ILogEntry` | `flowchartEntry(Agent agent, Agent block)` | Entity entered some block |
| `static ILogEntry` | `flowchartProcessStateChangedLogEntry(Agent agent, Agent block, Object activityType, long startTime)` | Entity entered some block |
| `static ILogEntry` | `fluidRatesLogEntry(Agent fluidBlock, String port, double total, double min, double max, double average)` |  |
| `static ILogEntry` | `fluidStoragesLogEntry(Agent fluidBlock, double min, double max, double average)` |  |
| `static ILogEntry` | `fluidUnitsLogEntry(Agent fluidBlock, String amountUnits, String rateUnits)` |  |
| `static ILogEntry` | `fluidUtilizationLogEntry(Agent fluidBlock, double utilization)` |  |
| `static ILogEntry` | `histogramDataLogEntry(Agent agent, String name, HistogramData h)` |  |
| `static ILogEntry` | `messageReceived(Agent agent, Agent sender, Object msg)` | Log agent's movement. |
| `static ILogEntry` | `resourcePoolUtilizationLogEntry(Agent resourcePool, double utilization, int size)` |  |
| `static ILogEntry` | `resourceUnitStateChangedLogEntry(Agent unit, Agent resourcePool, Object usageState, Object taskType, Agent agent, Agent resourceTask, long startTime)` | Resource unit changed its activity. |
| `static ILogEntry` | `resourceUnitUtilizationLogEntry(Agent unit, Agent resourcePool, double utilization)` |  |
| `static ILogEntry` | `statechartElementLogEntry(Agent agent, Statechart<?> statechart, int stateId)` |  |
| `static <T extends Enum<T> & IStatechartState<?, T>> ILogEntry` | `statechartEnterStateLogEntry(Agent agent, Statechart<T> statechart, T state)` |  |
| `static <T extends Enum<T> & IStatechartState<?, T>> ILogEntry` | `statechartExitStateLogEntry(Agent agent, Statechart<T> statechart, T state)` |  |
| `static <T extends Enum<T> & IStatechartState<?, T>> ILogEntry` | `statechartTransitionLogEntry(Agent agent, Statechart<T> statechart, Transition transition, T nextState)` | Statechart transition has happened |
| `static ILogEntry` | `statisticsContinuousLogEntry(Agent agent, String name, StatisticsContinuous statistics)` |  |
| `static ILogEntry` | `statisticsDiscreteLogEntry(Agent agent, String name, StatisticsDiscrete statistics)` |  |
| `static ILogEntry` | `traceLogEntry(Utilities utilities, String trace)` | traceToDB() was called |
