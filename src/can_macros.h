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

#define DECODE_MESSAGE_H(message) \
    decode_##message(const message##_t &message, const unsigned int id = message##_frame_id)

#define DECODE_MESSAGE(message) \
    decode_##message(const message##_t &message)

#define SEND_MESSAGE_H(message) \
    send_##message(message##_t message = [](){ INIT_MESSAGE(message); return message; }())

#define SEND_MESSAGE(message) \
    send_##message(message##_t message)

// Macros specific to https://github.com/autowp/arduino-mcp2515
#if __has_include(<mcp2515.h>) || defined(TEST_PICO_2)

#define INIT_FRAME(message) \
    struct can_frame message##_msg; \
    message##_msg.can_id = message##_frame_id | (message##_is_extended ? CAN_EFF_FLAG : 0); \
    message##_msg.can_dlc = message##_length

#define READ_MESSAGE_CASE(message) \
    case message##_frame_id | (message##_is_extended ? CAN_EFF_FLAG : 0): { \
        INIT_MESSAGE(message); \
        UNPACK_MESSAGE(message, data); \
        decode_##message(message); \
        break; \
    }

#endif
