# Standard library imports...
from unittest.mock import Mock, patch
import unittest
from githubapi import get_repo_name,get_commits_num
import json

class Testgithubapi(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_repo_name(self,mock_get_repo):
        
        with open('richkempinski_repo.json') as fopen:
            data = json.load(fopen)
        mock_get_repo.return_value.json.return_value = data

        # Call the service, which will get a list of todos filtered on completed.
        getrepo = get_repo_name('richkempinski')

        # Confirm that the expected filtered list of todos was returned.
        self.assertEqual(getrepo, ['hellogitworld','helloworld','Mocks','Project1','threads-of-life'])

    @patch('requests.get')
    def test_get_commits_num(self,mock_get_commits_num):
        
        with open('richkempinski_commit.json') as fopen:
            data = json.load(fopen)
        mock_get_commits_num.return_value.json.return_value = data

        # Call the service, which will get a list of todos filtered on completed.
        getCommits = get_commits_num('richkempinski','hellogitworld')

        # Confirm that the expected filtered list of todos was returned.
        self.assertEqual(getCommits, 30)

    @patch('requests.get')
    def test_get_commits_num2(self,mock_get_commits_num):
        
        with open('helloworld.json') as fopen:
            data = json.load(fopen)
        mock_get_commits_num.return_value.json.return_value = data

        # Call the service, which will get a list of todos filtered on completed.
        getCommits = get_commits_num('richkempinski','helloworld')

        # Confirm that the expected filtered list of todos was returned.
        self.assertEqual(getCommits, 6)

if __name__ == '__main__':
   
    unittest.main(exit=False, verbosity=2) 