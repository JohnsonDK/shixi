def count_words(s, n):
    w = {}
    sp = s.split()
    for i in sp:
        if i not in w:
            w[i] = 1
        else:
            w[i] += 1

    top = sorted(w.items(), key=lambda item:(-item[1], item[0]))
    top_n = top[:n]
    return top_n


def test_run():
    print(count_words("I mean, think about music . music is all about repetition and patterns. If you didn’t have repetition in music , it would all just be noise.", 1))

if __name__ == '__main__':
    test_run()