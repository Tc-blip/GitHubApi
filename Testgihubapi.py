
import unittest
from githubapi import getRepositories


class Testgithubapi(unittest.TestCase):
    def testgetRepositories(self):
        except_out = [['Convenience-system','11'],['GitHubApi',"11"],['Github_issue_spyder','17'],['ssw540','4'],['SSW555','30'],['SSW567hw','16'],['SSW695','24'],['ssw810','2'],['Triangle567','2']]
        self.assertEqual(getRepositories('Tc-blip'), except_out) 


if __name__ == '__main__':
   
    unittest.main()  