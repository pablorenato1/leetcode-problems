class Solution:
    def findWinners(self, matches):
        ans = [[],[]]
        games = {}
        for game in matches:
            if not (game[0] in games): games[game[0]] = 0
            if game[1] in games:
                games[game[1]] += 1
                continue
            else: games[game[1]] = 1
        for key in dict(sorted(games.items())):
            if games[key] > 1:
                continue
            elif games[key] == 1: ans[1].append(key)
            else: ans[0].append(key)
        return ans
        

if __name__ == "__main__":
    test = Solution()
    print(test.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
    pass