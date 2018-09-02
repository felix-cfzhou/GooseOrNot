from server.ml.boost import is_goose


def test_is_goose(goose_pic_filename, notgoose_pic_filename):
    assert(is_goose(goose_pic_filename))
    assert(not is_goose(notgoose_pic_filename))
