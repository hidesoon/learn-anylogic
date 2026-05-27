*来源 (Source): <https://anylogic.help/advanced/functions/math.html>*

---

# Mathematical functions

AnyLogic provides a comprehensive set of mathematical functions. The table below gives a brief descriptions of the functions, for the details you may refer to the online Javadoc on  [Math](https://docs.oracle.com/javase/9/docs/api/java/lang/Math.html) class.

| Return type | Name | Description |
| --- | --- | --- |
| double | abs(double a) | Returns the absolute value of a double value. |
| int | abs(int a) | Returns the absolute value of an int value. |
| double | acos(double a) | Returns the arc cosine of a value; the returned angle is in the range 0.0 through π.   a — the value whose arc cosine is to be returned. |
| double | asin(double a) | Returns the arc sine of a value; the returned angle is in the range -π/2 through π/2.   a — the value whose arc sine is to be returned. |
| double | atan(double a) | Returns the arc tangent of a value; the returned angle is in the range -π/2 through π/2.   a — the value whose arc tangent is to be returned. |
| double | atan2(double y, double x) | Returns the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta). |
| double | cbrt(double a) | Returns the cube root of a double value. |
| double | ceil(double a) | Returns the smallest (closest to negative infinity) double value that is greater than or equal to the argument and is equal to a mathematical integer. |
| double | cos(double a) | Returns the trigonometric cosine of an angle.   a — an angle, in radians. |
| double | cosh(double x) | Returns the hyperbolic cosine of a double value.  x — The number whose hyperbolic cosine is to be returned. |
| double | exp(double a) | Returns Euler’s number e raised to the power of a double value. |
| double | expm1(double x) | Returns ex-1. |
| double | floor(double a) | Returns the largest (closest to positive infinity) double value that is less than or equal to the argument and is equal to a mathematical integer. |
| double | gammaLog(double x) | Returns the natural logarithm of the gamma function of x: ln(Γ(x)). The gamma function is an extension of the factorial function that works on all positive values of x. If n is a positive integer, then: Γ(n) = (n - 1)!.  The gammaLog function may be useful in System Dynamics models for computing combinatorial factors. |
| int | getExponent(double d) | Returns the unbiased exponent used in the representation of a double. |
| double | hypot(double x, double y) | Returns sqrt(x2 y2) without intermediate overflow or underflow. |
| boolean | isFinite(double v) | Returns true if the given value v is finite (not +/-infinity or NaN). |
| double | limit(double min, double x, double max) | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| int | limit(int min, int x, int max) | Returns x if it is within [min,max] interval, otherwise returns the closest bound. |
| double | limitMax(double x, double max) | Returns x if it is less or equal to max, otherwise returns max. May be more self-explanatory than the function min as explicitly says “x is right-limited by max”. |
| int | limitMax(int x, int max) | Returns x if it is less or equal to max, otherwise returns max. May be more self-explanatory than the function min as explicitly says “x is right-limited by max”. |
| double | limitMin(double min, double x) | Returns x if it is greater or equal to min, otherwise returns min. May be more self-explanatory than the function max as explicitly says “x is left-limited by min”. |
| int | limitMin(int min, int x) | Returns x if it is greater or equal to min, otherwise returns min. May be more self-explanatory than the function max as explicitly says “x is left-limited by min”. |
| double | log(double a) | Returns the natural logarithm (base e) of a double value. |
| double | log10(double a) | Returns the base 10 logarithm of a double value. |
| double | log1p(double x) | Returns the natural logarithm of the sum of the argument and 1. |
| double | max(double a, double b) | Returns the greater of two double values. |
| int | max(int a, int b) | Returns the greater of two integer values. |
| double | min(double a, double b) | Returns the smaller of two double values. |
| int | min(int a, int b) | Returns the smaller of two integer values. |
| double | pow(double a, double b) | Returns the value of the first argument raised to the power of the second argument. |
| double | quantum(double value, double quantizer) | Returns the number smaller (by absolute value) than or equal to value that is an integer multiple of quantizer. If quantizer is less than or equal to zero, then value is returned unchanged.   value — the value quantizer — quantizer, defining the interval between possible values returned by the function: quantizer, quantizer\*2, … |
| double | random() | Returns a double value with a positive sign, greater than or equal to 0.0 and less than 1.0. |
| double | rint(double a) | Returns the double value that is closest in value to the argument and is equal to a mathematical integer. |
| double | roundToDecimal(double v, int nDecimalDigits) | Rounds the given value v to the given precision. Returns the number closest to the given value, retaining the given number of decimal digits in the fractional / integer part.  The result is equal to the value of the expression:  floor(v\*10nDecimalDigits + 0.5) / 10DecimalDigits   v — floating-point value to be rounded to the given precision  nDecimalDigits — if positive, the fractional part will be affected; if negative, the integer part |
| int | roundToInt(double v) | Returns integer value closest to the given value v. Unlike Math.round(double), returns int value (instead of long) which may be more convenient for some operations.  The result is equal to the value of the expression: (int) floor(v + 0.5)  Special cases:  * If the argument is NaN, the result is 0. * If the argument is negative infinity or any value less than or equal to the value of Integer.MIN\_VALUE, the result is equal to the value of Integer.MIN\_VALUE. * If the argument is positive infinity or any value greater than or equal to the value of Integer.MAX\_VALUE, the result is equal to the value of Integer.MAX\_VALUE. |
| double | scalb(double d, int scaleFactor) | Returns d\*2scaleFactor rounded as if performed by a single correctly rounded floating-point multiply to a member of the double value set. |
| double | signum(double d) | Returns the signum function of the argument; zero if the argument is zero, 1.0 if the argument is greater than zero, -1.0 if the argument is less than zero. |
| double | sin(double a) | Returns the trigonometric sine of an angle.   a — an angle, in radians. |
| double | sinh(double x) | Returns the hyperbolic sine of a double value.   x — The number whose hyperbolic sine is to be returned. |
| double | sqr(double v) | Returns the square of the given value v2. |
| double | sqrt(double a) | Returns the correctly rounded positive square root of a double value. |
| double | tan(double a) | Returns the trigonometric tangent of an angle.   a — an angle, in radians. |
| double | tanh(double x) | Returns the hyperbolic tangent of a double value. |
| double | toDegrees(double angrad) | Converts an angle measured in radians to an approximately equivalent angle measured in degrees.  angrad — an angle, in radians. |
| double | toRadians(double angdeg) | Converts an angle measured in degrees to an approximately equivalent angle measured in radians.   angdeg — an angle, in degrees. |
| double | xidz(double a, double b, double x) | Tries to divide the first argument by the second. If the result is infinity or not a number, returns the third argument (x), otherwise returns the division result. |
| double | zidz(double a, double b) | Tries to divide the first argument by the second. If the result is infinity or not a number, returns 0, otherwise returns the division result. |
