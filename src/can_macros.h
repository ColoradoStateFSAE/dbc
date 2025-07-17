#pragma once

/**
 * @brief Creates a dbc_message_t struct initialized with zeros.
 *
 *
 * @param message The name of a message.
 */
#define INIT_MESSAGE(message) \
    message##_t message; \
    message##_init(&message)

/**
 * @brief Encodes a signal into a dbc_message_t struct.
 *
 *
 * @param message The name of a message.
 * @param signal The name of a signal.
 * @param value Value to be encoded using the signal format.
 */
#define ENCODE_SIGNAL(message, signal, value) \
    message.signal = message##_##signal##_encode(value)

/**
 * @brief Decodes a signal from a dbc_message_t struct.
 *
 *
 * @param message The name of a message.
 * @param signal The name of a signal.
 * @return The decoded value.
 */
#define DECODE_SIGNAL(message, signal) \
    message##_##signal##_decode(message.signal)

/**
 * @brief Pack message.
 *
 *
 * @param message The name of a message.
 * @param dst Object to pack the message into.
 */
#define PACK_MESSAGE(message, dst) \
    message##_pack(dst, &message, sizeof(dst))

/**
 * @brief Unpack message.
 *
 *
 * @param message The name of a message.
 * @param dst Object to unpack the message into.
 */
#define UNPACK_MESSAGE(message, src) \
    message##_unpack(&message, src, sizeof(src))

/**
 * @brief Check that given signal is in allowed range.
 *
 *
 * @param message The name of a message.
 * @param signal The name of a signal.
 */
#define IS_IN_RANGE(message, signal) \
    message##_##signal##_is_in_range(message.signal)

/**
 * @brief A function name to read a message.
 *
 *
 * @param message The name of a message.
 */
#define READ_MESSAGE(message) \
    read_##message(const message##_t &message)

/**
 * @brief A function name to send a message.
 *
 *
 * @param message The name of a message.
 */
#define SEND_MESSAGE(message) \
    send_##message()

#ifdef _MCP2515_H_

/**
 * @brief Creates a if statement to call an accompanying READ_MESSAGE() function.
 *
 *
 * @param frame The uppercase name of a message.
 * @param message The name of a message.
 * @param src Object to unpack into the message.
 */

#define FRAME_MASK(is_extended) ((is_extended) ? CAN_EFF_MASK : CAN_SFF_MASK)

#define READ_MESSAGE_CASE(frame, message, src) \
    if (msg.can_id == (frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0))) { \
        INIT_MESSAGE(message); \
        UNPACK_MESSAGE(message, src); \
        read_##message(message); \
    }

#define INIT_FRAME(message, frame) \
    struct can_frame message##_msg; \
    message##_msg.can_id = frame##_FRAME_ID | (frame##_IS_EXTENDED ? CAN_EFF_FLAG : 0); \
    message##_msg.can_dlc = frame##_LENGTH

#define SEND_FRAME(message, interface) \
    interface.sendMessage(&message##_msg);

#endif
