import sys


def count_words(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for ch in ",.!?;:":
        text = text.replace(ch, " ")
    words = text.split()
    freq = {}
    for w in words:
        w = w.lower()
        freq[w] = freq.get(w, 0) + 1
    return freq


def main():
    if len(sys.argv) < 2:
        print("usage: python code/text_stats.py <file>")
        sys.exit(1)
    freq = count_words(sys.argv[1])
    for w, c in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{w}\t{c}")
    print(f"total unique words: {len(freq)}")


if __name__ == "__main__":
    main()
