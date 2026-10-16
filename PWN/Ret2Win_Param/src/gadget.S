.section .text
.global gadget_pop_rdi
.type gadget_pop_rdi, @function

gadget_pop_rdi:
    pop %rdi
    ret

.section .note.GNU-stack,"",@progbits