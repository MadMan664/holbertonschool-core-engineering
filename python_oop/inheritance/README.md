# Python - Inheritance & Polymorphism

Building a small class hierarchy (`BaseGeometry` -> `Rectangle` ->
`Square`) to explore how subclasses reuse and extend behavior from a
parent class, how method overriding enables polymorphism, and how
`isinstance()`/`issubclass()` check the relationships between them.

## Tasks

0. `0-polymorphism_demo.py` - guided demo of inheritance and
   polymorphism with `Animal`, `Dog`, and `Cat`, plus
   `isinstance()`/`issubclass()` checks.
1. `base_geometry.py` - `BaseGeometry`, defining a shared `area()`
   interface and `integer_validator()`.
2. `1-rectangle.py` - `Rectangle(BaseGeometry)` with private,
   validated `width` and `height`.
3. `2-rectangle.py` - `Rectangle` with `area()` and a
   `[Rectangle] <width>/<height>` string form.
4. `1-square.py` - `Square(Rectangle)`, a specialized rectangle with
   equal sides.
5. `2-square.py` - `Square` with its own `[Square] <width>/<height>`
   string form.
