import math

# ---------- Constants ----------
print(math.pi)        # Value of pi
print(math.e)         # Euler's number
print(math.tau)       # 2*pi
print(math.inf)       # Infinity
print(math.nan)       # Not a Number

# ---------- Power & Log ----------
print(math.pow(2, 3))     # 2^3
print(math.sqrt(16))      # Square root
print(math.exp(1))        # e^1
print(math.log(8, 2))     # log base 2
print(math.log10(100))    # log base 10
print(math.log2(8))       # log base 2

# ---------- Trigonometry (radians) ----------
print(math.sin(math.pi/2))  # Sine
print(math.cos(0))          # Cosine
print(math.tan(math.pi/4))  # Tangent

# ---------- Inverse Trigonometry ----------
print(math.asin(1))       # Inverse sine
print(math.acos(1))       # Inverse cosine
print(math.atan(1))       # Inverse tangent
print(math.atan2(1, 1))   # atan(y/x) with quadrant info

# ---------- Hyperbolic Functions ----------
print(math.sinh(1))       # Hyperbolic sine
print(math.cosh(1))       # Hyperbolic cosine
print(math.tanh(1))       # Hyperbolic tangent
print(math.asinh(1))      # Inverse hyperbolic sine
print(math.acosh(2))      # Inverse hyperbolic cosine
print(math.atanh(0.5))    # Inverse hyperbolic tangent

# ---------- Degree & Radian Conversion ----------
print(math.degrees(math.pi))  # Radian to degree
print(math.radians(180))      # Degree to radian

# ---------- Rounding Functions ----------
print(math.ceil(4.2))     # Round up
print(math.floor(4.9))    # Round down
print(math.trunc(4.9))    # Remove decimal part
print(math.fabs(-5))      # Absolute value

# ---------- Remainder & Mod ----------
print(math.fmod(7, 3))    # Floating-point remainder
print(math.remainder(7, 3))  # IEEE remainder

# ---------- Factorial & Combinatorics ----------
print(math.factorial(5))  # 5!
print(math.comb(5, 2))    # nCr
print(math.perm(5, 2))    # nPr

# ---------- Number Theory ----------
print(math.gcd(12, 18))   # Greatest common divisor
print(math.lcm(12, 18))   # Least common multiple

# ---------- Special Functions ----------
print(math.hypot(3, 4))   # sqrt(x^2 + y^2)
print(math.fsum([0.1, 0.2, 0.3]))  # Accurate sum
print(math.prod([1, 2, 3, 4]))     # Product of elements
print(math.dist([1,2], [4,6]))     # Euclidean distance

# ---------- Floating-Point Manipulation ----------
print(math.frexp(8))      # Mantissa & exponent
print(math.ldexp(0.5, 4)) # mantissa * 2^exp
print(math.modf(3.14))    # Fractional & integer parts
print(math.nextafter(1.0, 2.0))  # Next representable float
print(math.ulp(1.0))      # Unit in last place

# ---------- Checking Functions ----------
print(math.isfinite(10))       # Check finite
print(math.isinf(math.inf))    # Check infinity
print(math.isnan(math.nan))    # Check NaN
print(math.isclose(0.1+0.2, 0.3))  # Float comparison

# ---------- Gamma Functions ----------
print(math.gamma(5))    # Gamma value
print(math.lgamma(5))   # Log gamma value
