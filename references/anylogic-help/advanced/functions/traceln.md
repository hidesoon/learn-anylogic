*来源 (Source): <https://anylogic.help/advanced/functions/traceln.html>*

---

# traceln

* [traceln(Object o)](#tracelnobject-o)
* [traceln(Color color, Object o)](#tracelncolor-color-object-o)
* [traceln(String textFormat, Object… args)](#tracelnstring-textformat-object-args)
* [traceln(Color color, String textFormat, Object… args)](#tracelncolor-color-string-textformat-object-args)
* [traceln()](#traceln-2)

### traceln(Object o)

Description
:   Prints a textual representation of the specified object with a line delimiter at the end to the Console in the [developer panel](https://anylogic.help/anylogic/running/developer-panel.html).

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | o | Object | The object to print. |

### traceln(Color color, Object o)

Description
:   Prints a textual representation of the specified object with a line delimiter at the end to the Console. The text color is defined by the color argument.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | color | Color | The color of text in console. |
    | o | Object | The object to print. |

### traceln(String textFormat, Object... args)

Description
:   The same as traceln(Object o) but allows text format syntax like in String.format(String, Object...) function.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | textFormat | String | A format string |
    | o | Object | The object to print. |

### traceln(Color color, String textFormat, Object... args)

Description
:   The same as traceln(Color color, Object o) but allows text format syntax like in String.format(String, Object...) function.

Parameters
:   | Name | Type | Description |
    | --- | --- | --- |
    | color | Color | The color of text in console. |
    | textFormat | String | A [format string](https://docs.oracle.com/javase/6/docs/api/java/util/Formatter.html) |
    | o | Object | The object to print. |

### traceln()

Description
:   Prints a line delimiter to the standard output stream.

[**Demo model:** Event Writes to the Log

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/d1c79d2f-d22c-4f75-ba04-96f39085879c?mode=SETTINGS)
[**Demo model:** Event Writes to the LogOpen the model in your AnyLogic desktop installation.](alp:Event Writes to the Log)
