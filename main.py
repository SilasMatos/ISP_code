from fotocopia import FotoCopia
from impressora_multi_funcional import ImpressoraMultiFuncional
from impressora_simples import ImpressoraSimples
from imprimir import Imprimir
from scanner import Scanner


impressora_simples = ImpressoraSimples(Imprimir())
print(impressora_simples.imprimir())

impressora_multi_funcional = ImpressoraMultiFuncional(Imprimir(), Scanner(), FotoCopia())
print("\n" + impressora_multi_funcional.imprimir())
print(impressora_multi_funcional.scanner())
print(impressora_multi_funcional.fotocopia())