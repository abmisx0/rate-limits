import json


# Data Struct to store Pool information
class PoolData:
    def __init__(self, address: str):
        self.address = address
        self.voting_power = 0

    def to_dict(self):
        return {"address": self.address, "voting_power": self.voting_power}

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


# Data Struct to store Chain information
class ChainData:
    def __init__(self, name: str, rpc_url: str):
        self.pools = []
        self.name = name
        self.rpc_url = rpc_url
        self.total_voting_weight = 0
        self.existing_buffer_cap = 0
        self.existing_rate_limit = 0
        self.expected_emissions = 0
        self.existing_midpoint = 0
        self.current_limit = 0

    def __repr__(self):
        return f"Name: {self.name}\nTotal Voting Weight: {self.total_voting_weight}\nExpected Emissions: {self.expected_emissions}\nExisting Buffer Cap: {self.existing_buffer_cap}\nExisting Rate Limit: {self.existing_rate_limit}\nPools={self.pools}\n"


# Data Struct to store new limits for each Chain
class NewLimitData:
    def __init__(self, name: str, new_buffer_cap: int, new_rate_limit: int, temporary_rate_limit: int):
        self.name = name
        self.new_buffer_cap = new_buffer_cap
        self.new_rate_limit = new_rate_limit
        self.temporary_rate_limit = temporary_rate_limit

    def __repr__(self):
        if self.temporary_rate_limit == 0:
            return f"Name: {self.name}\nNew Buffer Cap: {self.new_buffer_cap:.0f}\nNew Rate Limit: {self.new_rate_limit:.0f}"
        else:
            return f"Name: {self.name}\nNew Buffer Cap: {self.new_buffer_cap:.0f}\nTemporary Rate Limit: {self.temporary_rate_limit:.0f}\nRate Limit Post Replenishment: {self.new_rate_limit:.0f}"
