import types
import os
from decorator_2 import logger


path = 'application_operation.log'

@logger(path)
def flat_generator(list_of_list):

    def __reqursiya(s):
        if s == []:
            return s
        if isinstance(s[0], list):
            return(__reqursiya(s[0]) + __reqursiya(s[1:]))
        return(s[:1] + __reqursiya(s[1:]))

    new_list = __reqursiya(list_of_list)
    for item in new_list:
        yield item

@logger(path)
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    list_of_lists_2 = [i for i in flat_generator(list_of_lists_2)]
    print(flat_generator(list_of_lists_2))
    print(list_of_lists_2)


if __name__ == '__main__':

    if os.path.exists(path):
        os.remove(path)

    test_4()