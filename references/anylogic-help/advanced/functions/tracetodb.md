*来源 (Source): <https://anylogic.help/advanced/functions/tracetodb.html>*

---

# traceToDB

* [traceToDB(Object o)](#tracetodbobject-o)
* [traceToDB(String textFormat, Object… args)](#tracetodbstring-textformat-object-args)

### traceToDB(Object o)

Description
:   Prints a string representation of an object to the **trace\_log** [model execution log](https://anylogic.help/anylogic/connectivity/logs.html).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | o | java.lang.Object | the object to print |

### traceToDB(String textFormat, Object... args)

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | textFormat | String | A [format string](https://docs.oracle.com/javase/9/docs/api/java/util/Formatter.html#syntax) |
    | o | java.lang.Object | the object to print |

Description
:   The same as traceToDB(Object) but allows text format syntax like in String.format(String, Object...) function.
