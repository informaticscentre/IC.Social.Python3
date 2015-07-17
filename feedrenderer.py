from renderer import *
from point import *
from PIL import Image, ImageTk

class FeedRenderer(Renderer):
    def __init__(self, postsPerRow, numberOfRows, tileColor = '#ffffff', textColor = '#000000', authorColor = '#000000'):
        Renderer.__init__(self)

        self.postsPerRow = postsPerRow
        self.numberOfRows = numberOfRows
        self.tileColor = tileColor
        self.textColor = textColor
        self.authorColor = authorColor

        self.CalculatePostBounds()
        self.DrawBackgroundImage()

    def CalculatePostBounds(self):
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        self.postSpacing = 10
        totalWidthOfSpacingBetweenPosts = (self.postsPerRow - 2) * self.postSpacing
        totalHeightOfSpacingBetweenPosts = self.numberOfRows * self.postSpacing

        self.postWidth = (self.screenWidth - totalWidthOfSpacingBetweenPosts) / self.postsPerRow
        self.postHeight = (self.screenHeight - totalHeightOfSpacingBetweenPosts) / self.numberOfRows

    def DrawBackgroundImage(self):
        leftMargin = (2048 - self.screenWidth) * -1
        topMargin = (1024 - self.screenHeight) * -1
        image = Image.open('background.jpg')

        self.photoImage = ImageTk.PhotoImage(image)
        self.canvas.create_image(leftMargin, topMargin, image = self.photoImage, anchor = 'nw')

    def DrawFeed(self, feed):
        point = Point(0, 0)
        self.colorIndex = 0

        for index, post in enumerate(feed):
            self.DrawPost(post, point.x, point.y, self.postWidth, self.postHeight)
            point = self.MovePoint(point)

    def DrawPost(self, post, x, y, width, height):
        self.RotateTileColor()

        self.DrawTile((x, y, x + width, y + height))
        self.DrawText(post.text.encode('unicode_escape'), x + self.postSpacing, y + self.postSpacing, width - (2 * self.postSpacing))
        self.DrawAuthor('@' + post.author, x + self.postSpacing, (y + self.postHeight) - (2.5 * self.postSpacing), width - (2 * self.postSpacing))

    def MovePoint(self, point):
        point.x += self.postWidth + self.postSpacing

        if point.x > self.screenWidth:
            point.x = 0
            point.y += self.postHeight + self.postSpacing

        return point

    def RotateTileColor(self):
        colors = list()
        colors.append('#f9b2fb') #Pink
        colors.append('#b2f4fe') #Blue
        colors.append('#ddf2b2') #Green

        self.tileColor = colors[self.colorIndex]
        self.colorIndex += 1

        if self.colorIndex == len(colors):
            self.colorIndex = 0

    def DrawTile(self, bounds):
        self.canvas.create_rectangle(
            bounds,
            fill = self.tileColor)

    def DrawText(self, text, x, y, width):
        self.canvas.create_text(
            x, y,
            anchor = 'nw',
            fill = self.textColor,
            font = ('Cambria', 14),
            text = text,
            width = width)

    def DrawAuthor(self, author, x, y, width):
        self.canvas.create_text(
            x, y,
            anchor = 'nw',
            fill = self.authorColor,
            font = ('Cambria', 12),
            text = author,
            width = width)
