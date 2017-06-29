import unittest

from dna_subsequence import subsequence


class DNATests(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(subsequence(['', '']), '')

    def test_empty_subsequence(self):
        self.assertEqual(subsequence(['accaacaacacc', 'tggtggggttgtt']), '')

    def test_same_strand(self):
        self.assertEqual(subsequence(['taggcta', 'taggcta']),
                         'taggcta')
        
    def test_more_than_one_possible_subsequences(self):
        self.assertEqual(subsequence(['agtc', 'gact']),
                         'at')

    def test_short_strands1(self):
        self.assertEqual(subsequence(['gtcatgcttaggcta','agcatgctgcag']),
                         'gcatgctgca')
        
    def test_short_strands2(self):
        self.assertEqual(subsequence(['taccaacaacacc','tggtggcggttgtt']),
                         'tc')

    def test_long_strands1(self):
        self.assertEqual(subsequence(['accggtcgagtgcgcggaagccggccgaa',
                                   'gtcgttcggaatgccgttgctctgtaaa']),
                         'gtcgtcggaagccggccgaa')
        
    def test_long_strands2(self):
        self.assertEqual(subsequence(['gatccatctggatcctatagttcatggaaagccgctgc',
                                  'tatttcaacattaattgttggttttgatacagatggtacacca']),
                         'atccattggttatagatggaacc')

if __name__ == '__main__':
    unittest.main()
