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
#if __has_include(<mcp2515.h>) || defined(TEST_PICO_2)

#define INIT_FRAME(frame, message) \
    struct can_frame message##_msg; \
    message##_msg.can_id = frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0); \
    message##_msg.can_dlc = frame##_LENGTH

#define CYCLIC_TRANSMITTER(frame, message, interface, timer) \
    timer.setInterval([&](){ \
        INIT_FRAME(frame, message); \
        INIT_MESSAGE(message); \
        encode_##message(message); \
        PACK_MESSAGE(message, message##_msg.data); \
        interface.sendMessage(&message##_msg); \
    }, frame##_CYCLE_TIME_MS)

#define READ_MESSAGE_CASE(frame, message) \
    case frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0): { \
        INIT_MESSAGE(message); \
        UNPACK_MESSAGE(message, msg.data); \
        decode_##message(message); \
        break; \
    }

#endif

#ifdef QT_VERSION

#define CAN_PROPERTY(type, name, defaultValue) \
    Q_PROPERTY(type name MEMBER name WRITE set_##name NOTIFY update) \

    public: \
        void set_##name(type value) { name = value; } \
        type get_##name() { return name; } \
    private: \
        type name = defaultValue; \
    public slots: \
    void set_##name(type value) { name = value; } \

#define SEND_FRAME(frame, message, interface) \
    QCanBusFrame message##_msg; \
    message##_msg.setFrameId(frame##_FRAME_ID); \
    uint8_t message##_payload[frame##_LENGTH] = {0}; \
    PACK_MESSAGE(message, message##_payload); \
    message##_msg.setPayload( \
        QByteArray(reinterpret_cast<char*>(message##_payload), sizeof(message##_payload)) \
    ); \
    interface->writeFrame(message##_msg)

#define READ_MESSAGE_CASE(frame, message) \
    case frame##_FRAME_ID: { \
        INIT_MESSAGE(message); \
        UNPACK_MESSAGE(message, data); \
        decode_##message(message); \
        break; \
    }

#endif
