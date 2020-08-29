
from block import Block
import datetime

class Blockchain:
    def __init__():
        block_chain = [Block.create_genesis_block()]
        print("El bloque genesis ha sido creado.")
        print("Hash: %s" % block_chain[0].hash)
        i = 1

    def write_block(i):
        datos = str("Numero de bloque %d \n" % i)
        datos += input("Dame un contrato: \n")
        block_chain.append(Block(block_chain[i-1].hash,
                                 datos,
                                 datetime.datetime.now()))

        print("Bloque #%d creado." % i)
        print("Hash: %s" % block_chain[-1].hash)
        if input("¿Quieres agregar otro bloque? [s/n]\n") in ["N","n"]:
            return 0
        return i+1



    def read_block(i):
        try:
            block_number = int(input("dame el numero del bloque que quieres buscar:\n"))
            print("\n" + block_chain[block_number].data + "\n")
        except:
            print("Ese bloque no existe")
        finally:
            if input("¿Quieres algun otro bloque? [s/n]\n") in ["N","n"]:
                return
