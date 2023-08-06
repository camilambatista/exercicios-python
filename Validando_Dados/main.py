from acesso_cep import BuscaEndereco
import requests


cep = 89220370

objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

