import unittest
from datetime import date
import PromoMessage as PromoMsgClass


class TestPromoMessage(unittest.TestCase):

    msg = PromoMsgClass.Message()

    # Testar campos da mensagem
    def test_msg_fields(self):

        # Checar se mensagem válida é aceita
        self.assertEquals(self.msg.send_msg('Tester', 'Produto X', 'R$ 100,00', 'R$ 50,00'), 
            'Olá Tester, os seguintes produtos que você costuma consumir estão em promoção! Vem conferir: - Produto X: R$ 100,00 por R$ 50,00')
        
        # Checar se os valores de entrada incorretos são rejeitados
        with self.assertRaises(ValueError): 
            self.msg.send_msg( '', 'Produto X', 'R$ 100,00', 'R$ 50,00')
        with self.assertRaises(ValueError): 
            self.msg.send_msg('Tester', '', 'R$ 100,00', 'R$ 50,00')
        with self.assertRaises(ValueError):
             self.msg.send_msg('Tester', 'Produto X', '', 'R$ 50,00')
        with self.assertRaises(ValueError):
             self.msg.send_msg('Tester', 'Produto X', 'a', 'R$ 50,00')
        with self.assertRaises(ValueError):
             self.msg.send_msg('Tester', 'Produto X', 'R$ 100,00', '')
        with self.assertRaises(ValueError):
             self.msg.send_msg('Tester', 'Produto X', 'R$ 100,00', 'b')

        # Checar se tipos não esperados são rejeitados
        with self.assertRaises(TypeError):
             self.msg.send_msg(1, 'Produto X', 'R$ 100,00', 'R$ 50,00')
        with self.assertRaises(TypeError):
             self.msg.send_msg('Tester', None, 'R$ 100,00', 'R$ 50,00')
        with self.assertRaises(TypeError):
             self.msg.send_msg('Tester', 'Produto X', False, 'R$ 50,00')
        with self.assertRaises(TypeError):
             self.msg.send_msg('Tester', 'Produto X', 'R$ 100,00', None)

    # Testar entradas de período de compra
    def test_buying_period(self):

        # Checar se período válido é aceito
        self.assertTrue(self.msg.is_valid_period(90, 6))

        # Checar se período inválido é rejeitado
        self.assertFalse(self.msg.is_valid_period(5, 0))
        self.assertFalse(self.msg.is_valid_period(365, 91))

        # Checar se os valores de entrada incorretos ou na ordem errada são rejeitados
        with self.assertRaises(ValueError):
             self.msg.is_valid_period(6, 90)
        with self.assertRaises(ValueError):
             self.msg.is_valid_period(0, -1)

        # Checar se tipos não esperados são rejeitados
        with self.assertRaises(TypeError):
             self.msg.is_valid_period('abc', 6)
        with self.assertRaises(TypeError):
             self.msg.is_valid_period(90, True)
        with self.assertRaises(TypeError):
             self.msg.is_valid_period('', 6)
        with self.assertRaises(TypeError):
             self.msg.is_valid_period(90, None)
        with self.assertRaises(TypeError):
             self.msg.is_valid_period(90, 0.5)

    # Testar se informação de envio de mensagem fica salva
    def test_sent_msg(self):

        # Enviar mensagem
        self.msg.send_msg('Tester', 'Produto X', 'R$ 100,00', 'R$ 50,00')

        # Checar se alguma mensagem promocional foi enviada sobre um produto até a data de hoje
        self.assertTrue(self.msg.get_msg_sent('Tester', 'Produto X', date.today))

        # Checar se alguma mensagem foi enviada a outro cliente
        self.assertFalse(self.msg.get_msg_sent('Tester2', 'Produto X', date.today))

        # Checar se uma mensagem foi enviada ao cliente sobre outro produto
        self.assertFalse(self.msg.get_msg_sent('Tester', 'Produto Y', date.today))


