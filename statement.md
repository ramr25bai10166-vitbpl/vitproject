**Project Title:** Multi-purpose Program

**● Problem Statement**

Many users, from students to professionals, rely on multiple separate
tools (basic calculators, scientific calculators, geometric formula
references, and timers) to perform diferent tasks. This fragmentation
leads to inefficiency, context switching, and reliance on physical
devices or web searches for simple calculations. The core problem is the
lack of a single, unified, and user-friendly application that provides
comprehensive computational utility across arithmetic, geometry,
algebra, and utility functions in one interface.

**● Scope of the Project**

The scope of this project is to develop a **Multi-purpose application**.

**In Scope:**

- Basic arithmetic operations (+, -, \*, /) with high precision (using
  decimal library).

- 2D Geometry calculations (area and perimeter for square, rectangle,
  triangle, circle).

- 3D Geometry calculations (surface area and volume for cube, cuboid,
  sphere, cylinder).

- Algebraic tool for finding the roots of a standard quadratic equation
  (\$ax\^2 + bx + c = 0\$).

- A basic stopwatch (uses time library).

- Input validation to prevent errors like division by zero and
  non-positive dimensions for shapes.

**Out of Scope:**

- Advanced scientific functions (e.g., trigonometry, logarithms, complex
  number manipulation beyond quadratic roots).

- Graphing capabilities.

- Data persistence or user accounts.

- Unit conversions (e.g., meters to feet).

- Advanced statistical calculations.

**● Target Users**

The application is designed for a broad audience that requires reliable,
diverse mathematical tools:

1.  **Students (Middle School to College):** Primary users needing tools
    for homework in math, physics, and introductory engineering courses.
    They need quick access to formulas for geometric shapes and
    algebraic solutions.

2.  **Hobbyists and DIY Enthusiats:** Users needing quick calculation of
    material requirements (area/volume) for home projects or simple
    geometry.

3.  **General Users:** Anyone needing a standard, reliable arithmetic
    calculator and utility tools like a stopwatch for daily tasks.

**● High-Level Features**

The application will feature a clear, menu-driven interface accessible
via numeric inputs.

**Feature 1: Basic Arithmetic Calculator**

- Supports standard four functions (+, -, \*, /).

- Uses a high-precision decimal type for accurate results.

- Handles division by zero error gracefully.

**Feature2: 2D Geometry Calculator**

- **Square:** Calculates Area and Perimeter from side length.

- **Rectangle:** Calculates Area and Perimeter from length and width.

- **Triangle:** Supports both Heron\'s formula (for 3 sides) and
  Right-Angled triangle area calculation.

- **Circle:** Calculates area and circumference from radius.

**Feature 3: 3D Geometry Calculator**

- **Cube:** Calculates surface area and volume from side length.

- **Cuboid:** Calculates surface area and volume from length, width, and
  height.

- **Sphere:** Calculates surface area and volume from radius.

- **Cylinder:** Calculates surface area and volume from radius and
  height.

**Feature 4: Quadratic Equation Solver**

- Accepts coefficients \$a\$, \$b\$, and \$c\$ for the equaton \$ax\^2 +
  bx + c = 0\$.

- Calculates and givess the real or complex roots based on the
  discriminant (\$D = b\^2 - 4ac\$).

**Feature 5 :Stopwatch Utility**

- Simple stopwatch activated and stopped by user input (by pressing
  Enter).

- Displays time in seconds.
