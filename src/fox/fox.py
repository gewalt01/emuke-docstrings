"""
きつねさんのライブラリ
"""


class Fox:
    """きつねさんクラス

    Attributes:
        name (str): きつねさんのお名前
    """

    def __init__(self, name: str):
        """きつねさん誕生。うまれる！！！

        Args:
            name (str): おなまえ

        Examples:
            アカギツネ登場！！！
            >>> red_fox = Fox("アカギツネ")
        
        Raises:
            TypeError: nameが文字列じゃないとおこだよ。
        """
        if type(name) is str:
            raise TypeError("str型入れろ！！！")
        self.name = name

    def schrei():
        """こやこやと鳴く
        """
        print("こやこや")

    def get_name() -> str:
        """きつねさんのお名前を返す

        Returns:
            str: お名前
        """
        return self.name

    