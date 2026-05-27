*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/ConsoleItemPrintStream.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Class ConsoleItemPrintStream

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.io.OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html "class or interface in java.io")

[java.io.FilterOutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FilterOutputStream.html "class or interface in java.io")

[java.io.PrintStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/PrintStream.html "class or interface in java.io")

com.anylogic.engine.gui.ConsoleItemPrintStream

All Implemented Interfaces:
:   `Closeable`, `Flushable`, `Appendable`, `AutoCloseable`

---

```
@AnyLogicInternalAPI
public class ConsoleItemPrintStream
extends PrintStream
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `PrintStream` | `append(char c)` |  |
| `PrintStream` | `append(CharSequence csq)` |  |
| `PrintStream` | `append(CharSequence csq, int start, int end)` |  |
| `boolean` | `checkError()` |  |
| `void` | `close()` |  |
| `void` | `flush()` |  |
| `PrintStream` | `format(String format, Object... args)` |  |
| `PrintStream` | `format(Locale l, String format, Object... args)` |  |
| `static Color` | `getColorAndSet(PrintStream out, Color color)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `print(boolean b)` |  |
| `void` | `print(char c)` |  |
| `void` | `print(char[] s)` |  |
| `void` | `print(double d)` |  |
| `void` | `print(float f)` |  |
| `void` | `print(int i)` |  |
| `void` | `print(long l)` |  |
| `void` | `print(Object obj)` |  |
| `void` | `print(String s)` |  |
| `PrintStream` | `printf(String format, Object... args)` |  |
| `PrintStream` | `printf(Locale l, String format, Object... args)` |  |
| `void` | `println()` |  |
| `void` | `println(boolean x)` |  |
| `void` | `println(char x)` |  |
| `void` | `println(char[] x)` |  |
| `void` | `println(double x)` |  |
| `void` | `println(float x)` |  |
| `void` | `println(int x)` |  |
| `void` | `println(long x)` |  |
| `void` | `println(Object x)` |  |
| `void` | `println(String x)` |  |
| `void` | `setColor(Color color)` |  |
| `static void` | `setColor(PrintStream out, Color color)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `write(byte[] b)` |  |
| `void` | `write(byte[] buf, int off, int len)` |  |
| `void` | `write(int b)` |  |
