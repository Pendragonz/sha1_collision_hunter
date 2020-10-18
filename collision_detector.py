import hashlib, random, string, _thread, time

# Author Daniel Parekh @Pendragonz


# set to store all known hashes in
all_hashes = {"a", "b"}


# list to store pairs of string+values
pairs = []
seed = random.randrange(100000000000)
print("seed: " + str(seed))

r = random.Random(seed)


def cut_hash(message, length):
    m = bytes(message, "utf-8")
    sha1 = hashlib.sha1()
    sha1.update(m)
    dig = sha1.hexdigest()[:length]

    return dig


def main_loop(overlap):
    found = False
    attempts = 0
    while found is False:
        msg = ''.join(r.choice(string.ascii_letters) for _ in range(9))
        dig = cut_hash(msg, overlap)

        if dig in all_hashes:
            print("Overlap found!")
            print("M1: " + msg + " " + str(attempts) + " digit digest: " + dig)

            for i in pairs:
                if i[1] == dig:
                    print("M2: " + i[0] + " " + str(overlap) + " digit digest: " + i[1])

                    if i[0] == msg:
                        print("False alarm. Strings are the same. Continuing.")
                    else:
                        print("Overlap found in " + str(attempts) + " attempts!")
                        return

        if attempts < 38000000:
            all_hashes.add(dig)
            pairs.append((msg, dig))
        elif attempts == 38000000:
            print("No longer saving new hashes to save memory.")

        attempts += 1
        
        if attempts % 250000 == 0:
            print(str(attempts) + " attempts")



if __name__ == '__main__':
    print("Thank you for running Ram Consumer 3000 v2.1!")
    main_loop(15)

