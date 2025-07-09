#ifndef CAN_MACROS_H
#define CAN_MACROS_H

#define INIT_MESSAGE(name) \
    name##_t name; \
    name##_init(&name)

#define PACK_MESSAGE(name, dst) \
    name##_pack(dst, &name, sizeof(dst))

#define UNPACK_MESSAGE(name, src) \
    name##_unpack(&name, src, sizeof(src))

#define ENCODE_SIGNAL(name, signal, value) \
    name.signal = name##_##signal##_encode(value)

#define DECODE_SIGNAL(name, signal) \
    name##_##signal##_decode(name.signal)

#endif
