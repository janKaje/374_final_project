def summary(arr, msg):
    """Takes an array of solutions and returns appropriate text that summarizes it."""
    maxlen = [9, 9, 18, 11, 28, 10, 10, 19]
    rounded = [[round(item, 2) if isinstance(item, float) else item for item in sublist] for sublist in arr]
    roundedtwice = [[[round(subitem, 2) for subitem in item] if isinstance(item, list) else item for item in sublist]
                    for sublist in rounded]

    for i, sublist in enumerate(arr):
        for j, item in enumerate(sublist):
            try:
                if len(str(roundedtwice[i][j])) > maxlen[j]:
                    maxlen[j] = len(str(roundedtwice[i][j]))
            except Exception as ex:
                print(i, j, item)
                raise ex

    txt = "\n" + "-" * (5 + sum(maxlen)) + "\n"
    txt += msg + "\n"
    txt += "-" * (5 + sum(maxlen)) + "\n"
    txt += f"|Diameters{' ' * (maxlen[0] - 9)}|Pump Type{' ' * (maxlen[1] - 9)}|Number of Pumps{' ' * (maxlen[2] - 15)}" \
           + f"|System Cost{' ' * (maxlen[3] - 11)}|Operating Cost (1 month max){' ' * (maxlen[4] - 28)}" \
           + f"|Flow Rates{' ' * (maxlen[5] - 10)}|Total Flow{' ' * (maxlen[6] - 10)}|Total Head Required{' ' * (maxlen[7] - 19)}|\n"
    txt += f"| in{' ' * (maxlen[0] - 3)}|{' ' * maxlen[1]}| series, parallel {' ' * (maxlen[2] - 18)}" \
           + f"| ${' ' * (maxlen[3] - 2)}| ${' ' * (maxlen[4] - 2)}" \
           + f"| gal/min{' ' * (maxlen[5] - 8)}| gal/min{' ' * (maxlen[6] - 8)}| ft{' ' * (maxlen[7] - 3)}|\n"
    txt += f"|{'-' * maxlen[0]}|{'-' * maxlen[1]}|{'-' * maxlen[2]}|{'-' * maxlen[3]}|{'-' * maxlen[4]}|{'-' * maxlen[5]}|{'-' * maxlen[6]}|{'-' * maxlen[7]}|\n"
    for sublist in roundedtwice:
        txt += f"|{str(sublist[0])}{' ' * (maxlen[0] - len(str(sublist[0])))}"
        txt += f"|{str(sublist[1])}{' ' * (maxlen[1] - len(str(sublist[1])))}"
        txt += f"|{str(sublist[2])}{' ' * (maxlen[2] - len(str(sublist[2])))}"
        txt += f"|{str(sublist[3])}{' ' * (maxlen[3] - len(str(sublist[3])))}"
        txt += f"|{str(sublist[4])}{' ' * (maxlen[4] - len(str(sublist[4])))}"
        txt += f"|{str(sublist[5])}{' ' * (maxlen[5] - len(str(sublist[5])))}"
        txt += f"|{str(sublist[6])}{' ' * (maxlen[6] - len(str(sublist[6])))}"
        txt += f"|{str(sublist[7])}{' ' * (maxlen[7] - len(str(sublist[7])))}|\n"
    txt += "\n"

    return txt

def time_str(time):
    """Takes a float of seconds and turns it into appropriate hours, minutes, and seconds.
    Really just for easy reading. Not important to assignment."""
    st = ""
    if time // 3600 > 1:
        st += str(time // 3600) + ' hours'
    elif time // 3600 > 0:
        st += str(time // 3600) + ' hour'


    if time % 3600 // 60 > 0 or time // 3600 > 0:
        if time // 3600 > 0:
            st += ', ' + str(time % 3600 // 60) + ' minute'
        else:
            st += str(time // 60) + ' minute'
        if time % 3600 // 60 > 1 or time // 3600 > 0:
            st += "s"

    if time % 60 > 0 or time % 3600 // 60 > 0:
        if time % 3600 // 60 > 0 or time // 3600 > 0:
            st += ', ' + str(time % 60) + ' second'
        else:
            st += str(time % 60) + ' second'
        if time % 60 > 1 or time % 60 == 0:
            st += "s"

    return st

if __name__ == "__main__":
    print(time_str(121))