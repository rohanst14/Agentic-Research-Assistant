from agentic_research_assistant import run,audit,Evidence
import unittest
class Tests(unittest.TestCase):
    def test_trace(self): self.assertEqual(run('heat',{'a':'heat rises'})['trace'],['retrieve','audit','synthesize'])
    def test_fake(self): self.assertEqual(audit([Evidence('a','fake',1)],{'a':'real'}),[])
    def test_abstain(self): self.assertEqual(run('heat',{'a':'cold'})['status'],'insufficient_evidence')
