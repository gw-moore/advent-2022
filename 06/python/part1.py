from pathlib import Path

path = Path(__file__).parents[1] / "data.txt"
buff = Path(path).read_text()


def id_start_of_packet_marker(buff: str):
    """Find the first 4 non-repeating character in a string and return the index at the start of the id"""

    buff_list = list(buff)
    counter = 0
    uid = ""
    # build the uid
    for _ in buff:
        while len(uid) < 5:
            counter += 1
            uid = uid + buff_list.pop(0)
        # once the uid is 4 character long, check if it is unique
        x = list(set(uid))
        y = list(uid)
        x.sort()
        y.sort()
        if x == y:
            return counter - 1, uid
        # if not unique, remove the first char from the string and start over
        uid = uid[1:]


index, uid = id_start_of_packet_marker(buff)
print(f"The index for the marker is: {index}")
print(f"The id is: {uid}")
