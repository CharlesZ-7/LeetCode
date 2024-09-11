class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        email_to_index = defaultdict(set)
        
        for index in range(n):
            for email in accounts[index][1:]:
                email_to_index[email].add(index)

        def dfs(index, visited, emails):
            visited.add(index)
            for email in accounts[index][1:]:
                emails.add(email)
                for neighbor in email_to_index[email]:
                    if neighbor not in visited:
                        dfs(neighbor, visited, emails)

        visited = set()
        merged_accounts = []

        for index in range(n):
            if index not in visited:
                name = accounts[index][0]
                emails = set()
                dfs(index, visited, emails)
                merged_accounts.append([name] + sorted(emails))

        return merged_accounts