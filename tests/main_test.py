from betacode_parser import *
import unittest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

class TestBetaConversions(unittest.TestCase):
    def test_beta_to_coptic(self):
        self.assertEqual(beta_to_coptic("*A"), "Ⲁ")
        self.assertEqual(beta_to_coptic("*NOUTON"), "Ⲛⲟⲩⲧⲟⲛ") 
        self.assertEqual(beta_to_coptic("XHMAIRA"), "ⲭⲏⲙⲁⲓⲣⲁ")
        self.assertEqual(beta_to_coptic("*A*B*G*D*E*V*Z*H*Q*I*K*L*M*N*C*O*P*R*S*T*U*F*X*Y*W*s*f*h*j*g*tABGDEVZHQIKLMNCOPRSTUFXYWsfhjgt"), "ⲀⲂⲄⲆⲈⲊⲌⲎⲐⲒⲔⲖⲘⲚⲜⲞⲠⲢⲤⲦⲨⲪⲬⲮⲰϢϤϨϪϬϮⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡⲣⲥⲧⲩⲫⲭⲯⲱϣϥϩϫϭϯ")
        self.assertEqual(beta_to_coptic(""), "")
        self.assertEqual(beta_to_coptic("123"), "123")

    def test_coptic_to_beta(self):
        self.assertEqual(coptic_to_beta("Ⲁ"), "*A")
        self.assertEqual(coptic_to_beta("Ⲛⲟⲩⲧⲟⲛ"), "*NOUTON") 
        self.assertEqual(coptic_to_beta("ⲭⲏⲙⲁⲓⲣⲁ"), "XHMAIRA")
        self.assertEqual(coptic_to_beta("ⲀⲂⲄⲆⲈⲊⲌⲎⲐⲒⲔⲖⲘⲚⲜⲞⲠⲢⲤⲦⲨⲪⲬⲮⲰϢϤϨϪϬϮⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡⲣⲥⲧⲩⲫⲭⲯⲱϣϥϩϫϭϯ"), "*A*B*G*D*E*V*Z*H*Q*I*K*L*M*N*C*O*P*R*S*T*U*F*X*Y*W*s*f*h*j*g*tABGDEVZHQIKLMNCOPRSTUFXYWsfhjgt")
        self.assertEqual(coptic_to_beta(""), "")
        self.assertEqual(coptic_to_beta("123"), "123")

    def test_beta_to_greek(self):
        self.assertEqual(beta_to_greek("*A"), "Α")
        self.assertEqual(beta_to_greek("*A)RIS1TOTE/LHS"), "Ἀριστοτέλης")
        self.assertEqual(beta_to_greek("*O(/MHROS"), "Ὅμηρος")
        self.assertEqual(beta_to_greek("*A*B*G*D*E*V*Z*H*Q*I*K*L*M*N*C*O*P*R*S3*S*T*U*F*X*Y*WABGDEVZHQIKLMNCOPRS3S1S2TUFXYW:#"), "ΑΒΓΔΕϜΖΗΘΙΚΛΜΝΞΟΠΡϹΣΤΥΦΧΨΩαβγδεϝζηθικλμνξοπρϲσςτυφχψω·ʹ")
        self.assertEqual(beta_to_greek(""), "")
        self.assertEqual(beta_to_greek("123"), "123")

    def test_greek_to_beta(self):
        self.assertEqual(greek_to_beta("Α"), "*A")
        self.assertEqual(greek_to_beta("Ἀριστοτέλης"), "*A)RIS1TOTE/LHS2")
        self.assertEqual(greek_to_beta("Ὅμηρος"), "*O(/MHROS2")
        self.assertEqual(greek_to_beta("ΑΒΓΔΕϜΖΗΘΙΚΛΜΝΞΟΠΡϹΣΤΥΦΧΨΩαβγδεϝζηθικλμνξοπρϲσςτυφχψω·ʹ"), "*A*B*G*D*E*V*Z*H*Q*I*K*L*M*N*C*O*P*R*S3*S*T*U*F*X*Y*WABGDEVZHQIKLMNCOPRS3S1S2TUFXYW:#")
        self.assertEqual(greek_to_beta(""), "")
        self.assertEqual(greek_to_beta("123"), "123")

    def test_beta_to_hebrew(self):
        self.assertEqual(beta_to_hebrew("b"), "ב")
        self.assertEqual(beta_to_hebrew("slvm2"), "שלום")
        self.assertEqual(beta_to_hebrew("m1m1lk1h"), "ממלכה") 
        self.assertEqual(beta_to_hebrew("Hk1m1h"), "חכמה")
        self.assertEqual(beta_to_hebrew("Adm2"), "אדם")
        self.assertEqual(beta_to_hebrew("ArT2"), "ארץ")
        self.assertEqual(beta_to_hebrew("yvm2"), "יום") 
        self.assertEqual(beta_to_hebrew(""), "")
        self.assertEqual(beta_to_hebrew("123"), "123")

    def test_hebrew_to_beta(self):
        self.assertEqual(hebrew_to_beta("ב"), "b")
        self.assertEqual(hebrew_to_beta("שָׁלוֹם"), "slvm2")
        self.assertEqual(hebrew_to_beta("ממלכה"), "m1m1lk1h")
        self.assertEqual(hebrew_to_beta("חכמה"), "Hk1m1h")
        self.assertEqual(hebrew_to_beta("אדם"), "Adm2")
        self.assertEqual(hebrew_to_beta("ארץ"), "ArT2")
        self.assertEqual(hebrew_to_beta("יום"), "yvm2")
        self.assertEqual(hebrew_to_beta(""), "")
        self.assertEqual(hebrew_to_beta("123"), "123")

    def test_beta_to_hebrew_old(self):
        self.assertEqual(beta_to_hebrew("B", True), "ב")
        self.assertEqual(beta_to_hebrew("$LWM", True), "שׁלום")
        self.assertEqual(beta_to_hebrew("MMLKH", True), "ממלכה") 
        self.assertEqual(beta_to_hebrew("XKMH", True), "חכמה")
        self.assertEqual(beta_to_hebrew(")DM", True), "אדם")
        self.assertEqual(beta_to_hebrew(")RC", True), "ארץ")
        self.assertEqual(beta_to_hebrew("YWM", True), "יום") 
        self.assertEqual(beta_to_hebrew("", True), "")
        self.assertEqual(beta_to_hebrew("123", True), "123")

    def test_hebrew_to_beta_old(self):
        self.assertEqual(hebrew_to_beta("ב", True), "B")
        self.assertEqual(hebrew_to_beta("שָׁלוֹם", True), "$LWM")
        self.assertEqual(hebrew_to_beta("ממלכה", True), "MMLKH")
        self.assertEqual(hebrew_to_beta("חכמה", True), "XKMH")
        self.assertEqual(hebrew_to_beta("אדם", True), ")DM")
        self.assertEqual(hebrew_to_beta("ארץ", True), ")RC")
        self.assertEqual(hebrew_to_beta("יום", True), "YWM")
        self.assertEqual(hebrew_to_beta("", True), "")
        self.assertEqual(hebrew_to_beta("123", True), "123")

if __name__ == "__main__":
    unittest.main()
