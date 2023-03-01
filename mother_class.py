class post:
    def __init__(self, nikname, date, text):
        self.nikname = nikname
        self.date = date
        self.likes = 0
        self.text = text
        self.comments = []

    def add_likes(self, how_much):
        try:
            how_much = int(how_much)
        except (ValueError, TypeError):
            self.likes = 'ERROR'
            print("Количество лайков указывается числом, а не буквами!!!")
        else:
            self.likes += how_much

    def add_comment(self, comment_text):
        if 'сволоч' in comment_text.lower():
            pass
        else:
            self.comments.append(comment_text)

    def get_all_comments(self):
        return self.comments

    def __str__(self):
        return f'Nickname: {self.nikname}, date: {self.date}, text: {self.text} likes: {self.likes}, comments: {(self.comments[:3])}'