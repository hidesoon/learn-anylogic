*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/UtilitiesRandom.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface UtilitiesRandom

All Known Implementing Classes:
:   `Agent`, `Experiment`, `ExperimentCompareRuns`, `ExperimentMultipleRuns`, `ExperimentOptimization`, `ExperimentParamVariation`, `ExperimentRunFast`, `ExperimentSimulation`, `FlowchartBlock`, `Utilities`

---

```
public interface UtilitiesRandom
```

Random number generation utilities for various probability distributions

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final int` | `RANDOM_BOUNDED_DISTRIBUTIONS_MAX_ITERATIONS` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default int` | `bernoulli(double p)` | Generates a sample of the Bernoulli distribution, i.e. |
| `static int` | `bernoulli(double p, Random r)` | Generates a sample of the Bernoulli distribution using the specified random number generator. |
| `default double` | `beta(double p, double q)` | Generates a sample of the Beta distribution with `min` set to `0` and `max` set to `1`. |
| `default double` | `beta(double p, double q, double min, double max)` | Generates a sample of the Beta distribution. |
| `default double` | `beta(double min, double max, double p, double q, double shift, double stretch)` | Generates a sample of truncated Beta distribution.  Distribution `beta(p, q, 0, 1)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `beta(double min, double max, double p, double q, double shift, double stretch, Random r)` | Generates a sample of truncated Beta distribution using the specified random number generator.  Distribution `beta(p, q, 0, 1)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `beta(double p, double q, double min, double max, Random r)` | Generates a sample of the Beta distribution using the specified random number generator. |
| `default int` | `binomial(double p)` | Generates a sample of the Binomial distribution with `n` set to `1`. |
| `default double` | `binomial(double min, double max, double p, double n, double shift, double stretch)` | Generates a sample of truncated Binomial distribution.  Distribution `binomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `binomial(double min, double max, double p, double n, double shift, double stretch, Random r)` | Generates a sample of truncated Binomial distribution using the specified random number generator.  Distribution `binomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `default int` | `binomial(double p, int n)` | Generates a sample of the Binomial distribution. |
| `static int` | `binomial(double p, int n, Random r)` | Generates a sample of the Binomial distribution using the specified random number generator. |
| `default double` | `cauchy(double lambda)` | Generates a sample of the Cauchy distribution with `theta` set to `0`. |
| `default double` | `cauchy(double lambda, double theta)` | Generates a sample of the Cauchy distribution. |
| `static double` | `cauchy(double lambda, double theta, Random r)` | Generates a sample of the Cauchy distribution using the specified random number generator. |
| `default double` | `chi2(double nu)` | Generates a sample of the Chi Squared distribution with `min` set to `0`. |
| `default double` | `chi2(double nu, double min)` | Generates a sample of the Chi Squared distribution. |
| `static double` | `chi2(double nu, double min, Random r)` | Generates a sample of the Chi Squared distribution using the specified random number generator. |
| `default double` | `erlang(double beta, int m)` | Generates a sample of the Erlang distribution with `min` set to 0. |
| `default double` | `erlang(double beta, int m, double min)` | Generates a sample of the Erlang distribution. |
| `static double` | `erlang(double beta, int m, double min, Random r)` | Generates a sample of the Erlang distribution using the specified random number generator. |
| `default double` | `exponential()` | Generates a sample of the Exponential distribution with `lambda` set to `1` and `min` set to `0`. |
| `default double` | `exponential(double lambda)` | Generates a sample of the Exponential distribution with `min` set to `0`. |
| `default double` | `exponential(double lambda, double min)` | Generates a sample of the Exponential distribution. |
| `default double` | `exponential(double min, double max, double shift, double stretch)` | Generates a sample of truncated Exponential distribution.  Distribution `exponential(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `exponential(double min, double max, double shift, double stretch, Random r)` | Generates a sample of truncated Exponential distribution using the specified random number generator.  Distribution `exponential(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `exponential(double lambda, double min, Random r)` | Generates a sample of the Exponential distribution using the specified random number generator. |
| `default double` | `gamma(double alpha, double beta)` | Generates a sample of the Gamma distribution with `min` set to `0`. |
| `default double` | `gamma(double alpha, double beta, double min)` | Generates a sample of the Gamma distribution. |
| `default double` | `gamma(double min, double max, double alpha, double shift, double stretch)` | Generates a sample of truncated Gamma distribution.  Distribution `gamma(alpha, 1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `gamma(double min, double max, double alpha, double shift, double stretch, Random r)` | Generates a sample of truncated Gamma distribution using the specified random number generator.  Distribution `gamma(alpha, 1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `gamma(double alpha, double beta, double min, Random r)` | Generates a sample of the Gamma distribution using the specified random number generator. |
| `default int` | `geometric(double p)` | Generates a sample of the Geometric distribution. |
| `static int` | `geometric(double p, Random r)` | Generates a sample of the Geometric distribution using the specified random number generator. |
| `Random` | `getDefaultRandomGenerator()` | Retrieves the random number generator used by all probability distributions by default, i.e. |
| `default double` | `gumbel1(double a, double b)` | Generates a sample of the Type I Gumbel distribution.  This distribution has the form  `p(x) = a b exp(-(b exp(-ax) + ax))` |
| `static double` | `gumbel1(double a, double b, Random r)` | Generates a sample of the Type I Gumbel distribution using the specified random number generator. |
| `default double` | `gumbel2(double a, double b)` | Generates a sample of the Type II Gumbel distribution.  This distribution has the form  `p(x) = b a x^-(a+1) exp(-b x^-a))` |
| `static double` | `gumbel2(double a, double b, Random r)` | Generates a sample of the Type II Gumbel distribution using the specified random number generator. |
| `default int` | `hypergeometric(int ss, int dn, int ps)` | Generates a sample of the Hypergeometric distribution. |
| `static int` | `hypergeometric(int ss, int dn, int ps, Random r)` | Generates a sample of the Hypergeometric distribution using the specified random number generator. |
| `default double` | `laplace(double phi, double theta)` | Generates a sample of the Laplace distribution. |
| `static double` | `laplace(double phi, double theta, Random r)` | Generates a sample of the Laplace distribution using the specified random number generator. |
| `default int` | `logarithmic(double theta)` | Generates a sample of the Logarithmic distribution. |
| `static int` | `logarithmic(double theta, Random r)` | Generates a sample of the Logarithmic distribution using the specified random number generator. |
| `default double` | `logistic(double beta, double alpha)` | Generates a sample of the Logistic distribution. |
| `static double` | `logistic(double beta, double alpha, Random r)` | Generates a sample of the Logistic distribution using the specified random number generator. |
| `default double` | `lognormal(double mu, double sigma, double min)` | Generates a sample of the Lognormal distribution. |
| `static double` | `lognormal(double mu, double sigma, double min, Random r)` | Generates a sample of the Lognormal distribution using the specified random number generator. |
| `default int` | `negativeBinomial(double p, double n)` | Generates a sample of the Negative Binomial distribution. |
| `default double` | `negativeBinomial(double min, double max, double p, double n, double shift, double stretch)` | Generates a sample of truncated Negative Binomial distribution.  Distribution `negativeBinomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `negativeBinomial(double min, double max, double p, double n, double shift, double stretch, Random r)` | Generates a sample of truncated Negative Binomial distribution using the specified random number generator.  Distribution `negativeBinomial(p, n)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static int` | `negativeBinomial(double p, double n, Random r)` | Generates a sample of the Negative Binomial distribution using the specified random number generator. |
| `default double` | `normal()` | Generates a sample of the Normal distribution with `mean` set to `0` and `sigma` set to `1`. |
| `default double` | `normal(double sigma)` | Generates a sample of the Normal distribution with `mean` set to `0`. |
| `default double` | `normal(double sigma, double mean)` | Generates a sample of the Normal distribution. |
| `default double` | `normal(double min, double max, double shift, double stretch)` | Generates a sample of truncated Normal distribution.  Distribution `normal(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `normal(double min, double max, double shift, double stretch, Random r)` | Generates a sample of truncated Normal distribution using the specified random number generator.  Distribution `normal(1, 0)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `normal(double sigma, double mean, Random r)` | Generates a sample of the Normal distribution using the specified random number generator. |
| `default double` | `pareto(double alpha)` | Generates a sample of the Pareto distribution with `min` set to `1`. |
| `default double` | `pareto(double alpha, double min)` | Generates a sample of the Pareto distribution. |
| `static double` | `pareto(double alpha, double min, Random r)` | Generates a sample of the Pareto distribution using the specified random number generator. |
| `default double` | `pert(double min, double max, double mode)` | Generates a sample of the PERT distribution. |
| `static double` | `pert(double min, double max, double mode, Random r)` | Generates a sample of the PERT distribution using the specified random number generator. |
| `default int` | `poisson(double lambda)` | Generates a sample of the Poisson distribution. |
| `default double` | `poisson(double min, double max, double mean, double shift, double stretch)` | Generates a sample of truncated Poisson distribution.  Distribution `poisson(mean)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `poisson(double min, double max, double mean, double shift, double stretch, Random r)` | Generates a sample of truncated Poisson distribution using the specified random number generator.  Distribution `poisson(mean)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static int` | `poisson(double lambda, Random r)` | Generates a sample of the Poisson distribution using the specified random number generator. |
| `default double` | `random()` | Generates a random value uniformly distributed on the interval [0,1), the upper bound is not included.  Please use [`uniform()`](#uniform()) function (has the same logic) instead, for not to get in confusion with [`Math.random()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Math.html#random() "class or interface in java.lang") function (the latter shouldn't be used in models because it doesn't utilize random number generator of Engine and will result in not reproducible model runs). |
| `default boolean` | `randomFalse(double p)` | Generates `false` with the given probability `p`. |
| `static boolean` | `randomFalse(double p, Random r)` | Generates `false` with the given probability `p` using the specified random number generator.  For more details see [`randomFalse(double)`](#randomFalse(double)) |
| `default <T extends Enum<T>> T` | `randomFrom(Class<T> enumeration)` | Returns the randomly chosen enumeration constant.  Throws `NullPointerException` if the given class is `null` or not an enumeration class |
| `static <T extends Enum<T>> T` | `randomFrom(Class<T> enumeration, Random r)` | Returns the randomly chosen enumeration constant. |
| `default <T> T` | `randomFrom(Iterable<T> collection)` | Returns the randomly chosen element of the given collection.  For empty collections return `null`.  This result of this method is an equivalent of calling: `collection.get( uniform_discr( collection.size() - 1 ) )` |
| `static <T> T` | `randomFrom(Iterable<T> collection, Random r)` | Returns the randomly chosen element of the given collection. |
| `default <T> T` | `randomFrom(T[] array)` | Returns the randomly chosen element of the given array.  This result of this method is an equivalent of calling: `array[ uniform_discr( array.length - 1 ) ]` |
| `static <T> T` | `randomFrom(T[] array, Random r)` | Returns the randomly chosen element of the given array. |
| `default <T> T` | `randomlyCreate(Class<? extends T>... classes)` | Creates a randomly chosen object using one of the given constructors. |
| `default <T> T` | `randomlyCreate(Supplier<? extends T>... constructors)` | Creates a randomly chosen object using one of the given constructors. |
| `static <T> T` | `randomlyCreate(Random r, Class<? extends T>... classes)` | Creates a randomly chosen object using one of the given constructors. |
| `static <T> T` | `randomlyCreate(Random r, Supplier<? extends T>... constructors)` | Creates a randomly chosen object using one of the given constructors. |
| `default boolean` | `randomTrue(double p)` | Generates `true` with the given probability `p`. |
| `static boolean` | `randomTrue(double p, Random r)` | Generates `true` with the given probability `p` using the specified random number generator.  For more details see [`randomTrue(double)`](#randomTrue(double)) |
| `default <T> T` | `randomWhere(Iterable<T> collection, Predicate<T> condition)` | Returns the randomly chosen element of the given collection which meets the given condition.  For empty collections return `null`. |
| `static <T> T` | `randomWhere(Iterable<T> collection, Predicate<T> condition, Random r)` | Returns the randomly chosen element of the given collection which meets the given condition. |
| `default <T> T` | `randomWhere(T[] array, Predicate<T> condition)` | Returns the randomly chosen element of the given array which meets the given condition. |
| `static <T> T` | `randomWhere(T[] array, Predicate<T> condition, Random r)` | Returns the randomly chosen element of the given array which meets the given condition. |
| `default double` | `rayleigh(double sigma)` | Generates a sample of the Rayleigh distribution with `min` set to `0`. |
| `default double` | `rayleigh(double sigma, double min)` | Generates a sample of the Rayleigh distribution. |
| `static double` | `rayleigh(double sigma, double min, Random r)` | Generates a sample of the Rayleigh distribution using the specified random number generator. |
| `default void` | `shuffle(List<?> list)` | Randomly permutes the specified list. |
| `default double` | `triangular(double min, double max)` | Generates a sample of the Triangular distribution with `mode` set to `(min + max)/2`. |
| `default double` | `triangular(double min, double max, double mode)` | Generates a sample of the Triangular distribution. |
| `default double` | `triangular(double min, double max, double left, double mode, double right)` | Generates a sample of truncated Triangular distribution.  Distribution `triangular(left, right, mode)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `triangular(double min, double max, double left, double mode, double right, Random r)` | Generates a sample of truncated Triangular distribution using the specified random number generator.  Distribution `triangular(left, right, mode)` is stretched by `stretch` coefficient, then shifted to the right by `shift`, after that it is truncated to fit in `[min, max]` interval. |
| `static double` | `triangular(double min, double max, double mode, Random r)` | Generates a sample of the Triangular distribution using the specified random number generator. |
| `default double` | `triangularAV(double average, double variability)` | Generates a sample of the Triangular distribution with `mode` set to `average`.  Defines distribution in the form like "roughly this, +/-20%".  Is equivalent to `triangular( average * (1 - variability), average * (1 + variability) )` . |
| `static double` | `triangularAV(double average, double variability, Random r)` | Generates a sample of the Triangular distribution with `mode` set to `average`.  Defines distribution in the form like "roughly this, +/-20%".  Is equivalent to `triangular( average * (1 - variability), average * (1 + variability) )` . |
| `default double` | `uniform()` | Generates a random value uniformly distributed on the interval [0,1), the upper bound is not included. |
| `default double` | `uniform(double max)` | Generates a sample of the Uniform distribution on the interval [0, max). |
| `default double` | `uniform(double min, double max)` | Generates a sample of the Uniform distribution on the interval [min, max). |
| `static double` | `uniform(double min, double max, Random r)` | Generates a sample of the Uniform distribution on the interval [min, max) using the specified random number generator. |
| `static double` | `uniform(Random r)` | Generates a random value uniformly distributed on the interval [0,1), using the specified random number generator. |
| `default int` | `uniform_discr(int max)` | Generates a sample of the Discrete Uniform distribution in the interval [0, max], both 0 and max included! Is equivalent to `uniform_discr(0, max)`. |
| `default int` | `uniform_discr(int min, int max)` | Generates a sample of the Discrete Uniform distribution on the interval [min, max], both min and max included! |
| `static int` | `uniform_discr(int min, int max, Random r)` | Generates a sample of the Discrete Uniform distribution on the interval [min, max] using the specified random number generator, both 0 and max included! For more details see [`uniform_discr(int,int)`](#uniform_discr(int,int)). |
| `default double` | `uniform_pos()` | Generates a positive random value uniformly distributed on the interval (0,1). |
| `static double` | `uniform_pos(Random r)` | Generates a positive random value uniformly distributed on the interval (0,1), using the specified random number generator. |
| `default double` | `weibull(double beta, double alpha)` | Generates a sample of the Weibull distribution with `min` set to `0`. |
| `default double` | `weibull(double alpha, double beta, double min)` | Generates a sample of the Weibull distribution. |
| `default double` | `weibull(double min, double max, double alpha, double shift, double stretch)` | Generates a sample of truncated Weibull distribution.  Distribution `weibull(alpha, stretch, 0)` is shifted to the right by `shift` and then truncated to fit in `[min, max]` interval. |
| `static double` | `weibull(double min, double max, double alpha, double shift, double stretch, Random r)` | Generates a sample of truncated Weibull distribution using the specified random number generator.  Distribution `weibull(alpha, stretch, 0)` is shifted to the right by `shift` and then truncated to fit in `[min, max]` interval. |
| `static double` | `weibull(double alpha, double beta, double min, Random r)` | Generates a sample of the Weibull distribution using the specified random number generator. |
