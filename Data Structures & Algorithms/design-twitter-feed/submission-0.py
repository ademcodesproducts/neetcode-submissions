class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_store = defaultdict(list)
        self.followers = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweet_store[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee in self.followers[userId]:
            heap.extend(self.tweet_store[followee])
        if userId not in self.followers[userId]:
            heap.extend(self.tweet_store[userId])
        
        heapq.heapify(heap)

        news = []
        while heap and len(news) < 10:
            _, tweetId = heapq.heappop(heap)
            news.append(tweetId)
        return news
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)