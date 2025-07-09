#ifndef DBC_MACROS_H
#define DBC_MACROS_H

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

#define SET_ID(name, dst) \
    dst = name##_FRAME_ID

#define SET_DLC(name, dst) \
    dst = name##_LENGTH

#endif
