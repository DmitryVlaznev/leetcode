# 359. Logger Rate Limiter

# Design a logger system that receive stream of messages along with its
# timestamps, each message should be printed if and only if it is not
# printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), return true
# if the message should be printed in the given timestamp, otherwise
# returns false.

# It is possible that several messages arrive roughly at the same time.

# Example:

# Logger logger = new Logger();

# logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;

# logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;

# logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;

# logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;

# logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;

# logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;

class Logger:
    def __init__(self):
        from collections import deque
        self.timestamps = deque()
        self.messages = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.timestamps:
            oldest_message, oldest_timestamp = self.timestamps[0]
            if timestamp - oldest_timestamp < 10: break
            self.timestamps.popleft()
            self.messages.remove(oldest_message)

        if message not in self.messages:
            self.messages.add(message)
            self.timestamps.append([message, timestamp])
            return True
        return False


