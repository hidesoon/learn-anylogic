*来源 (Source): <https://anylogic.help/advanced/functions/format.html>*

---

# Formatting functions

:   | Function | Description |
    | --- | --- |
    | String format(boolean value) | Formats a boolean value. Returns the string containing the formatted value (true or false).   value — the boolean value to be formatted |
    | String format(int value) | Formats an integer value to String using the default AnyLogic formatter. Returns the string containing the formatted value.   value — the integer value to be formatted |
    | String format(double value) | Formats a double value to String using the default AnyLogic formatter. Returns the string containing the formatted value.   value — the value to be formatted |
    | String format(long value) | Formats a long value to String using the default AnyLogic formatter. Returns the string containing the formatted value.   value — the value to be formatted |
    | String format(char value) | Formats a character to String. Returns the string containing the formatted value.   value — the value to be formatted |
    | String format(java.util.Date date) | Formats the given date to String. Returns the string containing the formatted value.   date — the date to be formatted |
    | String format(double value, IUnits<?> units) | Formats a double value with units to String using the default AnyLogic formatter. Returns the string containing the formatted value.   value — the value to be formatted  units — the units |
    | String formatAmountUnits(double value, AmountUnits units) | Converts the value to the given units and formats it to String using the default AnyLogic formatter. Returns the string containing the formatted value.   value — the value in cubic meters or kilograms  units — the required units |
    | String formatLengthUnits(double value, LengthUnits units) | Converts the value to the given units and formats it to String. Returns the string containing the formatted value.   value — the value in meters  units — the required units |
    | String formatLengthUnits(LengthUnits unit, boolean fullName) | Returns the full or short name of the length units.   unit — the length units  fullName —  if true, then returns the full name (meter, foot, etc.), otherwise - short (m, ft, etc.) |
    | String formatSpeedUnits(double value, SpeedUnits units) | Converts the value to the given units and formats it to String. Returns the string containing the formatted value.   value — the value in meters per second  units — the required units |
    | String formatFlowRateUnits(double value, FlowRateUnits units) | Converts the value to the given units and formats it to String. Returns the string containing the formatted value.   value — the value in cubic meters per second or kilograms per second  units — the required units |
    | String formatDayOfWeek(int dayOfWeek, boolean fullName) | Returns the full or short name of the weekday. If fullName is true, then the function returns the full name (Monday, Tuesday, etc.), otherwise - short (Mon, Tue, etc.)   dayOfWeek — one of MONDAY, TUESDAY, ... constants  fullName — defines, whether to return the short, or the full name |
    | String formatMonth(int month, boolean fullName) | Returns the full or short name of the month. If fullName is true, then the function returns the full name (January, February, etc.), otherwise - short (Jan, Feb, etc.)   month — one of JANUARY, FEBRUARY, ... constants  fullName — defines, whether to return the short, or the full name |
    | String formatTimeInterval(double dt) | Returns a string representation of the given time interval, according to the current time unit settings, in the form 123 days 21h 0’56”.   dt — the time interval |
    | String formatGeoHeading(double radians) | Formats the given heading angle (measured in radians CW, starting from North direction) and returns it as human-readable geographical heading (azimuth). E.g. PI / 7 will be formatted as 26° NNE.   radians — the heading angle (measured in radians clockwise, starting from North direction) |
    | String formatLatitude(double degrees) | Formats the given latitude (in degrees) and returns the formatted latitude, e.g. N59°56’0”.   degrees — the latitude in decimal degrees |
    | String formatLongitude(double degrees) | Formats the given longitude (in degrees) and returns the formatted longitude, e.g. E30°20’0”.   degrees — the longitude in decimal degrees |
    | double toLatitude(int degrees, int minutes, double seconds, boolean northOrSouth) | Converts latitude from human-readable format (e.g. 59° 56’ 0” North) to the format used in the model. Returns the resulting latitude, measured in degrees (-90 ... (South) ... 0 ... (North) ... +90).   degrees — number of degrees, 0...90  minutes — number of minutes (1/60 of degree), 0 .. 59  seconds — number of seconds (1/60 of minute), 0 .. 59  northOrSouth — true for North, false for South |
    | double toLongitude(int degrees, int minutes, double seconds, boolean eastOrWest) | Converts longitude from human-readable format (e.g. 30° 20’ 0” East) to the format used in the model. Returns the resulting longitude, measured in degrees (-180 ... (West) ... 0 ... (East) ... +180).   degrees — number of degrees, 0...90  minutes — number of minutes (1/60 of degree), 0 .. 59  seconds — number of seconds (1/60 of minute), 0 .. 59  eastOrWest — true for East, false for West |
