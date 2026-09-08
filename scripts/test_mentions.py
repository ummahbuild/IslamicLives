"""External-format regression tests: fail closed on truncation and handle name spans."""
import unittest
from index_quran_mentions import parse_page

def page(start,end,total,refs):
 return f'Results <b>{start}</b> to <b>{end}</b> of <b>{total}</b>'+''.join(f'<a href="wordmorphology.jsp?location=({r})">name</a>' for r in refs)
class SourceFormatTests(unittest.TestCase):
 def test_truncated_page_rejected(self):
  with self.assertRaises(ValueError):parse_page(page(1,2,2,['2:31:2']))
 def test_multiword_name_is_one_match(self):
  total,words,_=parse_page(page(1,1,1,['38:48:4','38:48:5']),compound=True)
  self.assertEqual(total,1);self.assertEqual(len(words),2)
 def test_separate_verses_not_merged(self):
  total,words,_=parse_page(page(1,2,2,['21:85:4','21:85:5','38:48:4','38:48:5']),compound=True)
  self.assertEqual(total,2);self.assertEqual(len(words),4)
 def test_unexpected_document_rejected(self):
  with self.assertRaises(ValueError):parse_page('<html>Access denied</html>')
if __name__=='__main__':unittest.main()
