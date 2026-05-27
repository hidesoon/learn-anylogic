*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesError.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class UtilitiesError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.UtilitiesError

---

```
@AnyLogicInternalAPI
public final class UtilitiesError
extends Object
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T extends Throwable> T` | `dropLastFromStack(T throwable)` | Removes last element from stack trace of the given throwable  This method may be used in private check/ensure-methods |
| `static <T extends Throwable> T` | `dropLastFromStack(T throwable, int count)` | Removes last elements from stack trace of the given throwable  This method may be used in private check/ensure-methods |
| `static RuntimeException` | `error(String errorText)` |  |
| `static RuntimeException` | `error(String errorTextFormat, Object... args)` |  |
| `static RuntimeException` | `error(Throwable cause, String errorText)` |  |
| `static RuntimeException` | `error(Throwable cause, String errorTextFormat, Object... args)` | Creates and throws new [`RuntimeException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang") with message using format syntax like in [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang") method |
| `static String` | `formatSafe(String messageFormat, Object... messageArgs)` | Safe analog of [`String.format(String, Object...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#format(java.lang.String,java.lang.Object...) "class or interface in java.lang"). |
| `static Class<?>` | `getClassSafe(Object obj)` |  |
| `static RuntimeException` | `getRuntimeException(Throwable e)` |  |
| `static void` | `processThreadDeath(Throwable e)` | Rethrows e if it is [`ThreadDeath`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ThreadDeath.html "class or interface in java.lang") |
| `static String` | `toStringSafe(Object o)` |  |
| `static String` | `toStringStackTrace(Throwable e)` |  |
| `static String` | `toStringWithCauses(Throwable e)` | Returns toString of the given throwable and all its causers |
