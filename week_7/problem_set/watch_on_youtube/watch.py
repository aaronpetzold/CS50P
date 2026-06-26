import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(
        r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(?P<video_id>\w+)"', s
    ):
        sharable = f"https://youtu.be/{match.group("video_id")}"
        return sharable
    else:
        return None


if __name__ == "__main__":
    main()
