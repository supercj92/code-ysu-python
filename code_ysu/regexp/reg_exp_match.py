import traceback

from code_ysu.excel import load_excel
import re


def match_reg_exp():
    # texts = load_excel.load_data("/Users/chris/Downloads/IMAGE_ITEM_100query_0914.csv", "IMAGE_ITEM_100query_0914", 1,
    # 0)
    texts = []
    with open("/Users/chris/Downloads/IMAGE_ITEM_100query_0914.csv") as file:
        texts = file.readlines()

    pattern = re.compile("(ht|f)tp(s?)://.+\\.(jpg|png|bmp)")

    with open("./match_result.csv", "a+") as file:
        for text in texts:
            try:
                matcher = pattern.search(text)
                if matcher:
                    matched_text = matcher.group()
                    file.write("%s,%s\n" % (text, matched_text))
                else:
                    print("%s not match" % text)
            except Exception:
                traceback.print_exc()
                print("%s match fail" % text)


if __name__ == "__main__":
    match_reg_exp()
