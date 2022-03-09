from collections import defaultdict
import re


class ParseHelper:
    def split(string, brackets_on_first_result=False):
        matches = re.split("[\[\]]+", string)
        matches.remove("")
        return matches

    def parse(self, params):
        results = {}
        for key in params:
            if "[" in key:
                key_list = self.split(key)
                d = results
                for partial_key in key_list[:-1]:
                    if partial_key not in d:
                        d[partial_key] = dict()
                    d = d[partial_key]
                d[key_list[-1]] = params[key]
            else:
                results[key] = params[key]
        return results
