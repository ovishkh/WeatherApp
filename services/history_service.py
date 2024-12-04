class HistoryService:
    """Service for managing search history."""
    def __init__(self):
        self.history = []

    def add_to_history(self, weather):
        """Add a weather search to history."""
        self.history.append(weather)

    def get_history(self):
        """Retrieve the search history."""
        return self.history
