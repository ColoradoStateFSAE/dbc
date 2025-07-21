#pragma once

#define INIT_MESSAGE(message) \
    message##_t message; \
    message##_init(&message)

#define PACK_MESSAGE(message, dst) \
    message##_pack(dst, &message, sizeof(dst))

#define UNPACK_MESSAGE(message, src) \
    message##_unpack(&message, src, sizeof(src))

#define ENCODE_SIGNAL(message, signal, value) \
    message.signal = message##_##signal##_encode(value)

#define DECODE_SIGNAL(message, signal) \
    message##_##signal##_decode(message.signal)

#define IS_IN_RANGE(message, signal) \
    message##_##signal##_is_in_range(message.signal)

#define DECODE_METHOD(message) \
    decode_##message(const message##_t &message)

#define ENCODE_METHOD(message) \
    encode_##message(message##_t &message)

// Macros specific to https://github.com/autowp/arduino-mcp2515
#if defined(PICO_RP2350) || defined(TEST_PICO_2)

#define INIT_FRAME(frame, message) \
    struct can_frame message##_msg; \
    message##_msg.can_id = frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0); \
    message##_msg.can_dlc = frame##_LENGTH

#define CYCLIC_TRANSMITTER(frame, message) \
    timers.setInterval([&](){ \
        INIT_FRAME(frame, message); \
        INIT_MESSAGE(message); \
        encode_##message(message); \
        PACK_MESSAGE(message, message##_msg.data); \
        mcp.sendMessage(&message##_msg); \
    }, frame##_CYCLE_TIME_MS)

#define READ_MESSAGE_CASE(frame, message) \
    case frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0): { \
        INIT_MESSAGE(message); \
        UNPACK_MESSAGE(message, msg.data); \
        decode_##message(message); \
        break; \
    }

#endif
