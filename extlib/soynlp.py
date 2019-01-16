import re


class RegexTokenizer:

    def __init__(self):
        self._patterns = [
            ('number', re.compile(r'[-+]?\d*[.]?[\d]+|[-+]?\d+', re.UNICODE)),
            ('korean', re.compile(r'[가-힣]+', re.UNICODE)),
            ('josa', re.compile(r'[은는]', re.UNICODE)),
            ('jaum', re.compile(r'[ㄱ-ㅎ]+', re.UNICODE)),
            ('moum', re.compile(r'[ㅏ-ㅣ]+', re.UNICODE)),
            ('english & latin', re.compile(r"[a-zA-ZÀ-ÿ]+[[`']?s]*|[a-zA-ZÀ-ÿ]+", re.UNICODE))
        ]

        self.double_white_pattern = re.compile(r'\s+')

    def __call__(self, s, debug=True, flatten=True):
        return self.tokenize(s, flatten)

    def tokenize(self, s, flatten=True):
        tokens = [self._tokenize(t) for t in s.split()]
        if flatten:
            tokens = [subtoken for token in tokens for subtoken in token if subtoken]
        return tokens

    def _tokenize(self, s):
        for name, pattern in self._patterns:

            founds = pattern.findall(s)
            if not founds:
                continue

            found = founds.pop(0)
            len_found = len(found)

            s_ = ''
            b = 0
            for i, c in enumerate(s):

                if b > i:
                    continue

                if s[i:i + len_found] == found:
                    s_ += ' %s ' % s[i:i + len_found]
                    b = i + len_found

                    if not founds:
                        s_ += s[b:]
                        break
                    else:
                        found = founds.pop(0)
                        len_found = len(found)

                    continue
                s_ += c
            s = s_

        s = self.double_white_pattern.sub(' ', s).strip().split()
        return s
