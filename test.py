from utils import get_config, extract

if __name__ == "__main__":
    pattern = get_config()["pattern"]

    assert(extract(pattern, " some text github.com/username-HERE123") == ["github.com/username-HERE123"])
    assert(extract(pattern, " some text gitlab.com/test0, and gitlab.com/test1") == ["gitlab.com/test0", "gitlab.com/test1"])
    assert(extract(pattern, " my-name-is.github.io a") == ["my-name-is.github.io"])
    print("good!")
