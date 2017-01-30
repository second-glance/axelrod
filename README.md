# axelrod
Stuff for the Axelrod Reloaded contest.

## Development Notes
So Far, the core of the development is in the python_environment_0 branch.
It includes:
<li>
  <ul>The main classes</ul>
  <ul>Some variables (in dummy_algo.py and main_test.py) to test the classes</ul>
</li>

The current version is slow and not user friendly in terms of inputs and outputs.

## Potential Improvement
### R Code Speed
R code is really slow to execute.
The current version does the job but is not optimized. There is probably a way to make it faster.

### Input Helper Class
An input helper class would be welcomed. This requires to define how competitors will provide their code and names.

### Output
The current output is an ordered list of competitor instances. This is ok for low number of competitors but could be improved (serializing?)
