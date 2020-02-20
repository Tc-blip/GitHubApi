
import unittest
from githubapi import getRepositories


class Testgithubapi(unittest.TestCase):
    def testgetRepositories(self):
        except_out = [['Convenience-system',11],['GitHubApi',18],['Github_issue_spyder',17],['ssw540',4],['SSW555',30],['SSW567hw',16],['SSW695',24],['ssw810',2],['Triangle567',3]]
        self.assertEqual(getRepositories('Tc-blip'), except_out) 

        except_out2 = [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]]
        self.assertEqual(getRepositories('richkempinski'), except_out2)

if __name__ == '__main__':
   
    unittest.main()  