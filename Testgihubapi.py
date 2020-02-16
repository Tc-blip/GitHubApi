
import unittest
from githubapi import getRepositories


class Testgithubapi(unittest.TestCase):
    def testgetRepositories(self):
        except_out = [()]
        self.assertEqual(getRepositories('Tc-blip'), except_out) 


if __name__ == '__main__':
   
    unittest.main()  