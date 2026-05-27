*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/ExcelFile.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class ExcelFile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.connectivity.ExcelFile

All Implemented Interfaces:
:   `Serializable`

---

```
public class ExcelFile
extends Object
implements Serializable
```

Microsoft® ExcelTM File access utility

This class is a representation of a workbook.

**File access**
This class have 2 methods for the file access: [`readFile()`](#readFile()) and
[`writeFile()`](#writeFile()). Also it has ability loading another file or saving to
other location - see [`setFileName(String)`](#setFileName(java.lang.String)).

**Data access**
Data may be read from and written to a workbook using various
`getCell*(...)` and `setCell*(...)` methods. This
object allows reading table functions (`readTableFunction()`) and
hyper arrays (with 1 or 2 dimensions, see `readHyperArray`) from
the sheet. Also, data sets may be written using `writeDataSet`.
New cells may need to be created before writing data:
`createCell(...)` (cell may be checked using
`cellExists()`)

**Cell access**
All cell-access methods have 3 forms of cell location specification:

* 3 numbers (one-based): sheet index, row index, column index
* sheet name and 2 (one-based) numbers row index and column index
* cell name in the following format:
  `<sheet name>!<column name><row number>`
  The sheet name can be skipped, then the first sheet is assumed.
  Examples (without quotes):
  `"Sheet1!A3"`, `"Sheet2!AAB100"`, `"B2"`

**Model Snapshot serialization notes**
This workbook may include all unsaved data (if any) to the model snapshot -
this is controlled by parameter `saveToSnapshot` of
[constructor](#%3Cinit%3E(java.lang.String,boolean)).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.ExcelFile)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_BLANK` | Blank Cell type |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_BOOLEAN` | Boolean Cell type |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_ERROR` | Error Cell type |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_FORMULA` | Formula Cell type |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_NUMERIC` | Numeric Cell type |
| `static final org.apache.poi.ss.usermodel.CellType` | `CELL_TYPE_STRING` | String Cell type |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExcelFile(Presentable owner, String packagePrefix, String fileName, boolean saveToSnapshot)` | Creates new ExcelTM file accessor |
| `ExcelFile(String fileName, boolean saveToSnapshot)` | Deprecated. this constructor is obsolete and will be removed in future |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `cellExists(int sheetIndex, int rowIndex, int columnIndex)` | Returns `true` if the cell at the given position exists in the workbook |
| `boolean` | `cellExists(String cellName)` | Returns `true` if the cell at the given position exists in the workbook |
| `boolean` | `cellExists(String sheetName, int rowIndex, int columnIndex)` | Returns `true` if the cell at the given position exists in the workbook |
| `void` | `clearCell(int sheetIndex, int rowIndex, int columnIndex)` | Clears type and value of the cell. |
| `void` | `close()` | Closes the workbook. |
| `void` | `createCell(int sheetIndex, int rowIndex, int columnIndex)` | Creates new cell at the given position. |
| `void` | `createCell(String cellName)` | Creates new cell at the given position. |
| `void` | `createCell(String sheetName, int rowIndex, int columnIndex)` | Creates new cell at the given position. |
| `void` | `evaluateFormulas()` | Evaluates formulas and saves the results for all the cells containing formulas in this workbook.  The cells are left as formula cells. |
| `boolean` | `getCellBooleanValue(int sheetIndex, int rowIndex, int columnIndex)` | Returns the value of the cell as a `boolean`.  For strings, numbers, and errors, throws an exception.  For blank cells returns `false`. |
| `boolean` | `getCellBooleanValue(String cellName)` | Returns the value of the cell as a `boolean`.  For strings, numbers, and errors, throws an exception.  For blank cells returns `false`. |
| `boolean` | `getCellBooleanValue(String sheetName, int rowIndex, int columnIndex)` | Returns the value of the cell as a `boolean`.  For strings, numbers, and errors, throws an exception.  For blank cells returns `false`. |
| `Date` | `getCellDateValue(int sheetIndex, int rowIndex, int columnIndex)` | Returns the value of the cell as a date.  For strings throws an exception.  For blank cells returns `null`. |
| `Date` | `getCellDateValue(String cellName)` | Returns the value of the cell as a date.  For strings throws an exception.  For blank cells returns `null`. |
| `Date` | `getCellDateValue(String sheetName, int rowIndex, int columnIndex)` | Returns the value of the cell as a date.  For strings throws an exception.  For blank cells returns `null`. |
| `byte` | `getCellErrorValue(int sheetIndex, int rowIndex, int columnIndex)` | Returns the value of the cell as an error code.  For strings, numbers, and booleans, throws an exception.  For blank cells returns a `0`. |
| `byte` | `getCellErrorValue(String cellName)` | Returns the value of the cell as an error code.  For strings, numbers, and booleans, throws an exception.  For blank cells returns a `0`. |
| `byte` | `getCellErrorValue(String sheetName, int rowIndex, int columnIndex)` | Returns the value of the cell as an error code.  For strings, numbers, and booleans, throws an exception.  For blank cells returns a `0`. |
| `String` | `getCellFormula(int sheetIndex, int rowIndex, int columnIndex)` | Return a formula for the cell, for example, SUM(C4:E4) |
| `String` | `getCellFormula(String cellName)` | Return a formula for the cell, for example, SUM(C4:E4) |
| `String` | `getCellFormula(String sheetName, int rowIndex, int columnIndex)` | Return a formula for the cell, for example, SUM(C4:E4) |
| `org.apache.poi.ss.usermodel.CellType` | `getCellFormulaType(int sheetIndex, int rowIndex, int columnIndex)` | Returns the type of the formula cell.  Only valid for formula cells. |
| `org.apache.poi.ss.usermodel.CellType` | `getCellFormulaType(String cellName)` | Returns the type of the formula cell.  Only valid for formula cells. |
| `org.apache.poi.ss.usermodel.CellType` | `getCellFormulaType(String sheetName, int rowIndex, int columnIndex)` | Returns the type of the formula cell.  Only valid for formula cells. |
| `double` | `getCellNumericValue(int sheetIndex, int rowIndex, int columnIndex)` | Returns the value of the cell as a number.  For strings throws an exception.  For blank cells we return a 0. |
| `double` | `getCellNumericValue(String cellName)` | Returns the value of the cell as a number.  For strings throws an exception.  For blank cells we return a 0. |
| `double` | `getCellNumericValue(String sheetName, int rowIndex, int columnIndex)` | Returns the value of the cell as a number.  For strings throws an exception.  For blank cells we return a 0. |
| `String` | `getCellStringValue(int sheetIndex, int rowIndex, int columnIndex)` | Returns the value of the cell as a string - for numeric cells throws an exception.  For blank cells returns an empty string.  For formula cells that are not string formulas, returns empty string |
| `String` | `getCellStringValue(String cellName)` | Returns the value of the cell as a string - for numeric cells throws an exception.  For blank cells returns an empty string.  For formula cells that are not string formulas, returns empty string |
| `String` | `getCellStringValue(String sheetName, int rowIndex, int columnIndex)` | Returns the value of the cell as a string - for numeric cells throws an exception.  For blank cells returns an empty string.  For formula cells that are not string formulas, returns empty string |
| `org.apache.poi.ss.usermodel.CellType` | `getCellType(int sheetIndex, int rowIndex, int columnIndex)` | Returns the cell type (numeric, formula, string...) |
| `org.apache.poi.ss.usermodel.CellType` | `getCellType(String cellName)` | Returns the cell type (numeric, formula, string...) |
| `org.apache.poi.ss.usermodel.CellType` | `getCellType(String sheetName, int rowIndex, int columnIndex)` | Returns the cell type (numeric, formula, string...) |
| `int` | `getFirstCellNum(int sheetIndex, int rowIndex)` | Returns the number of the first cell contained in this row (the 1-based column number of the first cell). |
| `int` | `getFirstCellNum(String sheetName, int rowIndex)` | Returns the number of the first cell contained in this row (the 1-based column number of the first cell). |
| `int` | `getFirstRowNum(int sheetIndex)` | Returns the first row on the sheet |
| `int` | `getFirstRowNum(String sheetName)` | Returns the first row on the sheet |
| `int` | `getLastCellNum(int sheetIndex, int rowIndex)` | Returns the index of the last cell contained in this row (the 1-based column number of the last cell). |
| `int` | `getLastCellNum(String sheetName, int rowIndex)` | Returns the index of the last cell contained in this row (the 1-based column number of the last cell). |
| `int` | `getLastRowNum(int sheetIndex)` | Returns the number of the last row on the sheet.  Owing to idiosyncrasies in the excel file format, if the result of calling this method is one, you can't tell if that means there are zero rows on the sheet, or one at the first position.  For that case, additionally call `org.apache.poi.ss.usermodel.Sheet.getPhysicalNumberOfRows()` to find out if there is a row at position zero or not. |
| `int` | `getLastRowNum(String sheetName)` | Returns the number of the last row on the sheet.  Owing to idiosyncrasies in the excel file format, if the result of calling this method is one, you can't tell if that means there are zero rows on the sheet, or one at the first position.  For that case, additionally call `org.apache.poi.ss.usermodel.Sheet.getPhysicalNumberOfRows()` to find out if there is a row at position zero or not. |
| `int` | `getNumberOfSheets()` | Returns the number of spreadsheets in the workbook |
| `int` | `getSheetIndex(String sheetName)` | Returns the index of the sheet with the given name.  Returns `1` if `sheetName` is `null` |
| `String` | `getSheetName(int sheetIndex)` | Returns the sheet name for the specified index |
| `org.apache.poi.ss.usermodel.Workbook` | `getWorkbook()` | Returns internal class of the workbook, `null` if file isn't not loaded.  Please note that if you change workbook using API of returned object and want to save workbook to a file, you need to call [`setChanged()`](#setChanged()) |
| `boolean` | `isLoaded()` | Returns `true` if workbook is loaded from file. |
| `void` | `readFile()` | Loads the workbook from the file.  **Warning!** All unsaved data (if any) in the workbook is lost after this method is called. |
| `void` | `readHyperArray(HyperArray array, int sheetIndex, int rowIndex, int columnIndex, boolean dim1AcrossRows)` | Reads one- or two-dimensional [`HyperArray`](../HyperArray.md "class in com.anylogic.engine") data from the sheet starting at the given cell. |
| `void` | `readHyperArray(HyperArray array, String cellName, boolean dim1AcrossRows)` | Reads one- or two-dimensional [`HyperArray`](../HyperArray.md "class in com.anylogic.engine") data from the sheet starting at the given cell. |
| `void` | `readHyperArray(HyperArray array, String sheetName, int rowIndex, int columnIndex, boolean dim1AcrossRows)` | Reads one- or two-dimensional [`HyperArray`](../HyperArray.md "class in com.anylogic.engine") data from the sheet starting at the given cell. |
| `int` | `readTableFunction(TableFunction tableFunction, int sheetIndex, int rowIndex, int columnIndex, int length)` | Reads the table function from the sheet starting at the row with index `rowIndex`:  - arguments are read from column at `columnIndex`  - values are read from column at `columnIndex + 1`    If there is not enough data in the sheet to fill in the `length`, then table function gets less points.  Method returns the actual number of table function points read from the sheet. |
| `int` | `readTableFunction(TableFunction tableFunction, String cellName, int length)` | Reads the table function from the sheet starting at the row of the given cell:  - arguments are read from column of the given cell  - values are read from column next to the given cell    If there is not enough data in the sheet to fill in the `length`, then table function gets less points.  Method returns the actual number of table function points read from the sheet. |
| `int` | `readTableFunction(TableFunction tableFunction, String sheetName, int rowIndex, int columnIndex, int length)` | Reads the table function from the sheet starting at the row with index `rowIndex`:  - arguments are read from column at `columnIndex`  - values are read from column at `columnIndex + 1`    If there is not enough data in the sheet to fill in the `length`, then table function gets less points.  Method returns the actual number of table function points read from the sheet. |
| `void` | `setCellFormula(String formula, int sheetIndex, int rowIndex, int columnIndex)` | Sets formula for this cell.  Note, this method only sets the formula string and does not calculate the formula value. |
| `void` | `setCellFormula(String formula, String cellName)` | Sets formula for this cell.  Note, this method only sets the formula string and does not calculate the formula value. |
| `void` | `setCellFormula(String formula, String sheetName, int rowIndex, int columnIndex)` | Sets formula for this cell.  Note, this method only sets the formula string and does not calculate the formula value. |
| `void` | `setCellValue(boolean value, int sheetIndex, int rowIndex, int columnIndex)` | Sets a boolean value for the cell. |
| `void` | `setCellValue(boolean value, String cellName)` | Sets a boolean value for the cell. |
| `void` | `setCellValue(boolean value, String sheetName, int rowIndex, int columnIndex)` | Sets a boolean value for the cell. |
| `void` | `setCellValue(double value, int sheetIndex, int rowIndex, int columnIndex)` | Sets a numeric value for the cell. |
| `void` | `setCellValue(double value, String cellName)` | Sets a numeric value for the cell. |
| `void` | `setCellValue(double value, String sheetName, int rowIndex, int columnIndex)` | Sets a numeric value for the cell. |
| `void` | `setCellValue(String value, int sheetIndex, int rowIndex, int columnIndex)` | Sets a string value for the cell. |
| `void` | `setCellValue(String value, String cellName)` | Sets a string value for the cell. |
| `void` | `setCellValue(String value, String sheetName, int rowIndex, int columnIndex)` | Sets a string value for the cell. |
| `void` | `setCellValue(Date value, int sheetIndex, int rowIndex, int columnIndex)` | Sets a date value for the cell. |
| `void` | `setCellValue(Date value, String cellName)` | Sets a date value for the cell. |
| `void` | `setCellValue(Date value, String sheetName, int rowIndex, int columnIndex)` | Sets a date value for the cell. |
| `void` | `setChanged()` | This method may be used to tell AnyLogic that this workbook has unsaved changes and should be written on [`writeFile()`](#writeFile()) or included to the model snapshot if it has [such setting](#%3Cinit%3E(java.lang.String,boolean)).  This method should be used when you manually change the workbook via [`getWorkbook()`](#getWorkbook()).  All `setCell*()` etc. |
| `void` | `setFileName(String fileName)` | Switches this object to work with another file.  Method does nothing if the given file name is the same as at the current workbook.  Any loaded or unsaved data (if any) in this workbook remains as is until you manually call [`readFile()`](#readFile()).  Method may be used for loading workbook from another file as well as for saving changed workbook to some other location. |
| `String` | `toString()` |  |
| `int` | `writeDataSet(DataSet dataSet, int sheetIndex, int rowIndex, int columnIndex)` | Writes the given data set to the sheet starting at the given cell. |
| `int` | `writeDataSet(DataSet dataSet, String cellName)` | Writes the given data set to the sheet starting at the given cell. |
| `int` | `writeDataSet(DataSet dataSet, String sheetName, int rowIndex, int columnIndex)` | Writes the given data set to the sheet starting at the given cell. |
| `void` | `writeFile()` | Stores the current workbook to the file.  Workbook should be loaded.  Unchanged workbooks (workbooks without any unsaved modifications) aren't saved.  For saving to another location please call [`setFileName(String)`](#setFileName(java.lang.String)) before this method. |
| `void` | `writeFile(boolean force)` | Stores the current workbook to the file.  Workbook should be loaded.  For saving to another location please call [`setFileName(String)`](#setFileName(java.lang.String)) before this method. |
