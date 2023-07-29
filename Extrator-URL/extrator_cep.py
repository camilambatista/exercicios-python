endereco = "Rua das Flores, 72, apartamento 1002, Laranajeiras, Rio de Janeiro, RJ, 23440201"

import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}-?[0-9]{3}")
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group()
    print(cep)

