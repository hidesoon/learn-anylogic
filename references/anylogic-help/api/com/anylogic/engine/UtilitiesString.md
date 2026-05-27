*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesString.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface UtilitiesString

All Known Implementing Classes:
:   `Agent`, `Experiment`, `ExperimentCompareRuns`, `ExperimentMultipleRuns`, `ExperimentOptimization`, `ExperimentParamVariation`, `ExperimentRunFast`, `ExperimentSimulation`, `FlowchartBlock`, `Utilities`

---

```
public interface UtilitiesString
```

Various string utilities, e.g. number formatting.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static String` | `format(boolean value)` | Formats a boolean value |
| `static String` | `format(char value)` | Formats a character to [`String`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") |
| `static String` | `format(double value)` | Formats a double value using the default AnyLogic formatter |
| `static String` | `format(double value, IUnits<?> units)` | Formats a double value with units, using the default AnyLogic formatter |
| `static String` | `format(int value)` | Formats an integer value using the default AnyLogic formatter |
| `static String` | `format(long value)` | Formats a long value using the default AnyLogic formatter |
| `static String` | `format(Date date)` | Formats a date using the default AnyLogic formatter |
| `static String` | `formatAmountUnits(double value, AmountUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatDayOfWeek(int dayOfWeek, boolean fullName)` | Returns the full or short name of the weekday |
| `static String` | `formatFlowRateUnits(double value, FlowRateUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatLengthUnits(double value, LengthUnits units)` | Converts value to required units and turns it into String |
| `static String` | `formatLengthUnits(LengthUnits unit, boolean fullName)` | Returns the full or short name of the length units |
| `static String` | `formatMonth(int month, boolean fullName)` | Returns the full or short name of the month |
| `static String` | `formatSpeedUnits(double value, SpeedUnits units)` | Converts value to required units and turns it into String |
| `static int` | `parseInt(String text)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Inverse operation of [`format(int)`](#format(long)) |
