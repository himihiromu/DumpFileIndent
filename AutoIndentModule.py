class AutoIndent:
    """
    ダンプファイルなどの文字列にインデントをつけるクラス
    Attributes
    ----------
    braces : int
        {}の入れ子の数
    indent_target : str
        （や｛などのぶろっくの開始文字
    indent_target_pair　：ｓｔｒ
        indent_targetとペアになる文字
    line_feed_char
        ;などのコードの改行の文字
    """

    def __init__(self, it, pair, lf):
        self.braces=0
        self.indent_target = it
        self.indent_target_pair = pair
        self.line_feed_char = lf

    def indent(self, s):
        """
        bracesの数に応じて、indent_target_pairのまわりへのインデントをつける
        Parameters
        ----------
        s　: ｓｔｒ
            インデント対象の文字列
        Returns
        -------
        return_value : ｓｔｒ
            インデント挿入後の文字列
        """
        return_value = ""
        while True:
            num = s.find(self.indent_target_pair)

            # 文字列中にはindent_target_pairがなかった
            if num == -1:
                self.braces += 1
                return_value += '\t' * self.braces + s
                break

            # 先頭にindent_target_pairを発見
            elif num == 0:
                return_value += '\t' * self.braces + self.indent_target_pair
                s = s[1:]

            # 文字列中にindent_target_pairを発見
            else:
                return_value += '\t' * (self.braces + 1) + s[0:num] + '\n' + '\t' * self.braces + self.indent_target_pair + '\n'
                self.braces -= 1
                s = s[num + 1:]

            # 終了
            if s == []:
                break
        return return_value

    def new_line(self, string):
        return '\n'.join(map(lambda x : x + self.line_feed_char, string.split(self.line_feed_char)))

    def add_indent(self, string):
        """
        文字列にインデントをつける
        Parameters
        ----------
        string　: ｓｔｒ
            インデント対象の文字列
        Returns
        -------
        return_value : ｓｔｒ
            インデント挿入後の文字列
        """
        # indent_targetで分割
        s_list = string.split(self.indent_target)
        return_value = s_list.pop(0) + self.indent_target + '\n'

        # 分割の際に消えてしまったindent_targetを付け加え、インデントをつける
        tmp_list = list(map(lambda x: x + self.indent_target + '\n', s_list[:-1])) + s_list[-1:]
        result_list = list(map(self.indent, tmp_list))

        return self.new_line(return_value + ''.join(result_list))