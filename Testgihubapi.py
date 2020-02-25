
import unittest
from githubapi import getRepositories


class Testgithubapi(unittest.TestCase):
    def testgetRepositories(self):
        except_out2 = [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]]
        self.assertEqual(getRepositories('richkempinski'), except_out2)

if __name__ == '__main__':
   
    unittest.main()  