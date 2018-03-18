import unittest
from GitRepositoryUri import GitRepositoryUri
class GitRepositoryUriTest(unittest.TestCase):
    def test_has_attr(self):
        self.assertTrue(hasattr(GitRepositoryUri(), 'ToHttps'))
        self.assertTrue(hasattr(GitRepositoryUri(), 'ToSsh'))
        self.assertTrue(hasattr(GitRepositoryUri(), 'From'))

    def test_to_https_A(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        self.assertEqual("https://github.com/{}/{}.git".format(user, repo), GitRepositoryUri().ToHttps(user, repo))
    def test_to_https_B(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        pw = 'PASS_WORD'
        self.assertEqual("https://{0}:{2}@github.com/{0}/{1}.git".format(user, repo, pw), GitRepositoryUri().ToHttps(user, repo, pw))
    def test_to_ssh_A(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        self.assertEqual("git@{}:{}/{}.git".format(host, user, repo), GitRepositoryUri().ToSsh(host, user, repo))

    def test_from_https_A(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "https://github.com/{}/{}.git".format(user, repo)
        res = GitRepositoryUri().From(url)
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_https_B(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        pw = 'PASS_WORD'
        url = "https://{0}:{2}@github.com/{0}/{1}.git".format(user, repo, pw)
        res = GitRepositoryUri().From(url)
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertTrue('pass' in res.keys())
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
        self.assertEqual(pw, res['pass'])

    def test_from_ssh_A(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "git@{}:{}/{}.git".format(host, user, repo)
        res = GitRepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_ssh_B1(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "ssh://git@{}/{}/{}.git".format(host, user, repo)
        res = GitRepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_ssh_B2(self):
        host = 'ytyaru0.github.com'
        port = '22'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "ssh://git@{}:{}/{}/{}.git".format(host, port, user, repo)
        res = GitRepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('port' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(port, res['port'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])


if __name__ == '__main__':
    unittest.main()
