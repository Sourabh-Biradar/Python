# if __name__ = ' __main__'

# check whether a Python script is being run directly or imported as a module.

# __name__
print(__name__)

# problem
import spanish

spanish.greet('Snow')
# jst importing executes module's greet()
# also module.greet() executes here
# so two outputs : problem



