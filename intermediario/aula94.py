# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero')
except IndexError:
    print('IndeError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('NÃO HOUVE ERRO')
finally:
    print('FECHAR ARQUIVO')