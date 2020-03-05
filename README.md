# cherub-bot

Very simple experiments with a starcraft 2 bot. The main experiment is using the pysc2 api, py_trees, and owl-bt.

![image](https://user-images.githubusercontent.com/2446659/75947417-ee3e7580-5e65-11ea-932f-160d472c1ae2.png)

owl-bt is a behavior tree editor so I can quickly visualize and change my behavior tree construction.

py_trees is the behavior tree runtime and implements the general purpose nodes like some of the composites and decorators.
It also has an ascii display which I can use to display the behavior tree at runtime as an overlay on the game

pysc2 is a nice starcraft 2 api that includes some high level functionality and some simple example bots.

Some more principles I plan on following
- Voronoi Diagram path planning for swarming and multi agent pursuit
  - To simplify the math, I'll probably use discrete approximation. A lot of traditional voronoi algorithms are difficult to adapt for barriers and concave shapes.
- Planning
  - Hard coded build order openings (like chess)
  - Using a general purpose SAT solver, probably Z3, for tightly constrained optimization problems (economy and build order planning)
  - hardcoded heuristics for approximating large complex optimizations and simulations (opponent modeling, large battle prediction)
- Logging should read like a story. "Walter finished building a proxy barracks in Colter's Ridge"
  - All non-structure units have randomly generated names from census data like "Bill" or "Juan"
  - All map regions will be given randomly generated names like "Dead Horse Valley" and "Colter's Ridge"
  - Game state observations and interpretations should also be logged. "Colter's ridge appears to be a good candidate for a proxy barracks"
- Run a debug webserver
  - display observations and interpretations that would be difficult or too crowded to view as an overlay
  - allow running commands and queries to change behavior or test different behaviors at runtime.
