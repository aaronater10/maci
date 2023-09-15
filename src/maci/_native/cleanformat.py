# cleanformat
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import List as _List
from typing import Any as _Any
from ..error import CleanFormat

#########################################################################################################
# Format data cleanly for string
def cleanformat(data: _Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a dict, list, tuple, or set, to a clean multiline structure to string

    [Example Use]
    
    var = cleanformat(data)

    Maci docs: https://docs.macilib.org
    """
    # Error Checks, Set indent level
    err_type = "Only dict|list|tuple|set is allowed for 'data'"
    err_indent = "Only int is allowed for 'indent_level'"

    if not isinstance(indent_level, int):
        raise CleanFormat(err_indent, f'\nGot: {indent_level!r}')

    if not isinstance(data, (dict,list,tuple,set)):
        raise CleanFormat(err_type, f'\nGot: {data!r}')


    # Setup
    build_data_stack = []
    dict_kv_marker_signal = object()
    
    # Check Initial Type and Return Formatted Data

    # List
    if isinstance(data, list):
        build_data_stack.extend([*data])
        return __format_data(stack=build_data_stack, initial_type='list', indent_level=indent_level, dict_kv_marker_signal=dict_kv_marker_signal)

    # Dict
    elif isinstance(data, dict):        
        build_data_stack.extend([(dict_kv_marker_signal, key, value)  # build a 3-tuple of kv signal, true key, true value
            for key,value in data.items()
            ]
        )
        return __format_data(stack=build_data_stack, initial_type='dict', indent_level=indent_level, dict_kv_marker_signal=dict_kv_marker_signal)

    # Tuple
    elif isinstance(data, tuple):
        build_data_stack.extend([*data])
        return __format_data(stack=build_data_stack, initial_type='tuple', indent_level=indent_level, dict_kv_marker_signal=dict_kv_marker_signal)

    # Set
    elif isinstance(data, set):  # pragma: no branch
        build_data_stack.extend([*data])
        return __format_data(stack=build_data_stack, initial_type='set', indent_level=indent_level, dict_kv_marker_signal=dict_kv_marker_signal)


#########################################################################################################
# Functions
def __format_data(stack: _List[_Any], initial_type: str, indent_level: int, dict_kv_marker_signal: object) -> str:
    """
    Format/Prep Dict, List, Tuple, or Set data for str

    "initial_type" options: 'list', 'set', 'tuple', 'dict'
    """
    # Error Checks - Internal
    if not isinstance(stack, list): raise Exception(f"'stack' received non-list type: Got\n{stack!r}")  # pragma: no cover  # internal check only
    if not isinstance(initial_type, str): raise Exception(f"'initial_type' received non-str type: Got\n{initial_type!r}")  # pragma: no cover  # internal check only
    if not isinstance(indent_level, int): raise Exception(f"'indent_level' received non-int type: Got\n{indent_level!r}")  # pragma: no cover  # internal check only
    if not (type(dict_kv_marker_signal) == type(object())): raise Exception(f"'dict_kv_marker_signal' received not pure 'object' type: Got\n{indent_level!r}")  # pragma: no cover  # internal check only

    # Setup
    indent_space = '    ' * indent_level  # str is 4x spaces
    level_track = 1
    write_str_list_build = []
    dict_kv_marker_signal = dict_kv_marker_signal
    dict_end_marker_signal = object()
    list_end_marker_signal = object()
    set_end_marker_signal = object()
    tuple_end_marker_signal = object()

    # Check initial type
    if initial_type == 'list':
        write_str_list_build.append('[')  # start marker
        stack.append(list_end_marker_signal)  # end marker

    elif initial_type == 'dict':
        write_str_list_build.append('{')  # start marker
        stack.append(dict_end_marker_signal)  # end marker
    
    elif initial_type == 'tuple':
        write_str_list_build.append('(')  # start marker
        stack.append(tuple_end_marker_signal)  # end marker
    
    elif initial_type == 'set':  # pragma: no branch
        write_str_list_build.append('{')  # start marker
        stack.append(set_end_marker_signal)  # end marker    
    

    # Walk/Process Items in Stack to Build Final Write String
    while stack:
        stack_item = stack.pop(0)
        
        # List
        if isinstance(stack_item, list):
            write_str_list_build.append(f'{indent_space * level_track}[')
            stack[:0] = [*stack_item, list_end_marker_signal]
            level_track += 1
            continue

        if stack_item is list_end_marker_signal:
            level_track -= 1
            write_str_list_build.append(f'{indent_space * level_track}],')
            continue

        # Set
        if isinstance(stack_item, set):
            write_str_list_build.append(f'{indent_space * level_track}{{')
            stack[:0] = [*stack_item, set_end_marker_signal]
            level_track += 1
            continue

        if stack_item is set_end_marker_signal:
            level_track -= 1
            write_str_list_build.append(f'{indent_space * level_track}}},')
            continue

        # Tuple: Non KV Pair with Special Signal from (3-Tuple)
        if (isinstance(stack_item, tuple)) and (dict_kv_marker_signal not in stack_item):
            write_str_list_build.append(f'{indent_space * level_track}(')
            stack[:0] = [*stack_item, tuple_end_marker_signal]
            level_track += 1
            continue

        if stack_item is tuple_end_marker_signal:
            level_track -= 1
            write_str_list_build.append(f'{indent_space * level_track}),')
            continue

        # Dict
        if isinstance(stack_item, dict):
            write_str_list_build.append(f'{indent_space * level_track}{{')
            dict_stack_items = [(dict_kv_marker_signal, key, value)  # build a 3-tuple of kv signal, true key, true value
                         for key,value in stack_item.items()
            ]
            stack[:0] = [*dict_stack_items, dict_end_marker_signal]
            level_track += 1
            continue
        
        # Dict: KV Pair with Special Signal from (3-Tuple)
        if (isinstance(stack_item, tuple)) and (dict_kv_marker_signal in stack_item):
            
            # Dict Value: List
            if isinstance(stack_item[2], list):
                write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item[1])}: [')
                stack[:0] = [*stack_item[2], list_end_marker_signal]
                level_track += 1
                continue
            
            # Dict Value: Set
            if isinstance(stack_item[2], set):
                write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item[1])}: {{')
                stack[:0] = [*stack_item[2], set_end_marker_signal]
                level_track += 1
                continue
            
            # Dict Value: Tuple
            if isinstance(stack_item[2], tuple):
                write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item[1])}: (')
                stack[:0] = [*stack_item[2], tuple_end_marker_signal]
                level_track += 1
                continue
            
            # Dict Value: Dict
            if isinstance(stack_item[2], dict):
                write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item[1])}: {{')
                sub_dict_stack_items = [(dict_kv_marker_signal, key, value)  # build a 3-tuple of kv signal, true key, true value
                            for key,value in stack_item[2].items()
                ]
                stack[:0] = [*sub_dict_stack_items, dict_end_marker_signal]
                level_track += 1
                continue

            write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item[1])}: {repr(stack_item[2])},')
            continue

        if stack_item is dict_end_marker_signal:
            level_track -= 1
            write_str_list_build.append(f'{indent_space * level_track}}},')
            continue

        
        # Always add remaining types/values
        write_str_list_build.append(f'{indent_space * level_track}{repr(stack_item)},')        


    # Return Final String Build with each element separated by New Lines, Remove trailing comma
    return '\n'.join(write_str_list_build)[:-1]
