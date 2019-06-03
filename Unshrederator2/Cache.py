from gutenberg.acquire.metadata import SqliteMetadataCache, set_metadata_cache, get_metadata_cache


def load_cache():
    cache = SqliteMetadataCache('C:/Users/Laszlo/Desktop/Unshrederator2/cache/cache.sqlite')
    cache.populate()
    set_metadata_cache(cache)

def load_cache_default():
    cache = get_metadata_cache()
    cache.populate()