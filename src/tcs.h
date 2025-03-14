/**
 * @file tcs.h
 *
 * @brief This header file was generated by cantools version 40.2.1 Fri Mar 14 23:09:57 2025.
 *
 * @copyright Copyright (c) 2018-2019 Erik Moqvist
 *
 * @par License
 * The MIT License (MIT)
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#ifndef TCS_H
#define TCS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifndef EINVAL
#    define EINVAL 22
#endif

/* Frame ids. */
#define TCS_SET_STATUS_FRAME_ID (0x65du)
#define TCS_SHIFT_CONTROLLER_FRAME_ID (0x65cu)
#define TCS_CLUTCH_FRAME_ID (0x659u)
#define TCS_SET_CLUTCH_FRAME_ID (0x65au)
#define TCS_ANALOG_INPUT_FRAME_ID (0x65bu)
#define TCS_SET_CLUTCH_SETTINGS_FRAME_ID (0x658u)
#define TCS_SET_SHIFT_SETTINGS_FRAME_ID (0x656u)
#define TCS_CLUTCH_SETTINGS_FRAME_ID (0x657u)
#define TCS_SHIFT_SETTINGS_FRAME_ID (0x655u)

/* Frame lengths in bytes. */
#define TCS_SET_STATUS_LENGTH (8u)
#define TCS_SHIFT_CONTROLLER_LENGTH (5u)
#define TCS_CLUTCH_LENGTH (4u)
#define TCS_SET_CLUTCH_LENGTH (4u)
#define TCS_ANALOG_INPUT_LENGTH (8u)
#define TCS_SET_CLUTCH_SETTINGS_LENGTH (8u)
#define TCS_SET_SHIFT_SETTINGS_LENGTH (8u)
#define TCS_CLUTCH_SETTINGS_LENGTH (8u)
#define TCS_SHIFT_SETTINGS_LENGTH (8u)

/* Extended or standard frame types. */
#define TCS_SET_STATUS_IS_EXTENDED (0)
#define TCS_SHIFT_CONTROLLER_IS_EXTENDED (0)
#define TCS_CLUTCH_IS_EXTENDED (0)
#define TCS_SET_CLUTCH_IS_EXTENDED (0)
#define TCS_ANALOG_INPUT_IS_EXTENDED (0)
#define TCS_SET_CLUTCH_SETTINGS_IS_EXTENDED (0)
#define TCS_SET_SHIFT_SETTINGS_IS_EXTENDED (0)
#define TCS_CLUTCH_SETTINGS_IS_EXTENDED (0)
#define TCS_SHIFT_SETTINGS_IS_EXTENDED (0)

/* Frame cycle times in milliseconds. */


/* Signal choices. */


/* Frame Names. */
#define TCS_SET_STATUS_NAME "set_status"
#define TCS_SHIFT_CONTROLLER_NAME "shift_controller"
#define TCS_CLUTCH_NAME "clutch"
#define TCS_SET_CLUTCH_NAME "set_clutch"
#define TCS_ANALOG_INPUT_NAME "analog_input"
#define TCS_SET_CLUTCH_SETTINGS_NAME "set_clutch_settings"
#define TCS_SET_SHIFT_SETTINGS_NAME "set_shift_settings"
#define TCS_CLUTCH_SETTINGS_NAME "clutch_settings"
#define TCS_SHIFT_SETTINGS_NAME "shift_settings"

/* Signal Names. */
#define TCS_SET_STATUS_ANTISTALL_NAME "antistall"
#define TCS_SET_STATUS_RPM_LIMITER_NAME "rpm_limiter"
#define TCS_SET_STATUS_OVER_REV_NAME "over_rev"
#define TCS_SHIFT_CONTROLLER_DOWN_NAME "down"
#define TCS_SHIFT_CONTROLLER_UP_NAME "up"
#define TCS_SHIFT_CONTROLLER_CLUTCH_RIGHT_NAME "clutch_right"
#define TCS_SHIFT_CONTROLLER_CLUTCH_LEFT_NAME "clutch_left"
#define TCS_CLUTCH_POSITION_NAME "position"
#define TCS_CLUTCH_POSITION_PERCENTAGE_NAME "position_percentage"
#define TCS_SET_CLUTCH_SET_POSITION_NAME "set_position"
#define TCS_SET_CLUTCH_SET_STATE_NAME "set_state"
#define TCS_ANALOG_INPUT_INPUT_RIGHT_TRAVEL_NAME "input_right_travel"
#define TCS_ANALOG_INPUT_INPUT_RIGHT_RAW_NAME "input_right_raw"
#define TCS_ANALOG_INPUT_INPUT_LEFT_TRAVEL_NAME "input_left_travel"
#define TCS_ANALOG_INPUT_INPUT_LEFT_RAW_NAME "input_left_raw"
#define TCS_SET_CLUTCH_SETTINGS_SET_START_NAME "set_start"
#define TCS_SET_CLUTCH_SETTINGS_SET_END_NAME "set_end"
#define TCS_SET_CLUTCH_SETTINGS_SET_FRICTION_NAME "set_friction"
#define TCS_SET_CLUTCH_SETTINGS_SET_AUTO_LAUNCH_NAME "set_auto_launch"
#define TCS_SET_SHIFT_SETTINGS_SET_UP_DELAY_NAME "set_up_delay"
#define TCS_SET_SHIFT_SETTINGS_SET_DOWN_DELAY_NAME "set_down_delay"
#define TCS_SET_SHIFT_SETTINGS_SET_OUTPUT_NAME "set_output"
#define TCS_SET_SHIFT_SETTINGS_SET_TIMEOUT_NAME "set_timeout"
#define TCS_CLUTCH_SETTINGS_START_NAME "start"
#define TCS_CLUTCH_SETTINGS_END_NAME "end"
#define TCS_CLUTCH_SETTINGS_FRICTION_NAME "friction"
#define TCS_CLUTCH_SETTINGS_AUTO_LAUNCH_NAME "auto_launch"
#define TCS_SHIFT_SETTINGS_UP_DELAY_NAME "up_delay"
#define TCS_SHIFT_SETTINGS_DOWN_DELAY_NAME "down_delay"
#define TCS_SHIFT_SETTINGS_OUTPUT_NAME "output"
#define TCS_SHIFT_SETTINGS_TIMEOUT_NAME "timeout"

/**
 * Signals in message set_status.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_set_status_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint8_t antistall;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint8_t rpm_limiter;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint8_t over_rev;
};

/**
 * Signals in message shift_controller.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_shift_controller_t {
    /**
     * Range: 0..1 (0..1 -)
     * Scale: 1
     * Offset: 0
     */
    int8_t down;

    /**
     * Range: 0..1 (0..1 -)
     * Scale: 1
     * Offset: 0
     */
    int8_t up;

    /**
     * Range: -
     * Scale: 0.01
     * Offset: 0
     */
    int16_t clutch_right;

    /**
     * Range: -
     * Scale: 0.01
     * Offset: 0
     */
    int16_t clutch_left;
};

/**
 * Signals in message clutch.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_clutch_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t position;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t position_percentage;
};

/**
 * Signals in message set_clutch.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_set_clutch_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_position;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_state;
};

/**
 * Signals in message analog_input.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_analog_input_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t input_right_travel;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t input_right_raw;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t input_left_travel;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t input_left_raw;
};

/**
 * Signals in message set_clutch_settings.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_set_clutch_settings_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_start;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_end;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_friction;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_auto_launch;
};

/**
 * Signals in message set_shift_settings.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_set_shift_settings_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_up_delay;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_down_delay;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_output;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t set_timeout;
};

/**
 * Signals in message clutch_settings.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_clutch_settings_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t start;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t end;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t friction;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t auto_launch;
};

/**
 * Signals in message shift_settings.
 *
 * All signal values are as on the CAN bus.
 */
struct tcs_shift_settings_t {
    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t up_delay;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t down_delay;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t output;

    /**
     * Range: -
     * Scale: 1
     * Offset: 0
     */
    uint16_t timeout;
};

/**
 * Pack message set_status.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_set_status_pack(
    uint8_t *dst_p,
    const struct tcs_set_status_t *src_p,
    size_t size);

/**
 * Unpack message set_status.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_set_status_unpack(
    struct tcs_set_status_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from set_status.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_set_status_init(struct tcs_set_status_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint8_t tcs_set_status_antistall_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_status_antistall_decode(uint8_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_status_antistall_is_in_range(uint8_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint8_t tcs_set_status_rpm_limiter_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_status_rpm_limiter_decode(uint8_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_status_rpm_limiter_is_in_range(uint8_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint8_t tcs_set_status_over_rev_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_status_over_rev_decode(uint8_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_status_over_rev_is_in_range(uint8_t value);

/**
 * Pack message shift_controller.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_shift_controller_pack(
    uint8_t *dst_p,
    const struct tcs_shift_controller_t *src_p,
    size_t size);

/**
 * Unpack message shift_controller.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_shift_controller_unpack(
    struct tcs_shift_controller_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from shift_controller.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_shift_controller_init(struct tcs_shift_controller_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
int8_t tcs_shift_controller_down_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_controller_down_decode(int8_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_controller_down_is_in_range(int8_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
int8_t tcs_shift_controller_up_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_controller_up_decode(int8_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_controller_up_is_in_range(int8_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
int16_t tcs_shift_controller_clutch_right_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_controller_clutch_right_decode(int16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_controller_clutch_right_is_in_range(int16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
int16_t tcs_shift_controller_clutch_left_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_controller_clutch_left_decode(int16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_controller_clutch_left_is_in_range(int16_t value);

/**
 * Pack message clutch.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_clutch_pack(
    uint8_t *dst_p,
    const struct tcs_clutch_t *src_p,
    size_t size);

/**
 * Unpack message clutch.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_clutch_unpack(
    struct tcs_clutch_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from clutch.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_clutch_init(struct tcs_clutch_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_position_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_position_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_position_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_position_percentage_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_position_percentage_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_position_percentage_is_in_range(uint16_t value);

/**
 * Pack message set_clutch.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_set_clutch_pack(
    uint8_t *dst_p,
    const struct tcs_set_clutch_t *src_p,
    size_t size);

/**
 * Unpack message set_clutch.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_set_clutch_unpack(
    struct tcs_set_clutch_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from set_clutch.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_set_clutch_init(struct tcs_set_clutch_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_set_position_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_set_position_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_set_position_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_set_state_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_set_state_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_set_state_is_in_range(uint16_t value);

/**
 * Pack message analog_input.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_analog_input_pack(
    uint8_t *dst_p,
    const struct tcs_analog_input_t *src_p,
    size_t size);

/**
 * Unpack message analog_input.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_analog_input_unpack(
    struct tcs_analog_input_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from analog_input.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_analog_input_init(struct tcs_analog_input_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_analog_input_input_right_travel_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_analog_input_input_right_travel_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_analog_input_input_right_travel_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_analog_input_input_right_raw_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_analog_input_input_right_raw_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_analog_input_input_right_raw_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_analog_input_input_left_travel_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_analog_input_input_left_travel_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_analog_input_input_left_travel_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_analog_input_input_left_raw_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_analog_input_input_left_raw_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_analog_input_input_left_raw_is_in_range(uint16_t value);

/**
 * Pack message set_clutch_settings.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_set_clutch_settings_pack(
    uint8_t *dst_p,
    const struct tcs_set_clutch_settings_t *src_p,
    size_t size);

/**
 * Unpack message set_clutch_settings.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_set_clutch_settings_unpack(
    struct tcs_set_clutch_settings_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from set_clutch_settings.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_set_clutch_settings_init(struct tcs_set_clutch_settings_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_settings_set_start_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_settings_set_start_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_settings_set_start_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_settings_set_end_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_settings_set_end_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_settings_set_end_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_settings_set_friction_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_settings_set_friction_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_settings_set_friction_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_clutch_settings_set_auto_launch_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_clutch_settings_set_auto_launch_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_clutch_settings_set_auto_launch_is_in_range(uint16_t value);

/**
 * Pack message set_shift_settings.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_set_shift_settings_pack(
    uint8_t *dst_p,
    const struct tcs_set_shift_settings_t *src_p,
    size_t size);

/**
 * Unpack message set_shift_settings.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_set_shift_settings_unpack(
    struct tcs_set_shift_settings_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from set_shift_settings.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_set_shift_settings_init(struct tcs_set_shift_settings_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_shift_settings_set_up_delay_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_shift_settings_set_up_delay_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_shift_settings_set_up_delay_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_shift_settings_set_down_delay_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_shift_settings_set_down_delay_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_shift_settings_set_down_delay_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_shift_settings_set_output_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_shift_settings_set_output_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_shift_settings_set_output_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_set_shift_settings_set_timeout_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_set_shift_settings_set_timeout_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_set_shift_settings_set_timeout_is_in_range(uint16_t value);

/**
 * Pack message clutch_settings.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_clutch_settings_pack(
    uint8_t *dst_p,
    const struct tcs_clutch_settings_t *src_p,
    size_t size);

/**
 * Unpack message clutch_settings.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_clutch_settings_unpack(
    struct tcs_clutch_settings_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from clutch_settings.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_clutch_settings_init(struct tcs_clutch_settings_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_settings_start_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_settings_start_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_settings_start_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_settings_end_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_settings_end_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_settings_end_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_settings_friction_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_settings_friction_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_settings_friction_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_clutch_settings_auto_launch_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_clutch_settings_auto_launch_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_clutch_settings_auto_launch_is_in_range(uint16_t value);

/**
 * Pack message shift_settings.
 *
 * @param[out] dst_p Buffer to pack the message into.
 * @param[in] src_p Data to pack.
 * @param[in] size Size of dst_p.
 *
 * @return Size of packed data, or negative error code.
 */
int tcs_shift_settings_pack(
    uint8_t *dst_p,
    const struct tcs_shift_settings_t *src_p,
    size_t size);

/**
 * Unpack message shift_settings.
 *
 * @param[out] dst_p Object to unpack the message into.
 * @param[in] src_p Message to unpack.
 * @param[in] size Size of src_p.
 *
 * @return zero(0) or negative error code.
 */
int tcs_shift_settings_unpack(
    struct tcs_shift_settings_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Init message fields to default values from shift_settings.
 *
 * @param[in] msg_p Message to init.
 *
 * @return zero(0) on success or (-1) in case of nullptr argument.
 */
int tcs_shift_settings_init(struct tcs_shift_settings_t *msg_p);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_shift_settings_up_delay_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_settings_up_delay_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_settings_up_delay_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_shift_settings_down_delay_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_settings_down_delay_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_settings_down_delay_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_shift_settings_output_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_settings_output_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_settings_output_is_in_range(uint16_t value);

/**
 * Encode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to encode.
 *
 * @return Encoded signal.
 */
uint16_t tcs_shift_settings_timeout_encode(double value);

/**
 * Decode given signal by applying scaling and offset.
 *
 * @param[in] value Signal to decode.
 *
 * @return Decoded signal.
 */
double tcs_shift_settings_timeout_decode(uint16_t value);

/**
 * Check that given signal is in allowed range.
 *
 * @param[in] value Signal to check.
 *
 * @return true if in range, false otherwise.
 */
bool tcs_shift_settings_timeout_is_in_range(uint16_t value);


#ifdef __cplusplus
}
#endif

#endif
