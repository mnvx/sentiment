class SentimentType:

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"

    @staticmethod
    def get_significant():
        return [
            SentimentType.POSITIVE,
            SentimentType.NEGATIVE,
        ]

    @staticmethod
    def get_list():
        return [
            SentimentType.POSITIVE,
            SentimentType.NEGATIVE,
            SentimentType.NEUTRAL,
        ]
