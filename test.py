from utils import get_config, extract

if __name__ == "__main__":
    patterns = get_config()["patterns"]
    assert(extract(patterns, " some text github.com/username-HERE123") == ["github.com/username-HERE123"])
    assert(extract(patterns, " some text gitlab.com/test0, and gitlab.com/test1") == ["gitlab.com/test0", "gitlab.com/test1"])
    assert(extract(patterns, " my-name-is.github.io a") == ["my-name-is.github.io"])
    assert(extract(patterns, " GitHub: /tester-here123 ") == ["GitHub: /tester-here123"])
    assert(extract(patterns, " gitlab: tester-here123 ") == ["gitlab: tester-here123"])
    print("good!")
