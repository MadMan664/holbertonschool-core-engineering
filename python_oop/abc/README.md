# Python - Abstract Classes & Interfaces

Abstract base classes and abstract methods (`ABC`, `@abstractmethod`),
interface-like design and duck typing, multiple inheritance and
method resolution order, mixins, and extending a built-in class
(`list`) while preserving its original behavior.

## Tasks

0. `animals.py` - `Animal(ABC)` with an abstract `sound()`, and
   concrete `Dog`/`Cat` subclasses.
1. `shapes.py` - `Shape(ABC)` with abstract `area()`/`perimeter()`,
   concrete `Circle`/`Rectangle`, and `shape_info()` using duck
   typing.
2. `flyingfish.py` - `Fish` and `Bird`, combined via multiple
   inheritance into `FlyingFish`, which overrides all three shared
   methods.
3. `dragon.py` - `SwimMixin` and `FlyMixin`, composed into `Dragon`.
4. `verboselist.py` - `VerboseList(list)`, announcing every
   `append`/`extend`/`remove`/`pop`.
