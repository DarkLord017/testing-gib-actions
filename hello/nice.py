
from eth_utils import keccak

# Field types
types = ['address', 'address']
arguments = f'{",".join(types)}'

# Function definition
function_definition = f'getPair({arguments})'

# Function signature
function_signature = '0x' + keccak(text=function_definition).hex()[:8]

function_signature
#OK OK 
print(function_signature)
