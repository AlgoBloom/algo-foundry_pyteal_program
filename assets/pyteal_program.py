# Contract Account

# Add directory to path so that algobpy can be imported
import sys
sys.path.insert(0,'.')

from algobpy.parse import parse_params
from pyteal import *

def main(RECEIVER_1, RECEIVER_2):

    # Write your code here
    program = If(Txn.receiver() == Addr(RECEIVER_1)).Then(And((Txn.arg[0] == Bytes("rcv1password")),(Txn.amount() <= Int(5)))).ElseIf(Txn.receiver() == Addr(RECEIVER_2)).Then(And((Txn.arg[0] == Bytes("rcv2password")),(Txn.amount() <= Int(10))))

    return program

if __name__ == "__main__":
    params = {
        "RECEIVER_1": "R4VDREHBHVETKRPBZT6IDOQQL4FBHLBYQBQQJPIBXLTCVXYJX7Z5WLDSZY",
        "RECEIVER_2": "WRBVLPUHQZ5O2UIZAKYKKMOUSNPOFIL6ALUZQZLHBDUSIKXHAEEIELWBFQ",
    }

    # Overwrite params if sys.argv[1] is passed
    if(len(sys.argv) > 1):
        params = parse_params(sys.argv[1], params)

    print(compileTeal(main(params["RECEIVER_1"], params["RECEIVER_2"]), Mode.Signature, version=6))
