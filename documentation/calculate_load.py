import cantools

baud_rate = 1000
total_bps = 0

def message_throughput(message):
    frame_size = 47 + 20 * message.is_extended_frame

    attr = message.dbc.attributes.get('GenMsgCycleTime')
    if not attr:
        return 0

    cycle_time = int(attr.value)
    if cycle_time == 0:
        return 0

    frame_size += 8 * message.length
    frame_size *= 1.15

    return frame_size * 1000 / cycle_time

def print_throughput(name, bps):
    kbps = bps / 1000
    percentage = round((kbps / baud_rate) * 100, 3)
    print(f"{name:<22} {kbps:>8.2f} kbps {percentage:>8.2f} %")

for file in ["../dbc/haltech.dbc", "../dbc/tcs.dbc", "../dbc/swc.dbc", "../dbc/acc.dbc"]:
    db = cantools.database.load_file(file)
    
    bps = round(sum(message_throughput(msg) for msg in db.messages))
    total_bps += bps
    print_throughput(file, bps)

print_throughput(f"Total ({baud_rate} baud CAN)", total_bps)
