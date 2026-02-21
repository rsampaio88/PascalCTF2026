import socket
import re
import numpy as np

def parse(equation):
    left, right = equation.split(' = ')
    right_val = int(right.strip())
    
    pattern = r'([+-]?\d*)\*x_(\d+)'
    matches = re.findall(pattern, left)
    
    coeffs = [0]*28
    for coeff_str, idx_str in matches:
        idx = int(idx_str)
        if coeff_str == '' or coeff_str == '+':
            coeff = 1
        elif coeff_str == '-':
            coeff = -1
        else:
            coeff = int(coeff_str)
        coeffs[idx] = coeff
    
    return coeffs, right_val

HOST = "cramer.ctf.pascalctf.it"
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    equations_text = data.decode('utf-8')

lines = equations_text.strip().split('\n')
equations = [line for line in lines if 'x_0' in line]

A = []
B = []
for eq in equations:
    c, r = parse(eq)
    A.append(c)
    B.append(r)

print(f"Matrix shape: {len(A)} x {len(A[0])}")
print(f"B length: {len(B)}")

A_np = np.array(A, dtype=np.float64)
B_np = np.array(B, dtype=np.float64)
sol = np.linalg.solve(A_np, B_np)
flag_inner = ''.join(chr(int(round(x))) for x in sol)
flag = f"pascalCTF{{{flag_inner}}}"
print("Flag:", flag)