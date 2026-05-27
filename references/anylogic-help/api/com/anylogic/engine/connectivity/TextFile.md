*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/TextFile.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class TextFile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.connectivity.TextFile

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class TextFile
extends Object
implements Serializable, com.anylogic.engine.internal.Child
```

Text File access utility

Write mode description:
This object has following methods for writing to the file:

* `print(value)` - prints given value to the file:
  [`print(double)`](#print(double)), [`print(String)`](#print(java.lang.String)), etc.
* `println()` - prints line-separator to the file
* `println(value)` - prints given value, followed by
  line-separator, to the file: [`println(double)`](#println(double)),
  [`println(String)`](#println(java.lang.String)), etc.
* [`printf(String, Object...)`](#printf(java.lang.String,java.lang.Object...)) and
  [`printf(Locale, String, Object...)`](#printf(java.util.Locale,java.lang.String,java.lang.Object...)) - convenience methods to write a
  formatted string to the text file using the specified format string and
  arguments

Read mode description:
This object reads text file line by line. Class defines method
[`getLineNumber()`](#getLineNumber()) for getting the current line number.
By default, line numbering begins at 0. This number increments at every [line terminator](#lt) as the data is read.

A line is considered to be terminated by any one of a line
feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a line feed.

In the reading mode, on each reading method call (e.g. [`readDouble()`](#readDouble())),
TextFile advances reading position to the next value
that can be read. I.e. it reads requested data and skips all trailing
`separatorsForReading` that were specified in the constructor.

Common information:
Initially, TextFile is in 'not open' state: any
further accessor-method call (e.g. [`print(double)`](#print(double))) will open file,
i.e.

* next reading (if in [`READ`](#READ) mode) will start reading file from its
  beginning
* next writing (if in [`WRITE`](#WRITE) mode) will start rewriting or
  appending (depends on mode)

TextFile has skipping methods [`skipChars(long)`](#skipChars(long)) and
[`skipTokens(int)`](#skipTokens(int)) which may be used to skip (preliminarily known)
number of characters/tokens in the file

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.TextFile)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `TextFile.Mode` | File operations mode constants |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final TextFile.Mode` | `READ` | 'read' mode |
| `static final TextFile.Mode` | `WRITE` | 'write' mode |
| `static final TextFile.Mode` | `WRITE_APPEND` | 'write/append' mode |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TextFile(Presentable owner, String packagePrefix, TextFile.Mode mode, String fileName, String charsetName, char[] separatorsForReading)` | Creates new TextFile object based on given name of file |
| `TextFile(Presentable owner, String packagePrefix, URL url, String charsetName, char[] separatorsForReading)` | Creates new TextFile object in [`READ`](#READ) mode, based on given URL |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `canReadMore()` | Returns `true` if there is available content in the file at the [reading position](#readpos).  This method opens file for reading if it is not open.  This method is only available in [`READ`](#READ) mode |
| `void` | `close()` | Closes the read or write stream of this TextFile and releases any system resources associated with it. |
| `int` | `getLineNumber()` | Get the current line number.  This method is only available in [`READ`](#READ) mode |
| `String` | `getLocation()` | Returns the location (path) of the file.  Returns `null` if the file location hasn't been set. |
| `void` | `print(boolean b)` | Prints a boolean value. |
| `void` | `print(char c)` | Prints a character. |
| `void` | `print(char[] s)` | Prints an array of characters. |
| `void` | `print(double d)` | Prints a double-precision floating-point number. |
| `void` | `print(float f)` | Prints a floating-point number. |
| `void` | `print(int i)` | Prints an integer. |
| `void` | `print(long l)` | Prints a long integer. |
| `void` | `print(Object obj)` | Prints an object. |
| `void` | `print(String s)` | Prints a string. |
| `void` | `printf(String format, Object... args)` | A convenient method to write a formatted string to the text file using the specified format string and arguments. |
| `void` | `printf(Locale l, String format, Object... args)` | A convenient method to write a formatted string to the text file using the specified format string and arguments. |
| `void` | `println()` | Terminates the current line by writing the line separator string. |
| `void` | `println(boolean x)` | Prints a boolean value and then terminates the line. |
| `void` | `println(char x)` | Prints a character and then terminates the line. |
| `void` | `println(char[] x)` | Prints an array of characters and then terminates the line. |
| `void` | `println(double x)` | Prints a double-precision floating-point number and then terminates the line. |
| `void` | `println(float x)` | Prints a floating-point number and then terminates the line. |
| `void` | `println(int x)` | Prints an integer and then terminates the line. |
| `void` | `println(long x)` | Prints a long integer and then terminates the line. |
| `void` | `println(Object x)` | Prints an Object and then terminates the line. |
| `void` | `println(String x)` | Prints a String and then terminates the line. |
| `boolean` | `readBoolean()` | Reads boolean string `"true"` or `"false"` (with or without quotation marks) |
| `byte` | `readByte()` | Reads and returns number as byte. |
| `char` | `readChar()` | Reads and returns one character.  Throws exception if there is separator in the current reading position or current text before next separator has more than one character |
| `double` | `readDouble()` | Reads and returns a `double` value (number with floating-point and double-precision). |
| `float` | `readFloat()` | Reads and returns a `float` value (number with floating-point). |
| `int` | `readInt()` | Reads and returns an `int` value.  Int value is a number in the range [`Integer.MIN_VALUE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html#MIN_VALUE "class or interface in java.lang") ... |
| `String` | `readLine()` | Read a line of text. |
| `long` | `readLong()` | Reads and returns a `long` value.  Long value is a number in the range [`Long.MIN_VALUE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#MIN_VALUE "class or interface in java.lang") ... |
| `short` | `readShort()` | Reads and returns a `short` value.  Short value is a number in the range [`Short.MIN_VALUE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html#MIN_VALUE "class or interface in java.lang") ... |
| `String` | `readString()` | Reads and returns a `String` which contains text from current reading position (which is after previously read separator), inclusive, to the next separator character position, exclusive |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setFile(String fileName, TextFile.Mode mode)` | Sets the new file to be used with this TextFile object  If specified file differs from previously used and the latter is not closed, it will be closed  **For TextFile based on URL or on file among class resources, the only possible mode is [`READ`](#READ)** |
| `void` | `setMode(TextFile.Mode mode)` | Sets the new mode of this TextFile object  If specified mode differs from previously used and the file is not closed, it will be closed  **For TextFile based on URL or on file among class resources, the only possible mode is [`READ`](#READ)** |
| `void` | `setURL(URL url)` | Sets the new url to be used with this TextFile object  This method switches TextFile to the [`READ`](#READ) mode  If specified url differs from previously used and the stream of latter is not closed, it will be closed |
| `long` | `skipChars(long n)` | Skip characters (as well as separator characters). |
| `int` | `skipTokens(int n)` | Skips tokens (texts between separators declared in the constructor) |
| `String` | `toString()` |  |
