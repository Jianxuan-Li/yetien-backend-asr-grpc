import unittest
import os
import sys

# add the test directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))

# add the server directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

# collect all tests from the test directory, the prefix is test_*.py, and import them
test_dir = os.path.join(os.path.dirname(__file__), 'test')
suite = unittest.TestLoader().discover(test_dir, pattern='test_*.py')

# run the tests
unittest.TextTestRunner(verbosity=2).run(suite)